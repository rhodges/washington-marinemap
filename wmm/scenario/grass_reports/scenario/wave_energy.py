from scenario.models import *
from utils import transpose_nested_dict, get_dict_from_stats, clean_stats_list

def wave_energy_report(g, summer_query, winter_query, scenario):
    wave_report = {}
    
    # Scenario 
    
    #substrate stats -- collecting area (in meters) for each substrate represented in the resulting scenario
    substrate_result = """r.mapcalc "subresult = if(rresult==1,substrate,null())" """
    g.run(substrate_result)
    #r.stats -an generates area stats with area totals (-a), while ignoring null values (-n) (those areas outside of overlap)
    substrate_name_dict, substrate_dict = get_dict_from_stats(g, Substrate, 'subresult')
    wave_report['substrate'] = substrate_name_dict    
    
    # Wave Potential
    
    result_area = get_area_from_stats(g, 'rresult')
    
    #Summer 
    if summer_query != 1:
        summer_wave = """r.mapcalc "summerresult = if(%s==1,1,null())" """ %summer_query
        g.run(summer_wave)
        summer_wave_area = get_area_from_stats(g, 'summerresult')
        percent_summer = result_area / summer_wave_area
        wave_report['percent_summer'] = percent_summer    
    
    #Winter
    if winter_query != 1: 
        winter_wave = """r.mapcalc "winterresult = if(%s==1,1,null())" """ %winter_query
        g.run(winter_wave)
        winter_wave_area = get_area_from_stats(g, 'winterresult')
        percent_winter = result_area / winter_wave_area
        wave_report['percent_winter'] = percent_winter
    
    # Substrate with Wave Potential
    
    # Summer -- how much of the Sand/Summer-Energy-Range did we capture?, etc
    summer_sub_dict = {}
    winter_sub_dict = {}
    for name, area in substrate_name_dict.items():
        sub_id = Substrate.objects.get(short_name=name).id
        sub_name = Substrate.objects.get(short_name=name).name
        sub_result_area = area
        
        #resulting_sand_summer_wave_area / total_sand_summer_wave_area
        #assuming resulting_sand_area == resulting_sand_summer_wave_area?
        if summer_query != 1:
            total_sub_summer_wave = """r.mapcalc "total_summer_wave_%s = if(substrate==%s,summerresult,null())" """ %(name, sub_id)
            g.run(total_sub_summer_wave)
            total_sub_summer_area = get_area_from_stats(g, 'total_summer_wave_%s'%name)
            sub_summer_perc = sub_result_area / total_sub_summer_area 
            summer_sub_dict[sub_name] = sub_summer_perc
        if winter_query != 1: 
            total_sub_winter_wave = """r.mapcalc "total_winter_wave_%s = if(substrate==%s,winterresult,null())" """ %(name, sub_id)
            g.run(total_sub_winter_wave)
            total_sub_winter_area = get_area_from_stats(g, 'total_winter_wave_%s'%name)  
            sub_winter_perc = sub_result_area / total_sub_winter_area 
            winter_sub_dict[sub_name] = sub_winter_perc
    if summer_query != 1:    
        wave_report['sub_summer_percs'] = summer_sub_dict
    if winter_query != 1: 
        wave_report['sub_winter_percs'] = winter_sub_dict
    return simplejson.dumps(wave_report)

def get_area_from_stats(g, input_rast):
    grass_output = g.run('r.stats -an input=%s' %input_rast)
    stats_list = grass_output.split()
    #int_list = [int(float(x)+.5) for x in stats_list]
    stats_dict = dict(zip(stats_list[::2], stats_list[1::2])) 
    return float(stats_dict['1'])

"""    
#WORTH REMEMBERING: r.surf.area does not return the same value as r.stats -an
#                   sometimes the difference is small (<5%) other times the difference is a factor of 2 or 3    
def get_surface_area(g, input_rast): 
    #r.stats -an generates area stats with area totals (-a), while ignoring null values (-n) (those areas outside of overlap)
    grass_output = g.run('r.surf.area input=%s' %input_rast)  
    #grass_output is something like the following: 'blah blah blah Surface Area: 2.172555e+009\n\nDone.\n'
    begin_index = grass_output.rfind('Area: ') + 6
    area_output = grass_output[begin_index:]
    #area_output is now something like: '2.172555e+009\n\nDone.\n'
    end_index = area_output.find('\n')
    surface_area = float(area_output[:end_index])
    #surface_area is something like: 2172555000
    return surface_area
"""
from django.utils import simplejson
from scenario.models import *


def get_scenario_stats(scenario, param_dict, model_class, param_area_class):  
    scenario_area = scenario.output_area
    stats = {} 
    for key,value in param_dict.items():
        perc = value / scenario_area * 100
        if perc > 0:
            #stats[key] = (int(perc*10 + .5) / 10., sq_meters_to_sq_miles(value))
            if perc > .05:
                stats[key] = (int(perc*10 + .5) / 10., value)
            elif perc > .005:
                stats[key] = (int(perc*100 + .5) / 100., value)
            elif perc > .0005:
                stats[key] = (int(perc*1000 + .5) / 1000., value)
            elif perc > .00005:
                stats[key] = (int(perc*10000 + .5) / 10000., value)
            else:
                stats[key] = (int(perc*100000 + .5) / 100000., value)
    #arrays not dicts as ordering matters for coloration (at least for now...)
    sorted_tuples, list_reverse = sort_dict(stats, model_class, param_area_class)
    jstats = simplejson.dumps(sorted_tuples) 
    return jstats, list_reverse
     
def sort_dict(param_dict, model_class, param_area_class):
    params = model_class.objects.order_by('-id')
    sorted_tuples = []
    ordered_list = []
    for param in params:        
        if param.short_name in param_dict.keys():
            try:
                total_param_area = param_area_class.objects.get(name=param.short_name).area
            except:
                total_param_area = None
            if total_param_area is not None:
                perc = param_dict[param.short_name][1] / total_param_area * 100
                if perc == 100:
                    perc = int(perc)
                    tooltip_text = "%s%s of available %s" %(perc, '%', param.name)
                else:
                    tooltip_text = "%.2f%s of available %s" %(perc, '%', param.name)
            else:
                tooltip_text = "Data Unavailable"
            #tooltip_text = "Total Area: %.2f sq miles" %param_dict[param.name][1]
            sorted_tuples.append( [param_dict[param.short_name][0], param.name, tooltip_text] )
            ordered_list.append(param)
    ordered_list.reverse()
    return sorted_tuples, ordered_list
      
def get_drill_down_stats(scenario, dictionary, outer_class, inner_class, param_area_class):  
    stats = {}
    for outer_short_name, param_dict in dictionary.items():
        outer_name = outer_class.objects.get(short_name=outer_short_name).name
        total_area = float( sum( [area for param, area in param_dict.items()] ) )
        param_perc_dict = {}
        param_perc_list = []
        ordered_inner_params = inner_class.objects.all().order_by('-id')
        for inner_param in ordered_inner_params:
            if inner_param.short_name in param_dict.keys():
                inner_name = inner_param.name
                inner_short_name = inner_param.short_name
                area = param_dict[inner_short_name]
        #for inner_short_name, area in param_dict.items():
            #inner_name = inner_class.objects.get(short_name=inner_short_name).name
                drill_down_name = '%s_%s' %(outer_short_name, inner_short_name)
                total_param_area = param_area_class.objects.get(name=drill_down_name).area
                if total_param_area is not None:
                    perc = param_dict[inner_short_name] / total_param_area * 100
                    if perc == 100:
                        perc = int(perc)
                        tooltip_text = "%s%s of available %s/%s" %(perc, '%', inner_name, outer_name)
                    else:
                        tooltip_text = "%.2f%s of available %s/%s" %(perc, '%', inner_name, outer_name)
                else:
                    tooltip_text = "Data Unavailable"
                #tooltip_text = "Total Area: %.2f sq miles" %sq_meters_to_sq_miles(area)
                perc = int(area / total_area * 1000 + .5) / 10.
                if perc == 0.0:
                    perc = int(area / total_area * 10000 + .5) / 100.
                if perc == 0.0:
                    perc = int(area / total_area * 100000 + .5) / 1000.
                param_perc_list.append([perc, inner_name, tooltip_text])
        stats[outer_short_name] = param_perc_list
    jstats = simplejson.dumps(stats)
    return jstats
              
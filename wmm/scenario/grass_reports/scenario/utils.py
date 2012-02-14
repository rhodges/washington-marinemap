from scenario.models import *

def transpose_nested_dict(orig_dict):
    transposed_dict = {}
    for key, value in orig_dict.items():
        for inner_key, area in value.items():
            if inner_key not in transposed_dict.keys():
                transposed_dict[inner_key] = {key: area}
            else:
                transposed_dict[inner_key][key] = area
    return transposed_dict

def get_raster_area(g, input_rast):
    grass_output = g.run('r.stats -an input=%s' %input_rast)
    stats_list = grass_output.split()
    #int_list = [int(float(x)+.5) for x in stats_list]
    stats_dict = dict(zip(stats_list[::2], stats_list[1::2])) 
    if len(stats_dict.keys()) == 1:
        return float(stats_dict['1'])
    else:
        return 0.0  
    
def get_dict_from_stats(g, model_class, input_rast):  
    #r.stats -an generates area stats with area totals (-a), while ignoring null values (-n) (those areas outside of overlap)
    stats = g.run('r.stats -an input=%s' %input_rast)  
    #stats is something like the following: '2 1360911.649924\n4 2940800464.852541\n'
    stats_list = stats.split()
    #stats_list becomes: ['2', '1360911.649924', '4', '2940800464.852541']
    clean_list = clean_stats_list(stats_list)
    int_list = [int(float(x)+.5) for x in clean_list]
    #int_list becomes: [2, 1360911, 4, 2940800464]
    stats_dict = dict(zip(int_list[::2], int_list[1::2])) 
    #stats_dict becoms: {2: 1360911, 4: 2940800464}
    name_dict = {}
    for key, area in stats_dict.items():
        try:
            name_dict[model_class.objects.get(id=key).short_name] = area
        except:
            print "failed to find %s object with id=%s" %(model_class, key)
    #name_dict = dict( map( lambda(key, value): (model_class.objects.get(id=key).short_name, value), stats_dict.items()))
    #name_dict finally becomes: {'Flat': 1360911, 'Slope': 2940800464}
    return name_dict, stats_dict

def clean_stats_list(list):
    clean_list = []
    #note the following '-' search is taking care to remove possible range values in stats list
    for item in list:
        if '-' in item:
            clean_list.append( item[:item.find('-')] )
        else:
            clean_list.append(item)
    return clean_list

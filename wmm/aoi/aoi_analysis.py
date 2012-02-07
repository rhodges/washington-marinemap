from conservation.physical import display_aoi_physical_analysis
from conservation.biological import display_aoi_biological_analysis
from energy.wind import display_aoi_wind_analysis
from energy.wave import display_aoi_wave_analysis
from energy.tidal import display_aoi_tidal_analysis

'''
calls display_<type>_analysis for a given type
called by views.aoi_analysis
'''
def display_aoi_analysis(request, aoi_obj, type):
    if type == 'physical':
        return display_aoi_physical_analysis(request, aoi_obj)
    elif type == 'biological':
        return display_aoi_biological_analysis(request, aoi_obj)
    elif type == 'wind':
        return display_aoi_wind_analysis(request, aoi_obj)
    elif type == 'wave':
        return display_aoi_wave_analysis(request, aoi_obj)
    elif type == 'tidal':
        return display_aoi_tidal_analysis(request, aoi_obj)
    else:
        raise ValueError('Unrecognized type, %s, sent to display_aoi_analysis' %type)
from general.wind_general import display_wind_general_analysis
from energy.wind_energy import display_wind_energy_analysis

'''
calls display_<type>_analysis for a given type
called by views.conservation_analysis
'''
def display_wind_analysis(request, wind_obj, type):
    if type == 'general':
        return display_wind_general_analysis(request, wind_obj)
    elif type == 'energy':
        return display_wind_energy_analysis(request, wind_obj)
    else:
        raise ValueError('Unrecognized type, %s, sent to display_wind_analysis' %type)
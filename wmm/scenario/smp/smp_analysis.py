from beach_erosion import display_smp_beach_erosion_analysis
from shoreline_use import display_smp_shoreline_use_analysis
from public_access import display_smp_public_access_analysis
from aquaculture import display_smp_aquaculture_analysis

'''
calls display_<type>_analysis for a given type
called by views.conservation_analysis
'''
def display_smp_analysis(request, smp_obj, type):
    if type == 'beach_erosion':
        return display_smp_beach_erosion_analysis(request, smp_obj)
    elif type == 'shoreline_use':
        return display_smp_shoreline_use_analysis(request, smp_obj)
    elif type == 'public_access':
        return display_smp_public_access_analysis(request, smp_obj)
    elif type == 'aquaculture':
        return display_smp_aquaculture_analysis(request, smp_obj)
    else:
        raise ValueError('Unrecognized type, %s, sent to display_smp_analysis' %type)
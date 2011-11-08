from physical.conservation_physical import display_cs_phy_analysis
from biological.conservation_biological import display_cs_bio_analysis

'''
calls display_<type>_analysis for a given type
called by views.conservation_analysis
'''
def display_conservation_analysis(request, cs, type):
    if type == 'phy':
        return display_cs_phy_analysis(request, cs)
    elif type == 'bio':
        return display_cs_bio_analysis(request, cs)
    else:
        raise ValueError('Unrecognized type, %s, sent to display_conservation_analysis' %type)
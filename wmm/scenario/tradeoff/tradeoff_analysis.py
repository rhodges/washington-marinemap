from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from scenario.models import *
from settings import *
from scenario.utils import default_value

'''
'''
def display_tradeoff_analysis(request, folder_obj, template='folder/reports/tradeoff_report.html'):
    context = get_tradeoff_context(folder_obj)
    return render_to_response(template, RequestContext(request, context)) 

'''
'''    
def get_tradeoff_context(folder_obj): 
    #get context from cache or from running analysis
    context = run_tradeoff_analysis(folder_obj)   
    return context
    
'''
Run the analysis, create the cache, and return the results as a context dictionary so they may be rendered with template
'''    
def run_tradeoff_analysis(folder_obj): 
    conservation_site_1 = [75, 23, 16, 'Point Beach']
    conservation_site_2 = [65, 82, 17, "Seal Cove"]
    conservation_site_3 = [84, 10, 26, "Beach Sands"]
    conservation_site_4 = [50, 33, 10, "Seagull Lookout"]
    conservation_sites = [conservation_site_1, conservation_site_2, conservation_site_3, conservation_site_4]
    conservation_colors = [ "#4bb2c5", "#4bb2c5", "#4bb2c5", "#4bb2c5" ]
    windenergy_site_1 = [18, 67, 9, "Blustery Ave"]
    windenergy_site_2 = [67, 89, 14, "Breeze Way"]
    windenergy_site_3 = [12, 73, 16, "Wind Alley"]
    windenergy_sites = [windenergy_site_1, windenergy_site_2, windenergy_site_3]
    windenergy_colors = [ "#c5b47f", "#c5b47f", "#c5b47f" ]
    #the following works as well, but not sure why i should bother with this when the previous line works...
    #from django.utils import simplejson
    #conservation_sites = simplejson.dumps([conservation_site_1])
    #compile context
    context = {'default_value': default_value, 'conservation_sites': conservation_sites, 'conservation_colors': conservation_colors, 'windenergy_sites': windenergy_sites, 'windenergy_colors': windenergy_colors}
    return context
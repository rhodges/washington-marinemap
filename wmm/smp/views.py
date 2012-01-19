from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from models import *
import settings

'''
'''
def smp_analysis(request, smp_id, type):
    from smp.smp_analysis import display_smp_analysis
    smp_obj = get_object_or_404(SMPSite, pk=smp_id)
    #check permissions
    viewable, response = smp_obj.is_viewable(request.user)
    if not viewable:
        return response
    return display_smp_analysis(request, smp_obj, type)
    
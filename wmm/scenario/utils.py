

default_value = '---'

def kmlcolor_to_htmlcolor(kmlcolor):
    return str('#' + kmlcolor[6] + kmlcolor[7] + kmlcolor[4] + kmlcolor[5] + kmlcolor[2] + kmlcolor[3] )
    
def miles_to_meters(miles):
    return int(miles * 1609.344)
    
def feet_to_meters(feet):
    return int(feet * .3048)
    
def sq_meters_to_sq_miles(sq_meters):
    return sq_meters * .000000386102159
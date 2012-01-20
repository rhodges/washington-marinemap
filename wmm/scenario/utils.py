
default_value = '---'

def kmlcolor_to_htmlcolor(kmlcolor):
    return str('#' + kmlcolor[6] + kmlcolor[7] + kmlcolor[4] + kmlcolor[5] + kmlcolor[2] + kmlcolor[3] )
    
def miles_to_meters(miles):
    return int(miles * 1609.344)
    
def meters_to_miles(meters):
    return meters * 0.000621371192
    
def feet_to_meters(feet):
    return int(feet * .3048)
    
def sq_meters_to_sq_miles(sq_meters):
    return sq_meters * .000000386102159
    
def intcomma(value): #grabbed this from humanize templatetag to help format numbers in kml balloons
    """
    Converts an integer to a string containing commas every three digits.
    For example, 3000 becomes '3,000' and 45000 becomes '45,000'.
    """
    from django.utils.encoding import force_unicode
    orig = force_unicode(value)
    import re
    new = re.sub("^(-?\d+)(\d{3})", '\g<1>,\g<2>', orig)
    if orig == new:
        return new
    else:
        return intcomma(new)    
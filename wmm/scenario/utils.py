
   
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

default_value = '---'


def get_tradeoff_score(model_class, model_geometry):
    scoring_objects = model_class.objects.filter(geometry__bboverlaps=model_geometry)
    total_area = 0.0
    total_score = 0.0
    
    for scoring_object in scoring_objects:
        scoring_geom = scoring_object.geometry
        overlap = scoring_geom.intersection(model_geometry)
        if overlap.area > 0:
            total_area += overlap.area
            total_score += scoring_object.score * overlap.area
    if total_area > 0:
        return total_score / total_area
    else:
        return 0

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
    
def sq_meters_to_acres(sq_meters):
    return sq_meters * .000247104393
    
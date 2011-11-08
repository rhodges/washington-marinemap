

default_value = '---'

def kmlcolor_to_htmlcolor(kmlcolor):
    return str('#' + kmlcolor[6] + kmlcolor[7] + kmlcolor[4] + kmlcolor[5] + kmlcolor[2] + kmlcolor[3] )
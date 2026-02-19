# start of main.py

def avalanche_risk(snow_depth, slope):
    status = 'Safe'
    if (snow_depth == 'Moderate' or snow_depth == 'Deep') and (slope == 'Steep' or slope == 'Very Steep'):
        status = 'Risky'
    return status

# end of main.py


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
	# within will hold the cities that fall within the specified region
    within = []
    temp = 0
    
	# Changing type of coordinates from string to float
    lat1 = float(lat1)
    lon1 = float(lon1)
    lat2 = float(lat2)
    lon2 = float(lon2)

    # Normalizing data so the first set of coordinates are always the highest number
    if lat1 >= lat2:
        pass
    else:
        temp = lat1
        lat1 = lat2
        lat2 = temp

    if lon1 >= lon2:
        pass
    else:
        temp = lon1
        lon1 = lon2
        lon2 = temp
	
	# TODO Ensure that the lat and lon values are all floats
	# Go through each city and check to see if it falls within 
	# the specified coordinates.

    for c in cities:
        if (c.lat <= lat1 and c.lat >= lat2 and c.lon <= lon1 and c.lon >= lon2):
            within.append(c)
    print(within)
    return within
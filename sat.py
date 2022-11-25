from skyfield.api import load, wgs84
from skyfield.api import EarthSatellite



stations_url = 'http://celestrak.org/NORAD/elements/gp.php?GROUP=active&FORMAT=tle'
satellites = load.tle_file(stations_url)

print(len(satellites))


def calc_pos(sat, bluffton, t):
    geocentric = sat.at(t)
    #print(geocentric.position.km)

    lat, lon = wgs84.latlon_of(geocentric)
    #print('Latitude:', lat)
    #print('Longitude:', lon)


    difference = sat - bluffton

    topocentric = difference.at(t)
    #print(topocentric.position.km)

    alt, az, distance = topocentric.altaz()
    #print('Altitude:', alt)
    #print('Azimuth:', az)
    if (alt.degrees > 45):
        print('Distance: {:.1f} km'.format(distance.km), alt.degrees, sat)
    #print("time" , t.utc_iso())
    
    


loc = wgs84.latlon(+37.389, -122.1469)


sat = satellites[80]


ts = load.timescale()

t = ts.now()

for sat in satellites:
    calc_pos(sat, loc, t)



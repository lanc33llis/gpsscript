import gpsd

gps = gpsd
gps.connect(host="0.0.0.0", port=2947)
gps.GpsResponse.mode = 1

print(gps.device())
gps.get_current()
print(gps.GpsResponse.altitude)

























































































































































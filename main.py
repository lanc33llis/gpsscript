import gpsd

gpsd.connect(host="0.0.0.0", port=2947)

gps = gpsd()
gps.connect(host="0.0.0.0", port=2947)
gps.GpsResponse.mode = 0
print(gps.device())
print(gps.getcurrent())

























































































































































import gpsd, subprocess


gpsd.connect(host="0.0.0.0", port=2947)
gpsd.GpsResponse.mode = 3

gps = gpsd.get_current()
gps.mode = 3

print(gpsd.device())
print(gpsd.get_current())
print(gps.altitude)


subprocess.run(["/home/pi/gpsscript/uhubctl -a 0 -p 10"], shell=True, stderr=subprocess.STDOUT)

print(subprocess.STDOUT)
























































































































































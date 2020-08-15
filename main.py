import gpsd, subprocess, sys, getopt
from subprocess import PIPE

def main(argv):
    opts, args = getopt.getopt(argv,"d")

    gpsd.connect(host="0.0.0.0", port=2947)
    gpsd.GpsResponse.mode = 3

    gps = gpsd.get_current()
    gps.mode = 3

    print(gpsd.device())
    print(gpsd.get_current())
    print(gps.altitude)

    uhub = subprocess.run(["/home/pi/gpsscript/uhubctl -a 0 -p 10"], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if uhub.stderr == '':
        print("Encoutered error at uhubctl: ", uhub.stderr)
    else:
        if opts[0] in ("-d"):
            print(uhub.stdout)
        print("I function correctly")

if __name__ == "__main__":
   main(sys.argv[1:])























































































































































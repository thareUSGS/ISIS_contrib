import sys
import math

# converted to Python from original C++ code using CoPilot

def main():
    if len(sys.argv) != 3:
        print(f"\nRerun the program and enter the required parameters:\n{sys.argv[0]} center_lat center_lon\n")
        sys.exit(1)

    lat = float(sys.argv[1])
    lon = float(sys.argv[2])

    # Biaxial case for Mars_2000
    a = 3396190.0
    b = 3396190.0
    c = 3376200.0

    PI = 4 * math.atan(1)
    lat = lat * PI / 180  # in radians
    lon = lon * PI / 180  # in radians

    # Get the scaling radius
    xyradius = a * b / math.sqrt((b * math.cos(lon))**2 + (a * math.sin(lon))**2)
    radius = xyradius * c / math.sqrt((c * math.cos(lat))**2 + (xyradius * math.sin(lat))**2)
    print(f"{radius:.8f} = Local Radius")

if __name__ == "__main__":
    main()


import sys
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


args = sys.argv

def map():
    img = Image.open("./resources/image.jpeg")

    exif_data = get_exif_data(img)

    latitude, longitude = get_lat_lon(exif_data)

    print (latitude, longitude)

def get_exif_data(img):
    exif_data = {}
    info = img._getexif()
    if info:
        print(info.items())
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                gps_data = {}
                for t in value:
                    sub_decoded = GPSTAGS.get(t, t)
                    gps_data[sub_decoded] = value[t]

                exif_data[decoded] = gps_data
            else:
                exif_data[decoded] = value
    return exif_data

def get_if_exist(data, key):
    if key in data:
        return data[key]
		
    return None

def convert_to_degress(value):
    d = float(value[0])
    m = float(value[1])
    s = float(value[2])
    return d + (m / 60.0) + (s / 3600.0)

def get_lat_lon(exif_data):
    print(exif_data)
    lat = None
    lon = None

    if "GPSInfo" in exif_data:		
        gps_info = exif_data["GPSInfo"]

        gps_latitude = get_if_exist(gps_info, "GPSLatitude")
        gps_latitude_ref = get_if_exist(gps_info, 'GPSLatitudeRef')
        gps_longitude = get_if_exist(gps_info, 'GPSLongitude')
        gps_longitude_ref = get_if_exist(gps_info, 'GPSLongitudeRef')

        if gps_latitude and gps_latitude_ref and gps_longitude and gps_longitude_ref:
            lat = convert_to_degress(gps_latitude)
            if gps_latitude_ref != "N":                     
                lat = 0 - lat

            lon = convert_to_degress(gps_longitude)
            if gps_longitude_ref != "E":
                lon = 0 - lon

    return lat, lon

def parse_args(args):
    if "--help" in args:
        if args[0] == '--help':
            help()
    elif "-map" in args:
        name_index = args.index("-map") + 1
        if name_index < len(args):
            map()
        else:
            print("./image -map image.jpeg")
    elif "-steg" in args:
        ip_index = args.index("-ip") + 1
        if ip_index < len(args):
            search_by_ip(args[ip_index])
        else:
            print("IP address not provided")
    else:
        print("Unknown command. Use '--help' for guidelines.")

parse_args(sys.argv[1:])

def help():
    print("Welcome to inspector-image\n"
          "OPTIONS:\n"
          " ./image -map   Search by full name like 'python3 passive.py -fn \"Jean Dupont\"'\n"
          "        -ip :     Search with IP address, like 'python3 passive.py -ip 127.0.0.1'\n")


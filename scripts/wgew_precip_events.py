import os
from .convert_coords import utm_to_latlon

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def run():
    print("Importing WGEW precip event data.")
    print("Done!")
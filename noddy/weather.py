""" Get weather data from precipation 

Start date:

1979-1-1

lat 90.0 to -90.0, 0.75

lon 0 to 359.25, 0.75

Year, day, month.
"""
import datetime

START = datetime.date(1979, 1, 1)

DELTA = 0.75

LATITUDE_START = 90.0
LONGITUDE_START = 0.0

def records_per_day():
    """ One record per lat and lon """
    
    return longitudes() * latitudes()

def longitudes():

    return int(360 / DELTA)

def latitudes():

    return int(1 + (180 / DELTA))

def latitude_index(lat):

    return int((LATITUDE_START - lat) / DELTA)

def longitude_index(lon):

    return int((lon - LONGITUDE_START) / DELTA)

def calculate_record_number(date, lat=90, lon=0.0, start=None):
    """  Calculate the record number for given date, lat, lon """
    if start is None:
        start = START

    days = (date - start).days

    lat_index = latitude_index(lat)

    lon_index = longitude_index(lon)

    number = days * records_per_day()
    number += lon_index * latitudes()
    number += lat_index

    return number

def get_data(date, infile, size=9):

    pos = calculate_record_number(date)

    infile.seek(pos * size)

    return infile.read(size * records_per_day())

def get_data_for_pos(lat, lon, infile, size=9):

    pos = calculate_record_number(START, lat, lon)

    infile.seek(pos * size)

    data = ''
    while True:
        record = infile.read(size)

        if not record:
            return data

        data += record

        pos += size * records_per_day()

        infile.seek(pos)
    
        
    

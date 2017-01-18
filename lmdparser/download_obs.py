from urllib2 import urlopen
from .GLMObservation import GLMObservation

def get_latest_observations(station_type='all'):
    """
    Gets the most recent observations from the GLERL CoastWatch website. 
    By default, observations from all station types are downloaded. 
    Alternatively, specify a valid station type.
    :param station_type: Download only obs originating from stations of this type. Default: All stations
    :return A list of GLMObservation objects
    """
    if station_type == 'all':
        url = 'https://coastwatch.glerl.noaa.gov/marobs/today.lmd.txt'
    else:
        station_type_mapping = ['buoy', 'cman', 'coastgaurd', 'ship', 'other', 'surface_stn']
        # exception when not matched?
        station_type_index = station_type_mapping.index(station_type)
        url = "https://coastwatch.glerl.noaa.gov/marobs/php/{}.lmd.txt".format(station_type_index)
    
    web_output = ''
    web_response = urlopen(url)
    web_output = web_response.read()
    obs_strings = web_output.split('\n')

    # Strip out the header lines
    obs_strings = obs_strings[3:]

    # Convert each obs string to a GLMObservation object
    obs_objects = [] 
    for obs_string in obs_strings:
        obs_record = GLMObservation.convert_string(obs_string)
        obs_objects.append(obs_record)

    return obs_objects

def get_observations_for_date(date_str):
    """
    Gets the observations from the GLERL CoastWatch website for the given date 
    string. Observations are available back the past 30 days.
    :param date_str: The date of obs to download. Format: yyyymmdd00
    :return A list of GLMObservation objects
    """
    url = "https://coastwatch.glerl.noaa.gov/marobs/recent/g{}.lmd".format(date_str)

    web_output = ''
    web_response = urlopen(url)
    web_output = web_response.read()
    obs_strings = web_output.split('\n')

    # Strip out the header lines
    obs_strings = obs_strings[3:]

    # Convert each obs string to a GLMObservation object
    obs_objects = [] 
    for obs_string in obs_strings:
        obs_record = GLMObservation.convert_string(obs_string)
        obs_objects.append(obs_record)

    return obs_objects

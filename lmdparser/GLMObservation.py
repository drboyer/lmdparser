import re
from datetime import datetime

lmd_regex = re.compile('(\d{11})(\d{1}|\s)(\w{1,8})\s*(\d{1})?9\s+(.*)')

class GLMObservation:
    """
    Class representing a single Great Lakes Meteorological Observation
    """
    # A few tuples for mapping values
    station_types = ('Buoy', 'CMAN Station', 'USCG Station', 'Ship Report', \
        'OMR Station', 'Surface Synoptic Station', 'Surface Airways Station', \
        'GLERL Met Station')
    lakes = ('Superior', 'Michigan', 'Huron', 'St. Clair', 'Erie', 'Ontario', 'Georgian Bay')
    data_values_order = ('air_temp', 'dewpoint', 'wind_dir', 'wind_speed', \
        'wind_gust', 'cloud_cover', 'solar', 'pressure', 'water_temp', \
        'wave_height', 'wave_period', 'ship_lat', 'ship_lon')

    def __init__(self, obs_date, station_id, **kwargs):
        self.obs_time = datetime.strptime(obs_date, "%Y%j%H%M")
        self.station_id = station_id
        self.station_type = kwargs.get('station_type')
        self.water_body = kwargs.get('water_body')

        # Data fields
        self.air_temp = float(kwargs.get('air_temp', 999.9))
        self.dewpoint = float(kwargs.get('dewpoint', 999.9))
        self.wind_direction = float(kwargs.get('wind_dir', 999))
        self.wind_speed = float(kwargs.get('wind_speed', 99.9))
        self.wind_gust = float(kwargs.get('wind_gust', 99.9))
        self.cloud_cover = float(kwargs.get('cloud_cover', 999))
        self.solar_radiation = float(kwargs.get('solar', 9999.9))
        self.pressure = float(kwargs.get('pressure', 9999.9))
        self.water_temp = float(kwargs.get('water_temp', 99.9))
        self.sig_wave_height = float(kwargs.get('wave_height', 99.9))
        self.wave_period = float(kwargs.get('wave_period', 99.9))
        # Now clean these values!
        self._clean_data_values()
        
        # Ship location:
        # These values will only ever exist for Ship Reports
        self.ship_latitude = kwargs.get('ship_lat')
        self.ship_longitude = kwargs.get('ship_lon')
        if self.ship_latitude != None:
            self.ship_latitude = float(self.ship_latitude)
        
        # Ship longitudes here are decimal degrees West, multiply by -1 to
        # fit convention
        if self.ship_longitude != None:
            self.ship_longitude = float(self.ship_longitude) * -1

    # TODO: This will be the final one
    @classmethod
    def convert_string(cls, lmd_string):
        """
        Converts a string formatted in Lake Meteorological Data format to a
        GLMObservation object.
        """
        rxp_match = lmd_regex.search(lmd_string)
        if rxp_match:
            line_groups = rxp_match.groups()
            data_datetime = datetime.strptime(line_groups[0], '%Y%j%H%M')
            data_values = line_groups[4].split()

            obs_kwargs = {'station_type': GLMObservation._get_station_type(line_groups[1]), \
                'water_body': GLMObservation._get_water_body(line_groups[3])}

            for i in range(0, len(data_values)):
                obs_kwargs[cls.data_values_order[i]] = data_values[i]

            return GLMObservation(line_groups[0], line_groups[2], **obs_kwargs)

    @classmethod
    def convert_string_to_datadict(cls, lmd_string):
        """
        Converts a string formatted in Lake Meteorological Data format to a
        dictionary containing the data.
        """
        rxp_match = lmd_regex.search(lmd_string)
        if rxp_match:
            line_groups = rxp_match.groups()
            data_datetime = datetime.strptime(line_groups[0], '%Y%j%H%M')
            data_values = line_groups[4].split()
            # print(data_values)

            obs_kwargs = {'station_type': GLMObservation._get_station_type(line_groups[1]), \
                'water_body': GLMObservation._get_water_body(line_groups[3])}

            for i in range(0, len(data_values)):
                # print i
                obs_kwargs[cls.data_values_order[i]] = data_values[i]

            return obs_kwargs

    @classmethod
    def _get_station_type(cls, station_type_value):
        '''Maps the station type number to a station type string'''
        # TODO: Make this value None if it's missing in the regular expression?
        if (station_type_value == ' '):
            return None
        else:
            return cls.station_types[int(station_type_value)]

    @classmethod
    def _get_water_body(cls, lake_number_value):
        '''Maps the lake number to a lake/water body name string'''
        if (lake_number_value == None):
            return None
        else:
            return cls.lakes[int(lake_number_value)]

    def _clean_data_values(self):
        '''
        Cleans missing data values in this observation instance, 
        setting missing values to None
        '''
        if self.air_temp == 999.9:
            self.air_temp = None

        if self.dewpoint == 999.9:
            self.dewpoint = None

        if self.wind_direction == 999:
            self.wind_direction = None

        if self.wind_speed == 99.9:
            self.wind_speed = None

        if self.wind_gust == 99.9:
            self.wind_gust = None

        if self.cloud_cover == 999:
            self.cloud_cover = None

        if self.solar_radiation == 9999.9:
            self.solar_radiation = None

        if self.pressure == 9999.9:
            self.pressure = None

        if self.water_temp == 99.9:
            self.water_temp = None

        if self.sig_wave_height == 99.9:
            self.sig_wave_height = None

        if self.wave_period == 99.9:
            self.wave_period = None

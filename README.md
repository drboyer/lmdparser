# lmdparser - Lake Meteorological Data Parser

This a Python module that can be used to parse text files that store data in 
Lake Meteorological Data format. Data stored in this format is weather 
observations from various sources from around the Great Lakes.

This module includes a class `GLMObservation` which has all of the attributes 
contained in a Great Lakes Meteorological Observation. The *download_obs* 
submodule also contains functions which can be used to download LDM datasets
from NOAA and parse them into GLMObservation objects.

This module has no external dependencies. Install via `python setup.py install`.
GLMObservation has unit tests: `python setup.py test`

## Example

Pull the latest observation file and print out the first observation's station
type, air temperature, air pressure and water temperature

```
import lmdparser.download_obs

latest_observations = lmdparser.download_obs.get_latest_observations()

first_obs = latest_observations[0]
print("Obs from {0} {1}, Air Temp: {1}, Pressure {2}, Water Temp: {3}"
    .format(first_obs.station_type, 
            first_obs.station_id,
            first_obs.air_temp,
            first_obs.pressure,
            first_obs.water_temp))
```

## More Reading

* [NOAA GLERL Daily Summary Page](https://coastwatch.glerl.noaa.gov/marobs/marobs.html) - Contains links to the datasets and some visualizations made with GLM observations
* [NOAA GLERL LMD Format Description Document](https://coastwatch.glerl.noaa.gov/marobs/docs/data.lmd.fmt)

## Future Enhancements

* Demos using matplotlib?

Feedbacl/contributions welcome!

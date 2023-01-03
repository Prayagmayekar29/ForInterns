import numpy as np
np.set_printoptions(threshold=np.inf)
#from pyhive import hive
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
from scipy import stats
from geopy.geocoders import Nominatim
from geopy.point import Point
import openpyxl
#import xlrd
from matplotlib import rcParams
import re
import calendar
#from natsort import natsorted
import warnings
warnings.filterwarnings('ignore')
#from pyhive import hive
import reverse_geocoder as rg 
import pprint 
import folium

coordinates=df_ign_off[["gpslatitude","gpslongitude"]]
coordinates.reset_index(drop=True,inplace=True)
coordinates=coordinates.apply(tuple,axis=1)
coordinates=pd.DataFrame(coordinates)
df_ign_off['coordinates']=coordinates


def reverseGeocode(coordinates): 
    result = rg.search(coordinates)
    return (result)
	
	
	
if __name__ == "__main__":
    # Coordinates tuple.Can contain more than one pair.
    coordinates = list(zip(df_tms['Latitude'],df_tms['Longitude']))#generates pairs of lat-long
    data = reverseGeocode(coordinates)
    df_tms['City'] = [i['name']for i in data]
    df_tms['State'] = [i['admin1'] for i in data]
    df_tms['District'] = [i['admin2'] for i in data]


	
from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="geoapiExercises")
locator = Nominatim(user_agent="myGeocoder", timeout=10)
rgeocode = RateLimiter(locator.reverse, min_delay_seconds=0.01)
from geopy.extra.rate_limiter import RateLimiter
import tqdm
from tqdm._tqdm_notebook import tqdm_notebook
from tqdm import tqdm
tqdm.pandas()

df_tms['geom'] = df_tms['Latitude'].map(str) + ',' + df_tms['Longitude'].map(str) 
df_tms["address"] = df_tms["geom"].progress_apply(rgeocode)
df_tms['address'] = df_tms['address'].astype('str')

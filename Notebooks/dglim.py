# Dependencies
import matplotlib
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from enum import Enum

# Globals
default_font_size = 10.0 # matplotlib.rcParams.get('font.size') # Should be 10.0
project_path = './'
datasets_path = project_path + 'Datasets/'
csv_path = project_path + 'Generated Data/'
keys_path = project_path + 'Keys/'

def setProjectPath(path):
    global project_path
    global datasets_path
    global csv_path
    global keys_path
    
    project_path = path
    datasets_path = project_path + 'Datasets/'
    csv_path = project_path + 'Generated Data/'
    keys_path = project_path + 'Keys/'

# Plotting
class Colors:
    orange = u'#1b679d' # Lightened orange
    blue = u'#ffa04d' # Darkened blue
    green = u'#2ca02c' # Green
    red = u'#d62728' # Red
    purple = u'#9467bd' # Purple
    brown = u'#8c564b' # Brown
    pink = u'#e377c2' # Pink
    gray = u'#7f7f7f' # Gray
    yellow = u'#bcbd22' # Yellow
    turquoise = u'#17becf' # Turquoise

def usePlotStyle():
    matplotlib.style.use('default')
    plt.rcParams.update({
        'figure.figsize': (20, 10),
        'font.size': 20,
        'xtick.labelsize': 18,
        'ytick.labelsize': 18,
        'axes.prop_cycle': plt.cycler(
            color=[
                Colors.orange,
                Colors.blue,
                Colors.green,
                Colors.red,
                Colors.purple,
                Colors.brown,
                Colors.pink,
                Colors.gray,
                Colors.yellow,
                Colors.turquoise
            ])
        })
    
# Files
def saveData(df, file_name):
    file_path = csv_path + file_name
    df.to_csv(file_path + '.csv', encoding='utf-8')
    df.to_pickle(file_path + '.pkl')

def loadData(file_name):
    file_path = csv_path + file_name
    return pd.read_pickle(file_path + '.pkl')

# Hide keys in unsynced files
def getGoogleAPIKey():
    f = open(keys_path + 'Google API Key')
    google_key = f.readline()
    f.close()
    return google_key

# Data
def getNAICSBusinessType(business_type):
    temp_series = naics_bus_types['NAICS Business Type'][naics_bus_types['Business types'] == business_type]
    if len(temp_series):
        return temp_series.iloc[0]
    else:
        return "Not found"

# City geographies
class City:
    latitude = 29.651961
    longitude = -82.325002

class Region(Enum):
    NE = 0
    SE = 1
    SW = 2
    NW = 3

def getRegion(lat, lng):
    try:
        # REGION POSSIBLE VALUES
        if(lat > City.latitude):
            if(lng < City.longitude):
                return Region.NW
            else:
                return Region.NE
        else:
            if(lng < City.longitude):
                return Region.SW
            else:
                return Region.SE
        return np.nan
    except(TypeError):
        pass

def getRowRegion(row):
    lat = float(row['Latitude'])
    lng = float(row['Longitude'])
    return getRegion(lat, lng)

# Geometries
import shapely
from shapely.wkt import dumps, loads

def getGainesvilleShape():
    f = open("../Geometries/gainesville_shape", "r")
    gainesville_shape = loads(f.read())
    f.close()
    return gainesville_shape

def getTractShapes(gainesville_shape):
    f = open("../Geometries/tract_shapes", "r")
    lines = f.readlines();
    f.close();

    num_fields = 4
    tract_shapes = {}
    for tract_index in range(len(lines)/num_fields):
        i = tract_index * num_fields
        tract = {}
        tract['GEOID'] = lines[i][:-1] # Remove the newline character at the end
        tract['Name'] = lines[i + 1][:-1]
        tract['Fraction'] = float(lines[i + 2][:-1])
        tract['Shape'] = loads(lines[i + 3][:-1])
        tract_shapes[tract['Name']] = tract
    return tract_shapes

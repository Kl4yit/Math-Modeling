import json
from plotter import Plotter
DATA_FILE_PATH = './data.json'


@Plotter
def get_data():
    with open(DATA_FILE_PATH, 'r') as f:
        data = json.load(f)
    return data

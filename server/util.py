import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None


def predict_price(total_sqft, bhk, balcony, bath, location):
    x = np.zeros(len(__data_columns))
    x[-1] = balcony
    x[-2] = bath
    x[-4] = bhk
    if total_sqft:
        x[-3] = total_sqft
    else:
        x[-3] = 1200


    try:
        loc_ind = __data_columns.index(location)
    except:
        loc_ind = -1

    if loc_ind >= 0:
        x[loc_ind] = 1

    return round(__model.predict([x])[0], 2)

def load_saved_artifacts():
    print('Loading Artifacts')
    global __locations
    global __data_columns
    global __model

    with open('../model/columns.json', 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[:-4]

    if __model is None:
        with open('../model/bengaluru_house_pred_model.pickle', 'rb') as f:
            __model = pickle.load(f)

    print('Done Loading Artifacts')


def get_locations():
    load_saved_artifacts()
    return __locations

def get_data_columns():
    load_saved_artifacts()
    return __data_columns

load_saved_artifacts()


# if __name__ == '__main__':
    # print(get_locations())

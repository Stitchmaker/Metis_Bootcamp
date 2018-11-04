import numpy as np
import pickle

pipeline = pickle.load(open('./model/Seatac_model.pkl', 'rb'))

example = {'Airline': 'AA',
      'MONTH': 7,
      'DAY_OF_WEEK': 5,
      'CRS_ARR_TIME': 1100,
      'CRS_FLIGHT_TIME': 200,
      'DISTANCE': 1000, 
      'SEA_SNOW': 0, 
      'SEA_TAVG': 70,
      'SEA_AWND': 0, 
      'ORD_SNOW': 0, 
      'ORD_TAVG': 70, 
      'ORD_AWND': 0, 
      'JFK_SNOW': 0, 
      'JFK_TAVG': 70,
      'JFK_AWND': 0
}

def make_prediction(features):
    features['OP_UNIQUE_CARRIER_AA'] = 0
    features['OP_UNIQUE_CARRIER_AS'] = 0
    features['OP_UNIQUE_CARRIER_B6'] = 0
    features['OP_UNIQUE_CARRIER_DL'] = 0
    features['OP_UNIQUE_CARRIER_F9'] = 0
    features['OP_UNIQUE_CARRIER_G4'] = 0
    features['OP_UNIQUE_CARRIER_HA'] = 0
    features['OP_UNIQUE_CARRIER_HK'] = 0
    features['OP_UNIQUE_CARRIER_OO'] = 0
    features['OP_UNIQUE_CARRIER_UA'] = 0
    features['OP_UNIQUE_CARRIER_VX'] = 0
    features['OP_UNIQUE_CARRIER_WN'] = 0

    features['OP_UNIQUE_CARRIER_'+features['Airline']] = 1
    features.pop('Airline', None)
    
    print(features)

    X = np.array([features['OP_UNIQUE_CARRIER_AA'],
       features['OP_UNIQUE_CARRIER_AS'],
       features['OP_UNIQUE_CARRIER_B6'],
       features['OP_UNIQUE_CARRIER_DL'],
       features['OP_UNIQUE_CARRIER_F9'],
       features['OP_UNIQUE_CARRIER_G4'],
       features['OP_UNIQUE_CARRIER_HA'],
       features['OP_UNIQUE_CARRIER_HK'],
       features['OP_UNIQUE_CARRIER_OO'],
       features['OP_UNIQUE_CARRIER_UA'],
       features['OP_UNIQUE_CARRIER_VX'],
       features['OP_UNIQUE_CARRIER_WN'],
       features['MONTH'],
       features['DAY_OF_WEEK'],
       features['CRS_ARR_TIME'],
       features['CRS_FLIGHT_TIME'],
       features['DISTANCE'], 
       features['SEA_SNOW'], 
       features['SEA_TAVG'],
       features['SEA_AWND'], 
       features['ORD_SNOW'], 
       features['ORD_TAVG'], 
       features['ORD_AWND'], 
       features['JFK_SNOW'], 
       features['JFK_TAVG'],
       features['JFK_AWND']]).reshape(1,-1)

    # This X should give probability of 0.572 with prediction 1 for Delay
    #X = np.array([-0.26761865, -0.78077626, -0.11515749, -0.42431955, -0.08438764,  0., \
    #     -0.06945212, -0.10599023, -0.42647294, -0.2752299,   7.94753871, -0.37951458,\
    #     -0.4724069,  -0.47445657,  0.98799467, -0.13575537, -0.38044794, -0.08644293,\
    #     0.21095946, -0.7189438,  -0.12632908,  0.10205602,  1.1529054,  -0.11560818,\
    #     0.25133512, -0.53186869]).reshape(1,-1)
    #print(X)
    
    prob_delay = pipeline.predict_proba(X)[0, 1]

    result = {
        'prediction': int(prob_delay > 0.5),
        'prob_delay': prob_delay
    }
    return result

if __name__ == '__main__':
    print(make_prediction(example))
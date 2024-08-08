import pickle

def load_model():
    #load the model from models directory
    with open('../models/model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model


def load_encoder():
    #load the encoder from models directory
    with open('../models/ohe.pkl', 'rb') as file:
        one_hot_encoder = pickle.load(file)
    return one_hot_encoder
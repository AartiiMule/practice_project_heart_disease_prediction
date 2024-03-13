import numpy as np
import pandas as pd
import pickle
import json
import warnings
warnings.filterwarnings("ignore")
import config
class Heart():
    def __init__(self,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):

        self.age = age
        self.sex = sex
        self.cp = cp
        self.trestbps = trestbps 
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.age = thalach
        self.sex = sex
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal
    
    def load_models(self):
        with open(config.MODEL_FILE_PATH,"rb") as file:
            self.logistic_model=pickle.load(file)

        with open(config.JSON_FILE_PATH,"r") as file:
            self.json_data=json.load(file)     

    def get_predicted_value(self):
        self.load_models()  
        test_array=np.zeros(len(self.json_data["columns"]))

        test_array[0] = self.age
        test_array[1] = self.sex
        test_array[2] = self.cp
        test_array[3] = self.trestbps
        test_array[4] = self.chol
        test_array[5] = self.fbs
        test_array[6] = self.restecg
        test_array[7] = self.thalach
        test_array[8] = self.exang
        test_array[9] = self.oldpeak
        test_array[10] = self.slope
        test_array[11] = self.ca
        test_array[12] = self.thal

        charges =  self.logistic_model.predict([test_array])
        return charges

if __name__== "__main__":
    age = 63.0
    sex = 1.0
    cp = 3.0
    trestbps = 145.0
    chol = 233.0
    fbs = 1.0
    restecg = 0.0
    thalach = 150.0
    exang = 0.0
    oldpeak = 2.3
    slope = 0.0
    ca = 0.0
    thal = 1.0



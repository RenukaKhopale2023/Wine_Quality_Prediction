import pickle
import json
import config
import numpy as np
import pandas as pd


class Redwinequality():

    def __init__(self,fixed_acidity,volatile_acidity,
                                          citric_acid,residual_sugar,
                                         chlorides,free_sulfur_dioxide, 
                                         total_sulfur_dioxide,density,
                                         pH,sulphates,alcohol) :
        self.fixed_acidity=fixed_acidity
        self.volatile_acidity=volatile_acidity
        self.citric_acid= citric_acid
        self.residual_sugar=residual_sugar
        self.chlorides= chlorides
        self.free_sulfur_dioxide= free_sulfur_dioxide
        self.total_sulfur_dioxide= total_sulfur_dioxide
        self.density= density
        self.pH=pH 
        self.sulphates= sulphates
        self.alcohol=alcohol 

    def __load_model(self): 
        with open(r'artifacts/labelencoder_y.pkl','rb') as f:
            self.model = pickle.load(f)
            
        with open(r'artifacts/std_scaler.pkl','rb') as f:
            self.model = pickle.load(f)

        with open(r'artifacts/regression_model.pkl','rb') as f:
            self.model = pickle.load(f)


        with open(r'artifacts/knn_model.pkl','rb') as f:
            self.model = pickle.load(f)


        with open(r'artifacts/project_data.json','r') as f:
            self.project_data = json.load( f)
            # print("Project Data :",self.project_data)
             
    def get_predict_quality(self): # Public Method
        self.__load_model()
        test_array = np.zeros((1,self.model.n_features_in_))
        
        test_array[0][0] = self.fixed_acidity
        test_array[0][1] = self.volatile_acidity
        test_array[0][2] = self. citric_acid
        test_array[0][3] = self.residual_sugar
        test_array[0][4] = self.chlorides
        test_array[0][5] = self.free_sulfur_dioxide
        test_array[0][6] = self.total_sulfur_dioxide
        test_array[0][7] = self.density
        test_array[0][8] = self.pH
        test_array[0][9] = self.sulphates
        test_array[0][10] = self.alcohol

        # print("Test Array is :",test_array)
        # scaler_test_array = self.scaler.fit_transform(array)  
        # test_dataset = pd.DataFrame(scaler_test_array,columns=self.model.feature_names_in_)


        predict_quality= np.around(self.model.predict(test_array)[0],3)
        print("Predicted quality :", predict_quality)
        return predict_quality

if __name__ == '__main__':
    cls = Redwinequality(1.2,12.23,12.32,23.11,65.1,67.6,12.43,45.98,12.89,76.90,23.6)
    # prediction = cls.get_predict_quality()
    # print(prediction)
    print(cls.get_predict_quality())
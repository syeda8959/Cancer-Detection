from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
import pickle
import numpy as np
import pandas as pd

import csv


@api_view(['GET'])
def setup(request):
    return HttpResponse('setup')


@api_view(['POST'])
def predict(request):
    
    model = pickle.load(open("../model/breast_model.pkl", "rb"))
    scaler = pickle.load(open("../model/breast_scaler.pkl", "rb"))
    enc = pickle.load(open("../model/breast_enc.pkl", "rb"))
    
    _dict = request.data
    value = list(request.data.values())
    data = {'age': [value[0]],
            'menopause': [value[1]],
            'tumor-size': [value[2]],
            'inv-nodes': [value[3]],
            'node-caps': [value[4]],
            'deg-malig': [value[5]],
            'breast': [value[6]],
            'breast-quad': [value[7]],
            'irradiat': [value[8]],
            } 
    df = pd.DataFrame.from_dict(data)

    #numpyArray = np.array([my_list])

    #df['age'] = enc.fit_transform(df['age'])
    #df['menopause'] = enc.fit_transform(df['menopause'])
    #df['inv-nodes'] = enc.fit_transform(df['inv-nodes'])
    #df['Class'] = enc.fit_transform(df['Class'])
    #df['tumor-size'] = enc.fit_transform(df['tumor-size'])
    df['age'] = df['age'].map({'40-49': 2, '50-59': 3})
    df['menopause'] = df['menopause'].map({'premeno': 2, 'ge40': 0})
    df['tumor-size'] = df['tumor-size'].map({'15-19': 2, '35-39': 6, '30-34': 5})
    df['inv-nodes'] = df['inv-nodes'].map({'0-2': 0, '3-5': 4})

    print(df)
    X_test_scaled = scaler.transform(df)
    prediction = model.predict(X_test_scaled)
    
    dd = df.to_dict(orient='dict')
    if int(dd['age'][0]) == 2:
        prediction = 1
    
    if prediction == 1:
        return HttpResponse('Indicates positive')
    else: 
        return HttpResponse('Indicates negative')


@api_view(['POST'])
def predict_cervical_cancer(request):
    
    model = pickle.load(open("../model/cervical_model.pkl", "rb"))
    scaler = pickle.load(open("../model/cervical_scaler.pkl", "rb"))

    my_list = list(request.data.values())
    numpyArray = np.array([my_list])

    X_test_scaled = scaler.transform(numpyArray)
    
    prediction = model.predict(X_test_scaled)
    print(numpyArray,X_test_scaled,prediction)
    if prediction == 1:
        return HttpResponse('Biopsy test needed')
    else:
        return HttpResponse('Biopsy test not needed')


@api_view(['POST'])
def book_doctor(request):
    f = open('../data/doctor_book.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(list(request.data.values()))
    f.close()
    return HttpResponse("Doctor's apointment Booked!")


@api_view(['POST'])
def book_hospital(request):
    f = open('../data/hospital_book.csv', 'a')
    writer = csv.writer(f)
    print(list(request.data.values()))
    writer.writerow(list(request.data.values()))
    f.close()
    return HttpResponse("Hospital's booking confirmed!")


@api_view(['POST'])
def contact(request):
    f = open('../data/contact_us.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(list(request.data.values()))
    f.close()
    return HttpResponse('Entry Successful, We will reach you shortly!')
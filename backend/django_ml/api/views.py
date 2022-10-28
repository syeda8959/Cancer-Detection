from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
import pickle
import numpy as np

import csv


@api_view(['GET'])
def setup(request):
    return HttpResponse('setup')


@api_view(['POST'])
def predict(request):
    
    model = pickle.load(open("/home/jawad/Documents/Cancer-Detection/backend/model/ml_model.sav", "rb"))
    
    my_list = list(request.data.values())
    numpyArray = np.array([my_list])
    prediction = model.predict(numpyArray)
    print(numpyArray,prediction)
    if prediction == 1:
        return HttpResponse('recurrence-events')
    else: 
        return HttpResponse('no-recurrence-events')


@api_view(['POST'])
def predict_cervical_cancer(request):
    
    model = pickle.load(open("/home/jawad/Documents/Cancer-Detection/backend/model/cervical_model.pkl", "rb"))
    scaler = pickle.load(open("/home/jawad/Documents/Cancer-Detection/backend/model/cervical_scaler.pkl", "rb"))

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
    return HttpResponse('Doctor'+'s apointment Booked!')


@api_view(['POST'])
def book_hospital(request):
    f = open('../data/hospital_book.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(list(request.data.values()))
    f.close()
    return HttpResponse('Hospital'+'s booking confirmed!')


@api_view(['POST'])
def contact(request):
    f = open('../data/contact_us.csv', 'a')
    writer = csv.writer(f)
    writer.writerow(list(request.data.values()))
    f.close()
    return HttpResponse('Entry Successful, We will reach you shortly!')
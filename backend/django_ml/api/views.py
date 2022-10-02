from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
import pickle
import numpy as np

@api_view(['GET'])
def setup(request):
    return HttpResponse('setup')


@api_view(['POST'])
def predict(request):
    print(type(request.data))
    model = pickle.load(open("/home/jawad/Documents/django-ml/ml_model.sav", "rb"))
    
    my_list = list(request.data.values())
    numpyArray = np.array([my_list])
    prediction = model.predict(numpyArray)
    if prediction == 1:
        return HttpResponse('recurrence-events')
    else: 
        return HttpResponse('no-recurrence-events')

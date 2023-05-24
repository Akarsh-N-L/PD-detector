from django.shortcuts import render
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm

input=[]

def home(request):
    return render(request,'home.html')

def result(request):
    freqArr=[]
    freqs = request.GET["input"]
    # print(type(freqs))
    freqArr = freqs.split("%2C")
    freqArr = freqArr[0].split(",")
    print(freqArr)
    for i in range(len(freqArr)):
        input.append(float(freqArr[i]))
    print("input=")
    print(input)
    print("End")
    return render(request,'result.html', {'freqs':freqs})
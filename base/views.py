from django.shortcuts import render,redirect
import numpy as np
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from django.core.mail import send_mail

diseaseStatus = False
isDetected = False

def home(request):
    return render(request,'home.html')

def diseasePredictor(input_data):
    parkinsons_data = pd.read_csv('parkinsons data set.csv')
    x=parkinsons_data.drop(columns=['name','status'],axis=1)
    y=parkinsons_data['status']
    X_train,X_test,Y_train,Y_test=train_test_split(x,y,test_size=0.2,random_state=2)
    scalar = StandardScaler()
    scalar.fit(X_train)
    X_train = scalar.transform(X_train)
    X_test = scalar.transform(X_test)
    model = svm.SVC(kernel='linear')
    model.fit(X_train,Y_train)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    std_data = scalar.transform(input_data_reshaped)
    prediction = model.predict(std_data)
    if prediction[0] == 1:
        return 1
    return 0


def result(request):
    input=[]
    freqArr=[]
    freqs = request.GET["input"]
    freqArr = freqs.split("%2C")
    freqArr = freqArr[0].split(",")
    print(freqArr)
    for i in range(len(freqArr)):
        input.append(float(freqArr[i]))
    print(input)
    ans = diseasePredictor(input)
    isDetected = True
    if ans==1:
        ans = "1"
        diseaseStatus= True
    else:
        ans = "0"
        diseaseStatus=False
    return render(request,'result.html', {'ans':ans})


def appointment(request):
    return render(request,'appointment.html')


def sendMail(request):
    name = request.GET["name-inp-apt"]
    email = request.GET["email-inp-apt"]
    phone = request.GET["phone-inp-apt"]
    date1 = request.GET["date-inp-1"]
    date2 = request.GET["date-inp-2"]
    time1 = request.GET["time-inp-1"]
    time2 = request.GET["time-inp-2"]
    if isDetected:
        if diseaseStatus:
            isAffected = "PD Positive"
        else:
            isAffected = "PD Positive"
    else:
        isAffected = "Not yet detected or Not tested"
    subject = "Parkinson's Disease Predictor"
    message = "Patient Name: "+ name + "\nEmail: "+email+"\nPhone Number: "+phone+"\nTime and Date-1: "+time1+" "+date1+"\nTime and Date-2: "+time2+" "+date2
    from_mail = "akarshnl21@gmail.com"
    to_mail = ["ghsaishreyas3@gmail.com","akarshnl17@gmail.com"]
    send_mail(subject,message,from_mail,to_mail, fail_silently=False)
    return redirect('home')
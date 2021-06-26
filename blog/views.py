from time import time
from django.shortcuts import render
from django.http import HttpResponse
import pyrebase
from django.contrib import auth
from firebase_admin import credentials, firestore
config = {
     'apiKey': "AIzaSyAtz2cuDcPHqAuQeWRzwTLhhWTZq_I1_XU",
    'authDomain': "hackathon-e6a4d.firebaseapp.com",
    'databaseURL': "https://hackathon-e6a4d-default-rtdb.firebaseio.com",
    'projectId': "hackathon-e6a4d",
    'storageBucket': "hackathon-e6a4d.appspot.com",
    'messagingSenderId': "147102212882",
    'appId': "1:147102212882:web:668f67aabeda976e5049cb",
    'measurementId': "G-TG8Z8SM65D"
}
firebase =pyrebase.initialize_app(config)
authe= firebase.auth()
database=firebase.database()

def index(request):
    return render(request,'index.html')

def singIN(request):
    return render(request,'signin.html')
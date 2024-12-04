from django.shortcuts import render, redirect

# Create your views here.
# recommendations/views.py
from recommendations.models import ClientRegister_Model
from .forms import RecommendationForm
import pickle
import pandas as pd
from django.contrib import messages
from .models import ClientRegister_Model
import re
import string
from django.db.models import Count
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
import datetime
import openpyxl

def index(request):
    return render(request,'RUser/design.html')

def login(request):


    if request.method == "POST" and 'submit1' in request.POST:

        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            enter = ClientRegister_Model.objects.get(username=username,password=password)
            request.session["userid"] = enter.id

            return redirect('ViewYourProfile')
        except:
            pass

    return render(request,'RUser/result.html')
def Register1(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phoneno = request.POST.get('phoneno')
        country = request.POST.get('country')
        state = request.POST.get('state')
        city = request.POST.get('city')
        ClientRegister_Model.objects.create(username=username, email=email, password=password, phoneno=phoneno,
                                            country=country, state=state, city=city)
        messages.success(request, "Registration completed successfully. You can login now.")
        return redirect('Register1')  # Redirect to the same page to show the message
    else:
        return render(request, 'RUser/Register1.html')

def ViewYourProfile(request):
    userid = request.session['userid']
    obj = ClientRegister_Model.objects.get(id= userid)
    return render(request,'RUser/ViewYourProfile.html',{'object':obj})

# Load the model components
with open('movie_recommender.pkl', 'rb') as f:
    model = pickle.load(f)

cv = model['cv']
similarity = model['similarity']
new_df = model['new_df']

def recommend_movie(movie):
    movie_index = new_df[new_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = [new_df.iloc[i[0]].title for i in movies_list]
    return recommended_movies

def recommend(request):
    if request.method == 'POST':
        form = RecommendationForm(request.POST)
        if form.is_valid():
            movie_name = form.cleaned_data['movie_name']
            recommendations = recommend_movie(movie_name)
            return render(request, 'RUser/result.html', {'recommendations': recommendations, 'movie_name': movie_name})
    else:
        form = RecommendationForm()

    return render(request, 'RUser/recommend.html', {'form': form})


from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import DiabeticsForm,BreastForm,HeartForm
from .ml_model import logic_layer,logic_layer2,logic_layer3
from django.contrib import messages
import numpy as np
# Create your views here.
res = None

def index(request):
    return render(request=request, 
                  template_name='main/index1.html')

def predict(request):
    return render(request=request, 
                  template_name='main/predict.html', context={"patient": res})


def index2(request):
    if request.method == 'POST':
        form = DiabeticsForm(request.POST)
        
        if form.is_valid():

            Pregnancies = form.cleaned_data['Pregnancies']
            Glucose = form.cleaned_data['Glucose']
            BloodPressure = form.cleaned_data['BloodPressure']
            SkinThickness = form.cleaned_data['SkinThickness']
            Insulin = form.cleaned_data['Insulin']
            BMI  = form.cleaned_data['BMI']
            DiabetesPedigreeFunction  = form.cleaned_data['DiabetesPedigreeFunction']
            Age  = form.cleaned_data['Age']

            
            x = [ Pregnancies,Glucose,  BloodPressure, SkinThickness, Insulin, BMI , DiabetesPedigreeFunction,Age]

            df=np.array(x).reshape(1,8)

            global res
            predictions = logic_layer(df)
            if int(predictions[0]) == 1:
                 res = 'have Diabetics'
            elif int(predictions[0]) == 0:
                res = "don't have Diabetics"
            return redirect("/predict")
        else:
            problem = form.errors.as_data()
            # This section is used to handle invalid data 
            messages.error(request, list(list(problem.values())[0][0])[0])
            form = DiabeticsForm()
    form = DiabeticsForm()
    return render(request=request, template_name='main/index2.html', context={"form": form})

def index3(request):
    if request.method == 'POST':
        form = BreastForm(request.POST)
        
        if form.is_valid():

            mean_radius = form.cleaned_data['mean_radius']
            mean_texture = form.cleaned_data['mean_texture']
            mean_perimeter = form.cleaned_data['mean_perimeter']
            mean_area = form.cleaned_data['mean_area']
            mean_smoothness = form.cleaned_data['mean_smoothness']
            

            
            x = [mean_radius,mean_texture, mean_perimeter,mean_area ,mean_smoothness]

            df=np.array(x).reshape(1,5)

            global res
            predictions = logic_layer2(df)
            if int(predictions[0]) == 1:
                 res = 'have Breast Cancer'
            elif int(predictions[0]) == 0:
                res = "don't have Breast Cancer"
            return redirect("/predict")
        else:
            problem = form.errors.as_data()
            # This section is used to handle invalid data 
            messages.error(request, list(list(problem.values())[0][0])[0])
            form = BreastForm()
    form = BreastForm()
    return render(request=request, template_name='main/index2.html', context={"form": form})


def index4(request):
    if request.method == 'POST':
        form = HeartForm(request.POST)
        
        if form.is_valid():

            Age = form.cleaned_data['Age']
            sex = int(form.cleaned_data['sex'])
            cp = int(form.cleaned_data['cp'])
            trestbps = form.cleaned_data['trestbps']
            chol = form.cleaned_data['chol']
            fbs =int(form.cleaned_data['fbs'])
            restecg = int(form.cleaned_data['restecg'])
            thalach = form.cleaned_data['thalach']
            exang = int(form.cleaned_data['exang'])
            oldpeak  = form.cleaned_data['oldpeak']
            slope = int(form.cleaned_data['slope'])
            ca  = int(form.cleaned_data['ca'])
            thal = int(form.cleaned_data['thal'])
            

            
            x = [Age,sex, cp,trestbps,chol,fbs,restecg,thalach,exang, oldpeak,slope,ca,thal]

            df=np.array(x).reshape(1,13)

            global res
            predictions = logic_layer3(df)
            if int(predictions[0]) == 1:
                 res = 'have Heart disease'
            elif int(predictions[0]) == 0:
                res = "don't have Heart disease"
            return redirect("/predict")
        else:
            problem = form.errors.as_data()
            # This section is used to handle invalid data 
            messages.error(request, list(list(problem.values())[0][0])[0])
            form = HeartForm()
    form = HeartForm()
    return render(request=request, template_name='main/index2.html', context={"form": form})


def about(request):
    return render(request=request, 
            template_name="main/about.html")



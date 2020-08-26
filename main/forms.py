from django import forms
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator


class DiabeticsForm(forms.Form):
    Pregnancies = forms.IntegerField(label="amount of pregnancies(eg.0-20)", 
                              validators=[MinValueValidator(0, message="input is invalid!"), 
                              MaxValueValidator(20, message="Please provide values less than 20")],)
    Glucose = forms.IntegerField(label="amount of Glucose level(eg.0-500)", 
                              validators=[MinValueValidator(0, message="input is invalid!"), 
                              MaxValueValidator(500, message="Please provide values less than 500")],)
    BloodPressure = forms.IntegerField(label="amount of BloodPressure(eg.0-100)", 
                              validators=[MinValueValidator(0, message="input is invalid!"), 
                              MaxValueValidator(100, message="Please provide values less than 100")],)
    SkinThickness = forms.IntegerField(label="amount of SkinThickness(eg.0-100)", 
                              validators=[MinValueValidator(0, message="input is invalid!"), 
                              MaxValueValidator(100, message="Please provide values less than 100")],)
    Insulin = forms.IntegerField(label="Insulin level(eg.0-500)", 
                              validators=[MinValueValidator(0, message="input is invalid!"), 
                              MaxValueValidator(500, message="Please provide values less than 500")],)
                        
    BMI = forms.FloatField(label="BMI value(eg.0-50)", 
                              validators=[MinValueValidator(0, message="input is invalid!"), 
                              MaxValueValidator(50, message="Please provide values less than 50")],)
    DiabetesPedigreeFunction = forms.FloatField(label="DiabetesPedigreeFunction(eg.0,0.1,1.2)", 
                              validators=[MinValueValidator(0, message="input is invalid!"), 
                              MaxValueValidator(2, message="Please provide decimal values less than 2")],)
                  
    Age = forms.IntegerField(label="Age(eg.1-120)", 
                              validators=[MinValueValidator(1, message="input is invalid!"), 
                              MaxValueValidator(120, message="Please provide values less than 120")],)
                                    




class BreastForm(forms.Form):
    mean_radius = forms.FloatField(label="mean_radius value(eg.0-30)", 
                              validators=[MinValueValidator(0, message="input is invalid!"), 
                              MaxValueValidator(30, message="Please provide values less than 30")],)

    mean_texture = forms.FloatField(label="mean_texture value(eg.0-50)", 
                              validators=[MinValueValidator(0, message="input is invalid!"), 
                              MaxValueValidator(50, message="Please provide values less than 50")],)
    
    mean_perimeter = forms.FloatField(label="mean_perimeter value(eg.0-200)", 
                              validators=[MinValueValidator(0, message="input is invalid!"), 
                              MaxValueValidator(200, message="Please provide values less than 50")],)

    mean_area = forms.FloatField(label="mean_area value(eg.0-2000)", 
                              validators=[MinValueValidator(0, message="input is invalid!"), 
                              MaxValueValidator(2000, message="Please provide values less than 2000")],)

    mean_smoothness = forms.FloatField(label="mean_smoothness value(eg.0.01-0.2)", 
                              validators=[MinValueValidator(0, message="input is invalid!"), 
                              MaxValueValidator(0.2, message="Please provide values less than 0.2")],)

Sex_CHOICES = [
    ('0', 'Female'),
    ('1', 'Male')
]
fbs_CHOICES = [
    ('0','Select fbs'),
    ('0', '0'),
    ('1', '1')
]
restecg_CHOICES=[
    ('0','Select restecg'),
    ('0', '0'),
    ('1', '1')
]
exang_CHOICES=[
    ('0','Select exang'),
    ('0', '0'),
    ('1', '1')
]
slope_CHOICES = [
    ('0', 'Select slope'),
    ('0', '0'),
    ('1', '1'),
    ('2', '2')
]
ca_CHOICES = [
    ('0', 'Select ca'),
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3')
]
thal_CHOICES = [
    ('0', 'select thal'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3')
]

class HeartForm(forms.Form):
    Age = forms.IntegerField(label="Age(eg.1-120)", 
                              validators=[MinValueValidator(1, message="input is invalid!"), 
                              MaxValueValidator(120, message="Please provide values less than 120")],)
    
    #sex = forms.CharField(label="Sex", widget=forms.Select(choices=Sex_CHOICES))

    #cp = forms.CharField(label="cp", widget=forms.Select(choices=ca_CHOICES))

    trestbps = forms.IntegerField(label="trestbps(eg.100-200)", 
                              validators=[MinValueValidator(100, message="Please provide values greater than 100"), 
                              MaxValueValidator(200, message="Please provide values less than 200")],)
    chol = forms.IntegerField(label="chol(eg.100-700)", 
                              validators=[MinValueValidator(100, message="Please provide values greater than 100"), 
                              MaxValueValidator(700, message="Please provide values less than 700")],)

    #fbs = forms.CharField(label="fbs", widget=forms.Select(choices=fbs_CHOICES))

    #restecg = forms.CharField(label="restecg", widget=forms.Select(choices=restecg_CHOICES))

    thalach = forms.IntegerField(label="thalach(eg.50-200)", 
                              validators=[MinValueValidator(50, message="Please provide values greater than 100"), 
                              MaxValueValidator(200, message="Please provide values less than 200")],)

  #  exang = forms.CharField(label="exang", widget=forms.Select(choices=exang_CHOICES))

    oldpeak = forms.FloatField(label="oldpeak(eg.0-5)", 
                              validators=[MinValueValidator(0, message="input is invalid!"), 
                              MaxValueValidator(5, message="Please provide values less than 5")],)
    
    sex = forms.CharField(label="Sex", widget=forms.Select(choices=Sex_CHOICES))

    cp = forms.CharField(label="cp", widget=forms.Select(choices=ca_CHOICES))

    
    fbs = forms.CharField(label="fbs", widget=forms.Select(choices=fbs_CHOICES))

    restecg = forms.CharField(label="restecg", widget=forms.Select(choices=restecg_CHOICES))

    exang = forms.CharField(label="exang", widget=forms.Select(choices=exang_CHOICES))

    slope = forms.CharField(label="slope", widget=forms.Select(choices=slope_CHOICES))

    ca = forms.CharField(label="ca", widget=forms.Select(choices=ca_CHOICES))

    thal = forms.CharField(label="thal", widget=forms.Select(choices=thal_CHOICES))
                  
    

                          
    

                                  
             

from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def toLogin(request):
    return redirect('login/')
def loginPage(request):
    formSI = MemberSignInForm()
    formSU = MemberSignUpForm()
    errSignIn = request.GET.get('errSignIn')
    errSignUp = request.GET.get('errSignUp')
    if errSignIn == None : 
        errSignIn = ''
    else :
        errSignIn = ' \ Une erreur s \' est produite lors de l\'enregistrement '
    if errSignUp == None : 
        errSignUp = ''
    else : 
        errSignUp = ' \ Email ou mot de passe invalide '
    return render(request, 'login.html', {
        'formSI':formSI, 
        'formSU':formSU,
        'errSignIn' : errSignIn,
        'errSignUp' : errSignUp
        })

def signIn(request):
    form = MemberSignInForm(request.POST)
    username = request.POST['name']
    if form.is_valid() and not Member.objects.filter(email = request.POST['email']).exists():
        form.save()
        return redirect('/'+username)
    else : 
        return redirect('/login/?errSignIn=Err')
    
def signUp(request):
    userMail = request.POST['email']
    password = request.POST['password']
    if Member.objects.filter(email=userMail).exists():
        user = Member.objects.filter(email=userMail).get()
        if password == user.password : 
            return redirect('/'+user.name)  
        else : 
            return redirect('/login/?errSignUp=Err')
    else : 
        return redirect('/login/?errSignUp=Err')

def home(request, username):
    return render(request, 'Home.html')
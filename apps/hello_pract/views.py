from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt


# Create your views here.
def index(request):
    if not 'count' in request.session:
        request.session['count'] = 0
        print 'yay'
    context = {
          'user':User.objects.get(id=request.session['user_id']),
          'message':'registered'
        }


    return render(request, 'hello_pract/index.html',context)
def main(request):
   return render(request, 'hello_pract/main.html')

def profile(request,id):
    context = {
      'company':User.objects.get(id=id).company
    }
    return render(request,'hello_pract/profile.html',context)
def user_score(request):
    if request.method == 'POST':
        print 'ok'
    score = request.POST.get("choice")
    score1 = request.POST.get("choice1")
    score2 = request.POST.get("choice2")
    score3 = request.POST.get("choice3")
    print 'the score'
    print score
    print score1
    print score2
    print score3
    count = 0
    if score == 'Yes':
         count+=1
    if score1 == 'Yes':
        count+=1
    if score2 == 'Yes':
        count+=1
    if score3 == 'Yes':
        count+=1
    request.session['count'] = count
    rate = request.session['count']
    context = {
     'rating':rate
    }


    messages.success(request,"Successful submission and your score is "+str(rate))
    return render(request,'hello_pract/profile.html',context)


def login(request):
    pwd = request.POST['password1']
    email = request.POST['email1']
    print pwd
    pwds = pwd.encode()
    if  len(pwd)  < 8:
        messages.error(request,"password invalid  or length too short")
        return render(request,'hello_pract/main.html')
    else:
        hashed = bcrypt.hashpw(pwds, bcrypt.gensalt())
        if bcrypt.hashpw(pwds, hashed) == hashed:
           print("It Matches!")
           print hashed
    user = User.objects.login(email,pwd)
    if user == False:
        messages.error(request, 'Unsuccessful login')
        return render(request,'hello_pract/main.html')
    else:

        print "User id ",user[1].id
        request.session['user_id'] = user[1].id
        #User.objects.get(id=request.session['user_id']),

        context = {
          'user':User.objects.get(id=request.session['user_id']),
          'message': 'logged in'
        }
        return render(request,'hello_pract/index.html',context)
def  register(request):
    name = request.POST['name']
    company_name = request.POST['company_name']
    print company_name
    email = request.POST['email']
    pwd = request.POST['password']
    print pwd
    cpwd = request.POST['pw']
    pwds = pwd.encode()
    cpwds = cpwd.encode()
    if not pwd == cpwd or len(pwd) < 8:
        messages.error(request,"passwords do not match or length too short")
        return render(request,'hello_pract/main.html')
    else:
        hashed1 = bcrypt.hashpw(cpwds, bcrypt.gensalt())
        hashed = bcrypt.hashpw(pwds, bcrypt.gensalt())
        if bcrypt.hashpw(pwds, hashed) == hashed:
           print("It Matches!")


    user = User.objects.register(name,email,hashed,company_name)
    if user[0] == False:
        #print  user[1][0]
        print "BOOOSSS"
        messages.error(request, 'One or more of your input is invalid')
        return render(request,'hello_pract/main.html')

    print "here"
    print user
    print 'OK'
    users = User.objects.all()
    print "User id ",user[1].id
    request.session['user_id'] = user[1].id
    print users

    context = {
      'user':User.objects.get(id=request.session['user_id']),
      'message':'registered'
    }


    return render(request,'hello_pract/index.html',context)

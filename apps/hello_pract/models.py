from __future__ import unicode_literals

from django.db import models

import re,bcrypt


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')


# Create your models here.
class UserManager(models.Manager):
    def login(self,email,pwd):
       user = self.filter(email=email).first()
       print user.password

       if bcrypt.hashpw(pwd.encode(), user.password.encode()) == user.password:
			return (True, user)
       else:

			return (False)




    def register(self, name,email,hashed,company_name):
            print "just landed"
            cop = Company.objects.get(name=company_name)
            print "Still working"
            print cop.score
            cops = cop.id
            print "Company got here"
            comp = Company.objects.get(id=cops)
            print "it works"
            error = []
            if len(name) < 2 or not NAME_REGEX.match(name):
                error.append("Invalid  Name")
                print "Failed"



            if not EMAIL_REGEX.match(email):
                error.append("Invalid Email")
                print "NO EMAIL"

            if len(error) > 0:
                 return(False,error)
            else:
                #user = User.objects.create(name=name,company_name=company_name,email=email,password=pwd)
                user = User.objects.create(name=name,email=email,password=hashed,company=comp)
                user.save()
                #new = user.first_name
                return(True,user)


class CompanyManager(models.Manager):
    def comp(request):
            return True

class Company(models.Model):
    name = models.CharField(max_length=255)
    score = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CompanyManager()

class Score(models.Model):
    score = models.IntegerField()

class User(models.Model):
  name = models.CharField(max_length=255)
  company = models.ForeignKey(Company, related_name="employees")
  user_score = models.OneToOneField(Score,null=True)
  email = models.CharField(max_length=255)
  company_name = models.CharField(max_length=255)
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  objects = UserManager()

 # def __str__(self):
    #S    return self.name+" "+" "+self.email+" "

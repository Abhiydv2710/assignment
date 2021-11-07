
from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from django.contrib import messages
from fore.models import Regi
# Create your views here.
def home(request):
    return render(request,'registration.html')





def registration(request):
    if request.method=="GET":
        username = request.GET.get('username')
        firstname = request.GET.get('firstname')
        middlename = request.GET.get('middlename')
        lastname = request.GET.get('lastname')
        
        
        phone = request.GET.get('phone')
        address = request.GET.get('address')
        email = request.GET.get('email')
        password = request.GET.get('pass')
        
        regi=Regi(username=username , firstname=firstname, middlename=middlename, lastname=lastname,
        phone=phone,address=address,email=email,password=password)
        regi.save()
        messages.success(request,"Sucessful")
    
      

        


    return render(request,'login.html')             


def login(request):
        if request.method=="POST":
          email = request.POST.get('email')
        
          password = request.POST.get('pass')
          
          

          
        
          b=Regi.objects.all()
        
          allemail=[item.email for item in b]
          allpassword=[item.password for item in b]
          allpassword=set(allpassword)
        #   print(allpassword)


          allemail=set(allemail)
          flag=0
          for i in allemail:
              
              if i == email:
                  for j in allpassword:
                      print(j,password)

                      if j==password:
                        flag+=1

                    
          
          if flag==1:
                return render(request,'banner.html')

            
                
          else:
        
           return HttpResponse("Does not match !!")
          
        

 
    



                
    
    

# i have create this file by vedsingh
from django.http import HttpResponse
#for templates import ke liye
from django.shortcuts import render

def index(request):
    return render(request,'loginsignup1.html')
    #return HttpResponse("Hello world  <h2>this is index page </h2></br></br><button><a href='http://127.0.0.1:8000/Home   '>Go TO HOme </a></button>")
    
#def ved(request):
#    return HttpResponse("hello world  <a href='aa.html'>HTML file</a>")
def Home(request):
    #djtext1 = request.GET.get('text1', 'default')
    #djtext2 = request.GET.get('text2', 'default')
    djtext3 = request.GET.get('username', 'default')
    djtext4 = request.GET.get('email', 'default')
    djtext5 = request.GET.get('password', 'default')
    print(djtext3)
    print(djtext4)
    print(djtext5)
    
    # analized = djtext
    
   
            
    
    #analized = djtext1
    #vv = djtext2
    
    vvt = {
        'purpose':'heading send to py file ',
        #'analaze_text':analized,
        #'analaze_text1':vv,
        'uname':djtext3,
        'Email':djtext4,
        'pass':djtext5,
        
    }
    return render(request, 'home.html', vvt)

    #return render(request, 'home.html', vvt)

    #return HttpResponse("hello world")
    #return render(request,'aa.html') video 9
def besic(request):
   return render(request, 'besic.html')
def anal(request):
   return render(request, 'index1.html')
from django.shortcuts import render

def home_view(request):
    context = { 'name':'Taraneh' , 'lastname':'kordi' , 'phonenumber':'09876543212' }
    return render(request,'index.html',context)

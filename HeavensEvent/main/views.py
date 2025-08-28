from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

class Home(View):
    def get(request):
        return render(request,'index.html')
    
class EntryPage(View):
    def get(request):
        return render(request,'index.html')

class ShowData(View):
    def get(request):
        return render(request,'index.html')
    
from django.views import View
from ..models import Data
from django.shortcuts import render

class ShowData(View):
    def get(self,request):
        data = Data.objects.all()
        context = {
            'data':data
        }
        return render(request,'show_data.html',context)
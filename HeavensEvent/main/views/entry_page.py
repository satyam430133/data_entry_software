from django.views import View
from django.shortcuts import render,redirect
from ..models import Data

class EntryPage(View):
    def get(self, request):
        return render(request,'entry_page.html')
    
    def post(self,request):
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        location = request.POST.get('location')
        if len(contact) < 10:
            context = {
                "name" : name,
                "contact" : contact,
                "location" :location,
                "alert": '📱 Mobile number must be 10 digits!' 
            }
            return render(request,'entry_page.html',context)
        context = {
            "name" : name,
            "contact" : contact,
            "location" :location,
            "msg" :'Entered data is not correct...',    
        }
        if name and contact and location:
            data = Data.objects.create(name=name,contact=contact,location=location)
            if data:
                return redirect('show_data')
            else:
                return render(request,'entry_page.html',context)
        else:
            return render(request,'entry_page.html',{'alert':'Entered data is not correct...'})
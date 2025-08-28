from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('entry', EntryPage.as_view(), name='entry_page'),
    path('show_data', ShowData.as_view(), name='show_data'),
]

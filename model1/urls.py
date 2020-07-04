from django.urls import path
from model1 import view1

urlpatterns = [
    path('', view1.index, name='index'),
    path('result', view1.showresult, name=''),
]

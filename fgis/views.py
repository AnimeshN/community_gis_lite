from django.shortcuts import render

# Create your views here.
def fgis(request):
    return render(request,'fgis/map.html')
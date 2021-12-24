from django.shortcuts import redirect, render
from .forms import PropertyForm, ActivityForm
from .models import Activity, Property
# Create your views here.

def property_list(request):
    context = {'property_list':Property.objects.all()}
    return render(request, "property_data/property_list.html", context)

def property_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = PropertyForm()
        else:
            property = Property.objects.get(pk=id)
            form = PropertyForm(instance=property)
        return render(request, "property_data/property_form.html",{'form':form})
    else:
        if id == 0:
            form = PropertyForm(request.POST)
        else:
             property = Property.objects.get(pk=id)
             form = PropertyForm(request.POST,instance = property)
        if form.is_valid():
             form.save()
        return redirect('/property/list')  

def property_delete(request,id):
    property = Property.objects.get(pk=id)
    property.delete()
    return redirect('/property/list')

def activity_list(request):
    context = {'activity_list':Activity.objects.all()}
    return render(request, "property_data/property_list.html", context)

def activity_form(request, id=0):
    if request.method == "GET":
        if id==0:
            form = ActivityForm()
        else:
            activity = Activity.objects.get(pk=id)
            form = ActivityForm(instance=activity)
        return render(request, "activity_data/property_form.html",{'form':form})
    else:
        if id == 0:
            form = ActivityForm(request.POST)
        else:
             activity = Activity.objects.get(pk=id)
             form = ActivityForm(request.POST,instance = activity )
        if form.is_valid():
             form.save()
        return redirect('/property/list')  

def activity_delete(request,id):
    activity = Activity.objects.get(pk=id)
    activity.delete()
    return redirect('/property/list')
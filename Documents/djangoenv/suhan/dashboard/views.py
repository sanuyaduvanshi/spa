from django.shortcuts import render,redirect
from beautyapp.models import Citys
from beautyapp.models import Appointment
from django.contrib import messages
from beautyapp.models import Services
from beautyapp.models import Gift
from beautyapp.models import Carriers
from .models import Addstaff




# Create your views here.
def dashboard(request):
    return render(request,'dashboard/home.html')

def guest(request):
    return render(request,'dashboard/guest.html')


def carriers(request):
    careers=Carriers.objects.all()
    return render(request,'dashboard/carriers.html', {'careers':careers})

def gifts(request):
    gifts = Gift.objects.all()
    return render(request,'dashboard/gifts.html',{'gifts':gifts})

def appointment(request):
    appointment = Appointment.objects.all()
    return render(request,'dashboard/appointment.html',{'appointment':appointment} )
# def edit(request, id):
#     city = Citys.objects.get(id=id)
#     context = {'city': city}
#     return render(request, 'crud/edit.html', context)

def update(request, id):
    city = Citys.objects.get(id=id)
    city.name = request.POST['name']
    city.save()
    return redirect(addcity)

def modify(request, id):
    service = Services.objects.get(id=id)
    service.name = request.POST['name']
    service.save()
    return redirect(addservice)


def updates(request, id):
    staff = Addstaff.objects.get(id=id)
    service = Services.objects.get(id=id)
    staff.name = request.POST['name']
    staff.mobileno = request.POST['mobileno']
    service.name = request.POST['service']
    service.save()
    staff.services = service

    staff.save()
    return redirect(addstaff)


def deletes(request,id):
    service = Services.objects.get(id=id)
    service.delete()
    # messages.success(request,('item has been deleted!'))
    return redirect(addservice)

def deleted(request,id):
    appointments=Appointment.objects.get(id=id)
    appointments.delete()
    return redirect(appointment)


def delete(request,id):
    city = Citys.objects.get(id=id)
    city.delete()
    # messages.success(request,('item has been deleted!'))
    return redirect( addcity)

def addservice(request):
    if request.method == 'POST':
        name = request.POST['name']
        service = Services(name=name)
        service.save()
        return redirect(addservice)
    else:
        context_data = {
        'service':Services.objects.all()
        }
    return render(request,'dashboard/addservices.html',context_data)


def addstaff(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobileno = request.POST['mobileno']
        services=request.POST['service']
        se=Services.objects.get(id=services)
        staff=Addstaff(name=name,mobileno=mobileno,services=se)
        staff.save()
        return redirect(addstaff)
    else:
        context_data = {
        'service':Services.objects.all(),
        'staff':Addstaff.objects.all()
        }
    return render(request,'dashboard/addstaff.html',context_data)



def addcity(request):
    if request.method == 'POST':
        name = request.POST['name']
        city = Citys(name=name)
        city.save()
        return redirect(addcity)
    else:
        context_data = {

          'city':Citys.objects.all()


        }

    return render(request,'dashboard/addcity.html',context_data)

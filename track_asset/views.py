from django.shortcuts import render, redirect, get_object_or_404
from .models import Company, Employee, DeviceLog, Device
from .forms import EmployeeForm, DeviceLogForm, Device

# Create your views here.

##No return statement is added because there is not html to render or redirect it to
def addEmployee(request, company_id):
    company = Company.objects.get(id=company_id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.company = company
            employee.save()
    else:
        form = EmployeeForm()

def delegateDevice(request, company_id):
    company = get_object_or_404(Company, id=company_id)
    devices = Device.objects.filter(company=company)
    form = DeviceLogForm()

    if request.method == 'POST':
        form = DeviceLogForm(request.POST)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.employee = form.cleaned_data['employee']
            assignment.device = form.cleaned_data['device']
            assignment.save()

    context = {
        'company': company,
        'devices': devices,
        'form': form,
    }

    def checkedOutDevice(request, device_id):
        device = get_object_or_404(Device, id=device_id)
        logs = DeviceLog.objects.filter(device=device)
        ## In the html, we can show which user it was checked out by and the according date
        print(logs)
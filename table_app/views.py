from django.shortcuts import render
from django.http import HttpResponse
from .models import Machine


def values_endpoint(request):
    """Receive values, store them to database"""

    id_ = request.GET.get('id')
    machine_number = request.GET.get('num')
    status = request.GET.get('status')

    print(f"id: {id_}, machine_number: {machine_number}, status: {status}")

    machine_object = Machine.objects.create(
        machine_id=id_,
        machine_number=machine_number,
        status=status
        )
    
    machine_object.save()
    
    return HttpResponse("OK")


def table_view(request):
    """Get values from database and generate table"""

    
    machine_object = Machine.objects.all().order_by('-id')
    machine_object = list(machine_object)

    context = {
        'table_data': machine_object,
    }

    return render(request, 'table_app/table.html', context)

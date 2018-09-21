from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.utils import json
import os

# Create your views here.

def index_resemblejs(request):
    return render(request, 'resemblejs.html', {})


def execute_subprocess(command, directory):
    base_path = os.path.dirname(os.path.realpath(__file__))
    print(base_path)

    #os.chdir(workspace)
    # os.system("start /wait cmd ")

    # = sub.Popen(command, stdout=sub.PIPE, stderr=sub.PIPE)
    #output, errors = p.communicate()

    # os.chdir(os.joi) creo se debe regresar al anterior
    #os.chdir(dir_path)
    #return output, errors


def headless_resemblejs_process(request):
    if request.method == 'POST':

        execute_subprocess(1, 2)

        # get code
        return HttpResponse(
            json.dumps({"success": True, "response": "Ejecutado con exito", 'errors': []}),
            content_type="application/json", status=200)
    else:
        return HttpResponse(
            json.dumps({"success": False, "response": "Metodo no permitido", 'errors': ["Metodo no permitido"]}),
            content_type="application/json", status=500)


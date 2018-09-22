from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.utils import json
from cypress.functions import cypress_path, screenshots_path
import subprocess
import os
from django.core.files import File

# Create your views here.
from tester.models import Report


def index_resemblejs(request):
    reports = Report.objects.all()
    return render(request, 'resemblejs.html', {"reports": reports})


def execute_subprocess(report):
    base_path = os.path.dirname(os.path.realpath(__file__))

    os.chdir(cypress_path())
    command = '%s run --spec */**/*.spec.js --env registerid=%d' % (os.path.join('node_modules', '.bin', 'cypress'), report.id)
    proc = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()

    # os.chdir(os.joi) se debe regresar al anterior
    os.chdir(base_path)
    return out.decode("utf-8")

def copy_images(report):
    base_path = os.path.dirname(os.path.realpath(__file__))

    os.chdir(cypress_path())

    first = open(os.path.join(screenshots_path(), ("%d-initial.png" % report.id)), "rb")
    second = open(os.path.join(screenshots_path(), ("%d-final.png" % report.id)), "rb")
    # resemble = open(os.path.join(screenshots_path(), ("%d-resemble.png" % report.id)), "r+")

    report.first_image.save(("%d-initial.png" % report.id), File(first), save=True)
    report.second_image.save(("%d-final.png" % report.id), File(second), save=True)
    # report.resemble_image = resemble

    report.save()


def headless_resemblejs_process(request):
    if request.method == 'POST':

        report = Report()
        report.save()

        result = execute_subprocess(report)
        report.report_info = result
        report.save()

        copy_images(report)

        # get code
        return HttpResponse(
            json.dumps({"success": True, "response": "Ejecutado con exito", 'result': result,  'errors': []}),
            content_type="application/json", status=200)
    else:
        return HttpResponse(
            json.dumps({"success": False, "response": "Metodo no permitido", 'errors': ["Metodo no permitido"]}),
            content_type="application/json", status=500)


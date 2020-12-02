import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication

from .models import Project, Run, TestResult, Attachment
from .serializers import ProjectSerializer, RunSerializer, TestResultSerializer, AttachmentSerializer


def HomePage(request):
    projects = Project.objects.all()
    context = {"projects": []}
    for p in projects:
        runs = Run.objects.filter(project_id=p.id)
        context['projects'].append({"project": p, "runs": runs})
    return render(request, 'ReportApp/homepage.html', context)


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class ProjectViewSet(viewsets.ModelViewSet):
    authentication_classes = (CsrfExemptSessionAuthentication,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class RunViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.all()
    serializer_class = RunSerializer
    filterset_fields = ('project_id',)


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    filterset_fields = ('test_result_id',)


class TestResultViewSet(viewsets.ModelViewSet):
    queryset = TestResult.objects.all()
    serializer_class = TestResultSerializer
    filterset_fields = ('run_id', 'status',)


@method_decorator(csrf_exempt, name='dispatch')
class FileFieldView(View):

    def post(self, request, *args, **kwargs):
        if request.POST['project']:
            try:
                project = Project.objects.filter(project_name=request.POST['project'])[0]
            except IndexError:
                return HttpResponse("No such project")
        else:
            return HttpResponse("No information about project provided. You have to specify correct Project name")

        run = Run(name=str(datetime.datetime.now().replace(microsecond=0)), project_id=project.id)
        run.save()

        files = request.FILES.getlist('file_field')
        images = [f for f in files if 'attachment.png' in f.name]
        results = [f for f in files if 'result.json' in f.name]
        for file in results:
            data = json.loads(file.read())

            test_result = TestResult(run_id=run.id,
                                     title=data['name'] if data['name'] else 'undefined',
                                     status=data['status'] if data['status'] else 'undefined',
                                     method_name=data['fullName'] if data['fullName'] else 'undefined',
                                     description=data['description'] if data['description'] else None,
                                     steps=data['steps'] if data['steps'] else None,
                                     parameters=data['parameters'] if data['parameters'] else None,
                                     start=data['start'] if data['start'] else None,
                                     stop=data['stop'] if data['stop'] else None,
                                     uuid=data['uuid'] if data['uuid'] else None,
                                     history_id=data['historyId'] if data['historyId'] else None,
                                     test_case_id=data['testCaseId'] if data['testCaseId'] else None,
                                     labels=data['labels'] if data['labels'] else None)
            test_result.save()

            if data['attachments']:
                for attachment in data['attachments']:
                    if attachment['type'] == "image/png":
                        name = attachment['name']
                        source = [i for i in images if i.name == attachment['source']][0]
                        attach = Attachment(name=name, image=source, test_result_id=test_result.id)
                        attach.save()

        return HttpResponse()

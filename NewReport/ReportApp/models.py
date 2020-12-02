from django.db import models


class Project(models.Model):
    project_name = models.CharField(max_length=100, unique=True, blank=False)

    def __str__(self):
        return self.project_name


class Run(models.Model):
    name = models.CharField(max_length=100, blank=False)
    project = models.ForeignKey(Project, related_name='runs', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project.project_name} {self.name}"


class TestResult(models.Model):
    run = models.ForeignKey(Run, on_delete=models.CASCADE, related_name='test_results')

    title = models.CharField(max_length=100)
    status = models.CharField(max_length=20)
    method_name = models.CharField(max_length=200)
    severity = models.CharField(max_length=20, blank=True, null=True)
    parameters = models.JSONField(max_length=2000, blank=True, null=True)
    steps = models.JSONField(max_length=2000, blank=True, null=True)
    description = models.TextField(max_length=2000, blank=True, null=True)
    start = models.BigIntegerField(blank=True, null=True)
    stop = models.BigIntegerField(blank=True, null=True)
    uuid = models.UUIDField(blank=True, null=True)
    history_id = models.UUIDField(blank=True, null=True)
    test_case_id = models.UUIDField(blank=True, null=True)
    labels = models.JSONField(max_length=2000, blank=True)

    def __str__(self):
        return f"{self.run.project.project_name} {self.run.name} {self.title}"


class Attachment(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    test_result = models.ForeignKey(TestResult, related_name='attachments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

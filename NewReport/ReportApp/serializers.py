from rest_framework import serializers

from .models import Project, Run, TestResult, Attachment


class TestResultSerializer(serializers.HyperlinkedModelSerializer):
    attachments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = TestResult
        fields = ['run_id', 'title', 'method_name', 'status', 'severity', 'parameters', 'steps', 'start', 'stop',
                  'uuid',
                  'history_id', 'test_case_id', 'labels', 'attachments']


class RunSerializer(serializers.HyperlinkedModelSerializer):
    test_results = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Run
        fields = '__all__'


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    runs = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'runs']


class AttachmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attachment
        fields = ['name', 'image', 'test_result']

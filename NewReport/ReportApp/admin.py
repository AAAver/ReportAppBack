from django.contrib import admin
from django.db import models
from django.forms import TextInput

from .models import Project, Run, TestResult, Attachment


class AttachmentInline(admin.StackedInline):
    model = Attachment
    extra = 0


class TestResultAdmin(admin.ModelAdmin):
    fields = ['run', 'title', 'method_name', 'status', 'severity', 'parameters', 'steps', 'start', 'stop', 'uuid',
              'history_id', 'test_case_id', 'labels']
    inlines = [AttachmentInline]

    readonly_fields = ['start', 'stop', 'uuid', 'history_id', 'test_case_id']
    #
    # def get_readonly_fields(self, request, obj=None):
    #     if obj:  # editing an existing object
    #         # All model fields as read_only
    #         return self.readonly_fields + tuple([item.name for item in obj._meta.fields])
    #     return self.readonly_fields
    #
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super(TestResultAdmin, self).get_form(request, obj, **kwargs)
    #     form.base_fields['start'].widget.attrs['style'] = 'width: 20em;'
    #     form.base_fields['stop'].widget.attrs['style'] = 'width: 20em;'
    #     return form

class RunInline(admin.TabularInline):
    model = Run
    show_change_link = True
    can_delete = False
    extra = 0


class ProjectAdmin(admin.ModelAdmin):
    fields = ['project_name']
    inlines = [RunInline]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Run)
admin.site.register(TestResult, TestResultAdmin)
admin.site.register(Attachment)

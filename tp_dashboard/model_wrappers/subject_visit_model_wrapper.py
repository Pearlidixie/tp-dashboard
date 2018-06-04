from django.conf import settings
from edc_subject_dashboard import SubjectVisitModelWrapper as BaseSubjectVisitModelWrapper


class SubjectVisitModelWrapper(BaseSubjectVisitModelWrapper):

    model = 'tp_subject.subjectvisit'
    next_url_name = settings.DASHBOARD_URL_NAMES.get('subject_dashboard_url')

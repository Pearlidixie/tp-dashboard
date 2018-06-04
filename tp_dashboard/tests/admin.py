from django.contrib.admin import AdminSite as DjangoAdminSite

from .models import SubjectConsent, SubjectLocator
from .models import SubjectRequisition, SubjectVisit, SubjectScreening


class AdminSite(DjangoAdminSite):
    site_title = 'Training Subject'
    site_header = 'Training Subject'
    index_title = 'Training Subject'
    site_url = '/administration/'


tp_test_admin = AdminSite(name='tp_test_admin')

tp_test_admin.register(SubjectScreening)
tp_test_admin.register(SubjectConsent)
tp_test_admin.register(SubjectLocator)
tp_test_admin.register(SubjectVisit)
tp_test_admin.register(SubjectRequisition)

from edc_subject_dashboard.model_wrappers.appointment_model_wrapper import(
    AppointmentModelWrapper as BaseAppointmentModelWrapper)

from .subject_visit_model_wrapper import SubjectVisitModelWrapper


class AppointmentModelWrapper(BaseAppointmentModelWrapper):

    visit_model_wrapper_cls = SubjectVisitModelWrapper

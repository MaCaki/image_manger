from django.views import generic

from .forms import ImageFieldForm
from .models import Study


class StudyIndexView(generic.ListView):
    """The landing page for the app is a list of studies to grade for."""
    model = Study
    template_name = 'core/study_index.html'


class StudyDetailView(generic.DetailView):
    model = Study
    template_name = 'core/study_detail.html'


# https://docs.djangoproject.com/en/1.11/topics/http/file-uploads/

class ImageFieldView(generic.edit.FormView):
    form_class = ImageFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                pass
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
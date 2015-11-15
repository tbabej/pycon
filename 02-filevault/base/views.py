import os

from django.conf import settings
from django.http import HttpResponse
from django.views.generic.edit import CreateView, FormView

from .models import Submission

# Create your views here.
class SubmissionCreateView(CreateView):
    model = Submission
    fields = ['description', 'secret']
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(SubmissionCreateView, self).get_context_data(**kwargs)
        context['submissions'] = Submission.objects.all()
        return context

def download_submission(request, submission_id):
    submission = Submission.objects.get(pk=submission_id)
    filepath = os.path.join(settings.UPLOAD_DIR, submission.secret.path)
    basepath = os.path.basename(filepath)

    with open(filepath, 'r') as f:
        response = HttpResponse(mimetype='image/jpeg')
        response['Content-Disposition'] = 'attachment; filename="{0}"'.format(basepath)
        response.write(f.read())

    return response

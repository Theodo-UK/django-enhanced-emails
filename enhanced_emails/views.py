from django.views.generic.detail import DetailView

from .models import SentEmail


class EmailView(DetailView):
    model = SentEmail
    template_name = "enhanced_emails/email.html"

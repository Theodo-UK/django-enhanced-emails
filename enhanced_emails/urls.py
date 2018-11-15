from django.urls import path

from .views import EmailView

urlpatterns = [path("<uuid:pk>", EmailView.as_view(), name="email")]

app_name = "enhanced_emails"

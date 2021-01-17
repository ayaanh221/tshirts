from django.conf.urls import url
from django.urls import reverse
from django.contrib.auth.views import PasswordResetView


urlpatterns = [
   url(
        'accounts/password_reset/',
        PasswordResetView.as_view(),
        name='password_reset'
    ),
]
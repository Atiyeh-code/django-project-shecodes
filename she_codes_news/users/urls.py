from django.urls import path, include
from . import views
from .views import CreateAccountView, ViewProfile

app_name = 'users'

urlpatterns = [
    path(
        'create-account/',
        CreateAccountView.as_view(),
        name='createAccount'
    ),
    path(
        'view-profile/',
        views.ViewProfile.as_view(),
        name='profile'
    )
]
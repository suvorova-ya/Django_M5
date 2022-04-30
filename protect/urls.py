from django.urls import path
from .views import IndexView

urlpatterns = [
    path('personal', IndexView.as_view(),name='personal account'),
]
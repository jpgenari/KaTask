from django.urls import path
from .views import DisplayHomeView

urlpatterns = [
    path('', DisplayHomeView.as_view(), name='home'),
]
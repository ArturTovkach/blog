from . import views
from django.urls import path


urlpatterns = [
    path('reg/', views.register, name='reg'),
    path('profile/', views.profile, name='profile')
]

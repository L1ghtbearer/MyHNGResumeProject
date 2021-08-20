from django.contrib import admin
from django.urls import path

from contact import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"),
    path('contact/', views.contact_view, name='contact'),
]

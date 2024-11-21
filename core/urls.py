from django.contrib import admin
from django.urls import path

from .views import HomeView, ContactView, ClassificationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('classification/', ClassificationView.as_view(), name='classification'),
]
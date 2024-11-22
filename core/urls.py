from django.contrib import admin
from django.urls import path

from .views import HomeView, ContactView, ClassificationView, RoutesView, ContainersView, LoginView, LogoutView, SignupView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('classification/', ClassificationView.as_view(), name='classification'),
    path('routes/', RoutesView.as_view(), name='routes'),
    path('containers/', ContainersView.as_view(), name='containers'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup'),
]
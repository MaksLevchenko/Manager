from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from Client_Manager import views
from Manager import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.LandingView.as_view(), name='lending'),
    path('success/', views.SuccessView.as_view(), name='success'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='signout'),
    path('home/', views.ClientListView.as_view(), name='home'),
    path('home/<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),
]

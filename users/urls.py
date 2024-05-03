from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.UserRegistrationView.as_view(), name='signup'),
    path('login/',views.UserLoginView.as_view(), name='login'),
    path('logout/',views.UserLogoutView.as_view(), name='logout'),
    path('profile/',views.Profile.as_view(), name='profile'),
    path('edit_profile/',views.UserAccountUpdateView.as_view(), name='edit_profile'),
    path('change_password/', views.pass_change, name='change_pass'),
    path('forgot_password/', views.forgot_pass, name='set_pass'),
]
from django.urls import path
from .views import home,signup, app, redirect_link,delete_link
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [    
    path('',home,name='home'),
    path('app/',app,name='app'),
    path('r/<str:unique_code>/',redirect_link,name='redirect_link'),
    path('delete/<str:unique_code>/',delete_link,name='delete_link'),
    
    path('signup/',signup,name='signup'),
    path('login/',LoginView.as_view(template_name = 'core/login.html'),name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),

]
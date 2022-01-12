from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.welcome, name='welcome'),    
    path('login/', views.login_view, name='login'),
    path('signup/', views.usersignup, name='signup'),
    path('activate/<uidb64>/<token>/',views.activate_account, name='activate'),
    path('registration/', include('django_registration.backends.activation.urls')),
    path('registration/', include('django.contrib.auth.urls')),
    
] 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
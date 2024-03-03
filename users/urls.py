
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name ='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('register/', views.register, name ='register'),
    path('showAllBooks/', views.catalogue, name='catalogue'),
    
] 
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from main.models import Task # Импорт модели задачи
from rest_framework.routers import SimpleRouter # импортирую роутер
from main.views import TaskViewSet # Импорт модели задачи
from django.conf import settings
from django.conf.urls.static import static
router = SimpleRouter() # Объявляю роутер

router.register(r'task', TaskViewSet) #регистрирую его



urlpatterns = [
    path('grappelli/', include('grappelli.urls')), 
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('register/', include('register.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='register/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='register/logout.html'), name='logout'),
    path('manual/', include('userManual.urls')),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    

urlpatterns +=router.urls

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
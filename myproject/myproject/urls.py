from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.homepage,name='home'),
    path('about/',views.about,name='about'),
    path('posts/', include('posts.urls')),
    path('users/',include('users.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
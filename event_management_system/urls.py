from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/event/', include('event.urls')),
]

urlpatterns += [
    path('api/v1/auth_token/', auth_views.obtain_auth_token)
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line includes all the default Django authentication URLs (login, logout, etc.).
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('tweet_app.urls')),
]
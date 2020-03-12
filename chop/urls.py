"""chop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from discipline_journal.views import profile_list, profile_detail, profile_new, profile_update, profile_delete,\
 punishment_new, punishment_update, punishment_delete

urlpatterns = [
    path('', profile_list, name='profile_list'),
    path('profile/new/', profile_new, name='profile_new'),
    path('profile/<slug:slug>/delete', profile_delete, name='profile_delete'),
    path('profile/<slug:slug>/detail', profile_detail, name='profile_detail'),
    path('profile/<slug:slug>/detail/punishment/new', punishment_new, name='punishment_new'),
    path('profile/<slug:slug>/detail/punishment/<int:id>/update', punishment_update, name='punishment_update'),
    path('profile/<slug:slug>/detail/punishment/<int:id>/delete', punishment_delete, name='punishment_delete'),
    path('profile/<slug:slug>/update', profile_update, name='profile_update'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

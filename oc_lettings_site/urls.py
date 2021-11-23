from django.contrib import admin
from django.urls import path

from lettings.views import letting, lettings_index
from profiles.views import profile, profiles_index
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path('lettings/', lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting, name='letting'),
    path('profiles/', profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profile, name='profile'),
    path('admin/', admin.site.urls),
]

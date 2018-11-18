from django.contrib import admin
from django.urls import path, re_path
from ItemsAPI import views
from rest_framework.urlpatterns import format_suffix_patterns
from UserAPI import views as user_views

urlpatterns = [
    
    #admin/
    path('admin/', admin.site.urls),

    #laptop/
    path('laptop/', views.LaptopList.as_view()),
    #laptop/1/
    re_path('laptop/(?P<pk>[0-9]+)/', views.LaptopDetail.as_view()),
    
    #laptop/?page=1
    #List the first page

    #accessory/
    path('accessory/', views.AccessoryList.as_view()),
    #accessory/1/
    re_path('accessory/(?P<pk>[0-9]+)/', views.AccessoryDetail.as_view()),
    
    #server/
    path('server/', views.ServerList.as_view()),
    #server/1/
    re_path('server/(?P<pk>[0-9]+)/', views.ServerDetail.as_view()),
    
    #gpu/
    path('gpu/', views.GPUList.as_view()),
    #gpu/1/
    re_path('gpu/(?P<pk>[0-9]+)/', views.GPUDetail.as_view()),
    
    #users/
    path('users/', user_views.UserList.as_view()),

    #users/1/
    re_path('users/(?P<pk>[0-9]+)/', user_views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

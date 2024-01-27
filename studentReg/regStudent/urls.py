from django.urls import path
from .import views
urlpatterns = [
    path('',views.insert,name='register'),
    path('view/',views.view,name='view'),
    path('detailview/<str:pk>',views.detailview,name='detailview'),
    path('update/<str:pk>',views.update,name='update'),
    path('update2/<str:pk>',views.update2,name='update2'),
    path('delete/<str:pk>',views.delete,name='delete'),
    path('login/',views.login,name='login'),
    path('display/',views.display,name='display'),
    path('logout/',views.logoutuser,name='logout'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('alogin/',views.alogin,name='alogin'),
]
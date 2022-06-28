from django.urls import path
from . import views  #引用這個資料夾中的views檔案

urlpatterns = [
    path('', views.index, name = "Index"),
    path('update/<str:pk>', views.update, name='Update'),
    path('delete/<str:pk>', views.delete, name='Delete')
]
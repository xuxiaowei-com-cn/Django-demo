from django.urls import path

from . import views

app_name = 'tests'

urlpatterns = [
    # 主页
    path('', views.index, name='index')
]

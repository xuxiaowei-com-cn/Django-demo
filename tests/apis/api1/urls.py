from django.urls import path

from . import views

app_name = 'tests/apis/api1'

urlpatterns = [
    # 主页
    path('', views.index, name='index')
]

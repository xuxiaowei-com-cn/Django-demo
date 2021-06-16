from django.urls import path

from tests.apis import views

app_name = 'tests/apis'

urlpatterns = [
    # 主页
    path('', views.index, name='index')
]

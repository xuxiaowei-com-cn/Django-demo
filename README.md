# Django-demo

## Django

- [Django 文档](https://docs.djangoproject.com/zh-hans/3.2/)

```
pip install django
```

- 在 Django 中创建项目

```
django-admin startproject django_demo .
```

- 创建数据库

```
python manage.py migrate
```

- 查看项目

```
python manage.py runserver 12345
```

- 创建超级用户

```
python manage.py createsuperuser
```

- 迁移模型

```
python manage.py makemigrations django_demo
python manage.py migrate
```

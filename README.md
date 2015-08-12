Django
======

Django applications

1. If you have Django installed, you can use the following commands to check its version
```python
  python -c "import django; print(django.get_version())"
 ```

2. Use django-admin to create an new app
  django-admin startproject myapp

   The structure it generated is as follows:
      mysite/
          manage.py
          mysite/
            __init__.py
            settings.py
            urls.py
            wsgi.pys

3. Use manage.py to start your first app
  python manage.py runservers
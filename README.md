Django
======

Django applications

## If you have Django installed, you can use the following commands to check its version
```python
  python -c "import django; print(django.get_version())"
 ```

## Use django-admin to create an new app
```python
  django-admin startproject myapp
```
   The structure it generated is as follows:

      mysite/

          manage.py

          mysite/

            __init__.py

            settings.py

            urls.py

            wsgi.pys

## Use manage.py to start your first app
```python
  python manage.py runservers
```
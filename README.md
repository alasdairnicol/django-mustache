django-mustache
===============

django-mustache is a template engine for Django 1.8+.

It uses [pystache][1], a Python implementation of Mustache.

It was built as a proof of concept for a talk at DjangoCon EU 2015.

Requirements
============

 * pystache
 * Django 1.8+

Installation
============

You can install from github using pip:

    pip install git+git://github.com/alasdairnicol/django-mustache.git@master

Install the requirements:

    pip install django pystache

In your settings.py, enable the

    TEMPLATES = [
        {
	    existing backends
	},
	{
        'BACKEND': 'django_mustache.backends.mustache.Mustache',
        'APP_DIRS': True,
        },
    ]

In your app's template directory, create a `mustache` directory for your templates

    myapp/
        templates/
	    mustache/
	        mytemplate.html

Django will now render your templates using pystache:

    def my_mustache_view(request):
        return render(request, "mytemplate.html", {})

[1]: https://github.com/defunkt/pystache
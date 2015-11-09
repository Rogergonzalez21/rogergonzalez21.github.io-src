¿Cómo configurar tu primer proyecto de Django? Parte II
#######################################################

:date: 2015-10-25 19:08
:category: Programación
:slug: como-configurar-tu-primer-proyecto-de-django-parte-II
:author: Roger González
:summary: Es hora de hacer tu primera aplicación web. En este pequeño tutorial, te voy a enseñar a configurar tu primera aplicación con Django, vistas, modelos y templates.
:tags: django, python

Continuando el ultimo tutorial, ya tenemos nuestro proyecto de Django completamente funcional, pero aún nos falta crear nuestra primera **aplicación**.

Nota: El motivo de este tutorial **no** es crear una aplicación, sino aprender lo básico para hacer una aplicación con Django

Pensé que eso es lo que ya teníamos, ¿Qué está pasando?
-------------------------------------------------------
Una 'aplicación' de Django no es lo mismo que un 'proyecto' de Django. ¿Por qué? Un proyecto es donde viven tus aplicaciónes. En un proyecto puedes tener 'n' aplicaciones, ordenadas y funcionando de forma conjunta. Eso no quiere decir que una aplicación no funcione en otro proyecto, todo lo contrario. El proyecto solo se encarga de mantener tu/tus aplicacion/es ordenada/s y en un mismo sitio.

Para iniciar tu primera aplicación, debes estar en la carpeta del proyecto (donde está :code:`manage.py`), y teclear lo siguiente:

.. code-block:: bash

	(env)user@pc:~/proyecto/tests$ python manage.py startapp app_test

Esto dará inicio a la aplicación "app_test". si accecemos y hacemos :code:`ls`, nos va a mostrar su contenido.

.. code-block:: bash

	(env)user@pc:~/proyecto/tests$ cd app_test
	(env)../app_test$ ls
	
	admin.py  
	__init__.py  
	migrations/  
	models.py  
	tests.py  
	views.py

Vamos a ir viendo para que funciona cada uno de los archivos.

- :code:`admin.py`: Aquí se registran todos los modelos que serán manejados desde el `administrador de Django`_.
- :code:`migrations/`: El directorio donde se guardan las migraciones de la base de datos. Por lo general eso no se toca.
- :code:`models.py`: En este archivo se escriben todos los modelos que van en nuestra aplicación. Si has trabajado antes con SQL, este es el "esquema de base de datos".
- :code:`tests.py`: Para hacer los tests unitarios.
- :code:`views.py`: Aquí van cada una de las vistas de tu aplicación web, eso quiere decir, la lógica de cada pantalla que el usuario va a ver.


Ya que sabemos que hace cada uno de los archivos, vamos a 'instalar' nuestra nueva aplicación en el proyecto. En nuestro archivo :code:`tests/settings.py` agregamos lo siguiente:

.. code-block:: python

	INSTALLED_APPS = (
	    'django.contrib.admin',
	    '...'
	    'app_test', # <----- Añadir nuestra aplicación al final
	)

Ya que nuestra aplicación está correctamente instalada, podemos empezar a hacer **modelos**, **vistas** y **rutas**.


Modelos
-------
Los modelos_ son los encargados de crear y mantener nuestra base de datos, independientemente de que motor de base de datos estemos utilizando (MySQL, SQLServer, PostgreSQL, etc.), lo que nos permite cambiar de motor de forma muy rápida.

Para hacer un modelo básico:

.. code-block:: python

	class Person(models.Model):
	    name = models.CharField(max_length=120)
	    phone = models.CharField(max_length=20)
	    email = models.EmailField(max_length=120)
	    address = models.CharField(max_length=120)

	    def __unicode__(self):
	        return self.name

Como podemos observar, hay diferentes tipos de campos en nuestro modelo. En el ejemplo solo usamos :code:`CharField` y :code:`EmailField` pero hay muchos mas. Siempre tenemos que asegurarnos que estamos usando el correcto. En `esta lista`_ podemos revisar todos los tipos de fields que tiene Django por defecto.

En Django tambien podemos establecer **relaciones**.

Para saber mas sobre modelos de Django, te recomiendo `esta guia`_ (en inglés).

Vistas 
------
Las vistas_ son las que procesan toda la lógica de lo que sucede cuando el usuario interactúa con la página web. Por ejemplo, el envío de un formulario, la petición de una lista, la edición de una serie de datos, etc.

Una vista básica sería la siguiente:

.. code-block:: python

	from django.http import HttpResponse 

	def index(request):
		return HttpResponse('Hola mundo!')

Esta vista solo nos va a devolver "Hola Mundo!", que quizá no sea lo mas interesante del mundo. Vamos a realizar una vista un poco mas completa.

.. code-block:: python
	
	from django.shortcuts import render 
	from app_test.models import Person

	def index(request):
	    persons = Person.objects.all()
	    return render(request, 'index.html', {'persons' : persons})

En esta vista estamos haciendo varias cosas. Primero, estamos importando nuestro modelo, :code:`Person`, y :code:`render`, que nos va a formatear el contexto en una plantilla HTML.

Luego, en nuestra función :code:`index`, hacemos una búsqueda en nuestra base de datos que nos devuelve a todas las personas. Es lo mismo que hacer un SQL:

.. code-block:: sql

	SELECT * FROM Person

Y por ultimo, retornamos :code:`render` con el nombre de nuestro template (:code:`index.html`) y nuestro diccionario (:code:`{'persons' : persons}`). Mas adelante veremos como funcionan las vistas en conjunto con los templates.

Para saber mejor como funcionan las vistas, te recomiendo `esta página`_

URL's
-----
El concepto del URL es básico. ¿Cómo un usuario va a llegar a nuestra flamante y nueva aplicación, si no tienen como hacerlo? Aquí es donde llegan las URL. Las URL no son mas que la dirección de las páginas de la aplicación. Cada una de las vistas de nuestra aplicación debe tener una URL para que puedan ser accedidas. Por ejemplo, :code:`www.miaplicacionweb.com/app-test`. Para definir nuestras URL's, tenemos que crear un archivo para colocarlas. En :code:`tests/app_test/` vamos a crear un archivo que se llame :code:`urls.py` y vamos a añadir lo siguiente:

.. code-block:: python

	from django.conf.urls import patterns, url
	from app_test import views

	urlpatterns = patterns('',
	        url(r'^index$', views.index, name='index'),

	    )

Aquí me voy a detener un poco.

- Primero, importamos :code:`patterns` y :code:`url`, que son necesarios para la creación de URL's, y nuestras vistas.
- Luego, creamos nuestros patterns. Cada pattern se compone por un :code:`url`, que a su vez se compone por:

  + Una expresion regular que dice cual es la dirección de la URL. En nuestro caso es "index"
  + La vista que representa
  + El nombre para identificar la URL

Luego de registrar los URL de la app, hay que registrar los URL del proyecto. En :code:`tests/urls.py` vamos a modificar lo siguiente:

.. code-block:: python

	from django.conf.urls import include, url
	from django.contrib import admin

	urlpatterns = [
	    url(r'^admin/', include(admin.site.urls)),
	    url(r'^', include('app_test.urls')), # <----- Agregar esta linea!
	]

Siguiendo la misma lógica del anterior, el url se compone por:

- Una expresión regular que dice cual es la dirección de la URL. En esta caso es ''.
- Un include de nuestro archivo de URL's en la aplicación :code:`app_test`

Ya que tenemos nuestros URL's configurados, podemos acceder a nuestra vista desde el navegador. Para saber mas sobre URL's, puedes investigar en `este enlace`_

Solo falta el template para poder renderizar lo que queremos.

Templates
---------
Llegamos a la última parte de este tutorial. Los templates son los archivos :code:`.html` que se van a visualizar en el navegador. Simple, ¿no?. Para generar contenido dinámico, Django hace uso del lenguaje de templates Jinja2_. En nuestro directorio :code:`app_test/` vamos a crear una carpeta que se llame "templates" y otra que se llame "static". En "templates" vamos a crear un archivo que se llame :code:`index.html` y vamos a agregar lo siguiente:

.. code-block:: html

  <!DOCTYPE html>
  <html>
    <head>
      <title>Test page</title>
    </head>
    <body>
      <h1>Hola mundo!</h1>
      <table class="table table-hover">
      <thead>
      <tr>
      <th>Nombre</th>
      <th>Teléfonos</th>
      <th>Email</th>
      <th>Dirección</th>
      </tr>
      </thead>
      <tbody>
      {% for person in persons %}
      <tr>
      <td>{{ person.name }}</td>
      <td>{{ person.phone_num }}</td>
      <td>{{ person.email }}</td>
      <td>{{ person.address }}</td>
      </tr>
      {% endfor %}
      </tbody>
      </table>
    </body>
  </html>




.. _administrador de Django: https://docs.djangoproject.com/en/1.8/ref/contrib/admin/
.. _modelos: https://docs.djangoproject.com/en/stable/topics/db/models/
.. _esta lista: https://docs.djangoproject.com/en/1.8/ref/models/fields/#model-field-types
.. _esta guia: https://docs.djangoproject.com/en/stable/topics/db/models/
.. _vistas: https://docs.djangoproject.com/en/1.8/topics/http/views/
.. _esta página: https://docs.djangoproject.com/en/1.8/topics/http/views/
.. _este enlace: https://docs.djangoproject.com/en/1.8/topics/http/urls/
.. _Jinja2: http://jinja.pocoo.org/docs/dev/

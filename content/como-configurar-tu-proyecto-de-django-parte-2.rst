¿Cómo configurar tu primer proyecto de Django? Parte II
#######################################################

:date: 2015-10-25 19:08
:category: Programación
:slug: como-configurar-tu-primer-proyecto-de-django-parte-II
:author: Roger González
:summary: Es hora de hacer tu primera aplicación web. En este pequeño tutorial, te voy a enseñar a configurar tu primera aplicación con Django, vistas, modelos y templates.
:tags: django, python

Continuando el ultimo tutorial, ya tenemos nuestro proyecto de Django completamente funcional, pero aún nos falta crear nuestra primera **aplicación**.

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


	

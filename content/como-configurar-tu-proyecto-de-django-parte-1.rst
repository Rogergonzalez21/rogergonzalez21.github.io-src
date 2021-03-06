¿Cómo configurar tu primer proyecto de Django? Parte I
######################################################

:date: 2015-10-25 19:08
:category: Programación
:slug: como-configurar-tu-primer-proyecto-de-django-parte-I
:author: Roger González
:summary: Es hora de hacer tu primera aplicación web. En este pequeño tutorial, te voy a enseñar a configurar tu primer proyecto con Django.
:tags: django, python
:status: published

Es hora de hacer tu primera aplicación web. En este pequeño tutorial, te voy a enseñar a configurar tu primera aplicación con Django.

Primero, ¿Qué demonios es Django?
---------------------------------

.. figure:: {filename}/images/django_tutorial/django.png
    :alt: Django

*- Django.*
*- Can you spell it?*
*- D-J-A-N-G-O. The 'D' is silent.*

Django_ es un framework web hecho completamente en Python, escalable, que ayuda a un desarrollo rápido de aplicaciones web.

Funciona con el lenguaje de programación Python_, que es muy sencillo de aprender. Aquí tienes un tutorial_ muy completo y entendible.


¿Y qué páginas web utilizan Django?
-----------------------------------

Buena pregunta, mi querido Padawan. Aquí te muestro 3 aplicaciones grandes que usan Django:

- Disqus_

.. image:: {filename}/images/django_tutorial/disqus.png
    :alt: Disqus
    :target: https://disqus.com/home/explore/

Si, la popular aplicación de comentarios, usada por millones de personas (¡Incluso en este sitio!), funciona con Django.

- Instagram_

.. image:: {filename}/images/django_tutorial/instagram.png
    :alt: Instagram
    :target: https://instagram.com/

El sitio superpopular de compartir fotos también está hecho en Django.

- Pinterest_

.. image:: {filename}/images/django_tutorial/pinterest.png
    :alt: Pinterest
    :target: https://pinterest.com/

Django es popular entre los sitios de imágenes, porque provee todas las herramientas que se necesitan para **escalar** y soportar miles de vistas inmediatas de contenido.

Aquí_ tienes más páginas hechas con Django.


¿Convencido? Entonces comencemos instalando los paquetes requeridos.
--------------------------------------------------------------------

Voy a asumir que estás usando Ubuntu Linux. Si tienes la última versión, ya tienes Python instalado.

Primero, tienes que instalar los paquetes de desarrollo, el `virtual environment`_ y pip_.

.. code-block:: bash
    
    user@pc:~$ sudo apt-get install python-dev virtualenv python-pip

Estos son todos los paquetes que necesitaremos para la instalación de nuestra primera aplicación de Django.


Iniciando la aplicación
-----------------------

Crea un nuevo directorio, vamos a llamarlo :code:`proyecto`

.. code-block:: bash
    
    user@pc:~$ mkdir proyecto
    user@pc:~$ cd proyecto

Dentro de :code:`proyecto` vamos a iniciar nuestro primer entorno virtual de desarrollo (virtualenv). **¿Por qué necesitamos un virtualenv?** Porque cada proyecto puede tener sus propios paquetes con sus propias versiones. Es una buena práctica instalar los paquetes localmente en un entorno virtual por proyecto.

.. code-block:: bash

    user@pc:~/proyecto$ virtualenv env
    New python executable in env/bin/python
    # Se ejecutará la instalación de tu virtualenv
    
    user@pc:~/proyecto$ source env/bin/activate
    (env)user@pc:~/proyecto$

Ya estamos dentro de nuestro virtualenv (¿Ven como bash cambió el comienzo de nuestra línea? ahora comienza con :code:`env`). Igual, podemos revisar qué versión de Python estamos usando si escribimos en nuestro terminal :code:`which python`

.. code-block:: bash

    (env)user@pc:~/proyecto$ which python
    /home/user/proyecto/env/bin/python

Ahora, ¡A instalar Django!

.. code-block:: bash

    (env)user@pc:~/proyecto$ pip install django
    Collecting django
    ...

Espera, espera. ¿Qué está pasando aquí?
---------------------------------------

Usando el administrador de paquetes de Python, :code:`pip` instalamos los paquetes **directamente en nuestro virtualenv**, así no necesitamos el uso de :code:`sudo`, porque no lo vamos a instalar como un paquete global.

Luego de que instalamos Django, podemos ejecutar el creador de aplicaciones automático de Django. Vamos a crear un proyecto que se llame :code:`tests`

.. code-block:: bash
    
    (env)user@pc:~/proyecto$ django-admin.py startproject tests
    
    # Revisamos si todo fué creado correctamente
    
    (env)user@pc:~/proyecto$ ls
    env/ tests/
    
    # Accedemos a 'tests'

    (env)user@pc:~/proyecto$ cd tests
    (env)user@pc:~/proyecto/tests$

Dentro de :code:`tests` vive nuestro proyecto de Django.

Prueba final. Redobles por favor
--------------------------------

Ejecutemos el servidor de Django para revisar que todo esté correcto.

.. code-block:: bash

    (env)user@pc:~/proyecto/tests$ python manage.py runserver

    # Quizá aparezcan unos errores, es normal

    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Si entramos en nuestro navegador a la dirección :code:`http://127.0.0.1:8000/`, nos saldrá este bello mensaje:

.. image:: {filename}/images/django_tutorial/it_worked.png
    :alt: Django


¡Funcionó! ¡Aplausos para tí!
-----------------------------

Así_ debería de verse tu proyecto ahora.

Igualmente, esto no es todo. Solo hemos configurado tu primer proyecto. Aún faltan crear tu aplicación, sus vistas, modelos, templates y por último, aprender a hacer el deployment... Pero no te asustes, todo lo cubriremos más adelante.

Mientras tanto, ¡Hasta la próxima!

`Parte 2: Aplicación, Vistas, Modelos, Templates y URLS`_

`Parte 3: Django Admin y Formularios`_

.. _Python: https://www.python.org/
.. _tutorial: https://www.codecademy.com/es/tracks/python
.. _Disqus: https://disqus.com/home/explore/
.. _Instagram: https://instagram.com/
.. _Pinterest: https://pinterest.com/
.. _Django: https://www.djangoproject.com/
.. _virtual environment: https://virtualenv.pypa.io/en/latest/
.. _pip: https://es.wikipedia.org/wiki/Pip_%28administrador_de_paquetes%29
.. _Aquí: http://codecondo.com/popular-websites-django/
.. _Así: https://github.com/Rogergonzalez21/django-tutorial/tree/4fe1d18891dbd3d6da202a906fb064bfba357b8b
.. _`Parte 2: Aplicación, Vistas, Modelos, Templates y URLS`: {filename}/como-configurar-tu-proyecto-de-django-parte-2.rst
.. _`Parte 3: Django Admin y Formularios`: {filename}/como-configurar-tu-proyecto-de-django-parte-3.rst
¿Cómo hacer un deploy de una aplicación de Django a Openshift?
##############################################################

:date: 2015-11-26 13:40
:category: Programación
:slug: deploy-django-a-openshift
:author: Roger González
:summary:
    Algo muy importante luego de que haces tu aplicación en Django es hacer el deploy. ¿Como van a usar tu aplicación **si no se puede llegar a ella**?.
:tags: deploy, django, openshift, python, tutorial
:status: published

Algo muy importante luego de que haces tu aplicación en Django es hacer el deploy. ¿Como van a usar tu aplicación **si no se puede llegar a ella**?.

Aquí llega Red Hat al rescate con su servicio PaaS_, OpenShift_.

¿Qué es OpenShift? ¿Eso con qué se come?
----------------------------------------
OpenShift es el servicio de "Plataforma-como-servicio" de Red Hat. Simple, ¿no?. Lo más importante que tiene OpenShift es que con su cuenta gratuita **se pueden tener hasta 3 aplicaciones en vivo**, incluso con **dominios propios**, características que lo convierten en una de las mejores opciones para hacer deploy de aplicaciones web.

Ya creé mi cuenta en OpenShift, ¿Ahora qué?
-------------------------------------------
Primero, tienes que `configurar tu cuenta`_. Si no configuras tu cuenta, no podrás acceder a tus aplicaciones
via Git.

Luego, desde tu panel de control debes **crear tu primera aplicación**.

.. image:: {filename}/images/deploy_django/add_aplication.png
    :alt: Añadir aplicación

Para efectos de este tutorial, vamos a crear una aplicación de Python 2.7.

.. image:: {filename}/images/deploy_django/python_2.7.png
    :alt: Python 2.7

Llenamos toda la información que nos pide, y luego esperamos a que nos lleve al panel de control de la aplicación.
Una vez en el panel de control, añadimos el cartucho de MySQL y el de PHPMyAdmin (opcional).

¡Ahora podemos clonar nuestro repositorio en OpenShift vía Git! En la parte derecha del panel de control
nos dice "Source code". Ese es el link de nuestro repositorio, al que podemos acceder con "git clone" desde el terminal.

Voy a asumir que ya tienes Git instalado y usas Ubuntu.

.. code-block:: bash

    user@pc:~/$ git clone el-link-de-tu-repositorio-aqui repo
    user@pc:~/$ cd repo

Si haces :code:`ls`:

.. code-block:: bash
    
    tuProyecto/
        +---wsgi.py
        +---setup.py
        *---.openshift/

Allí vas a pegar toda tu aplicación (si tienes una), o vas a crear una nueva.

Ahora viene lo básico. Crear tu virtualenv, activarlo, instalar las dependencias desde tu requirements.txt,
etc, etc, etc...

Luego de que hagas todo esto, coloca esto en tu terminal:

.. code-block:: bash
    
    user@pc:~/repo$ mkdir wsgi
    user@pc:~/repo$ mkdir wsgi/static
    user@pc:~/repo$ touch wsgi/static/.gitkeep

Esto lo usaremos más adelante, es bueno tenerlo listo.

Si has seguido todos los pasos correctamente, deberías tener el siguiente esquema de proyecto:

.. code-block:: bash

    tuProyecto/
    +---wsgi/
    |   +---static/
    |       +---.gitkeep
    +---wsgi.py
    +---setup.py
    +---.openshift/
    +---tuProyectoDjango/
    |   +----__init__.py
    |   +----urls.py
    |   +----settings.py
    |   +----wsgi.py
    +---+tuAppDjango/
        +----__init__.py
        +----models.py
        +----views.py
        +----tests.py
        +----migrations
             +---__init__.py

Ya el proyecto está configurado. Empecemos con el wsgi_.
********************************************************

Primero, debes editar el activho wsgi.py que vino directamente del repositorio de OpenShift con lo siguiente:


¡No olvides de reemplazar **'tuProyectoDjango'** con el nombre de tu proyecto!

.. code-block:: python
    
    #!/usr/bin/python
    import os
    virtenv = os.environ['OPENSHIFT_PYTHON_DIR'] + '/virtenv/'
    virtualenv = os.path.join(virtenv, 'bin/activate_this.py')
    try:
        execfile(virtualenv, dict(__file__=virtualenv))
    except IOError:
        pass

    from tuProyectoDjango.wsgi import application


Crea un archivo que se llame "build" (así, sin extensión), añade los siguientes scripts y guardalos en :code:`.openshift/action_hooks`. Estos van a ser ejecutados cada vez que se haga el deployment de la aplicación.

.. code-block:: bash

    #!/bin/bash
    #this is .openshift/action/hooks/build
    #remember to make it +x so openshift can run it.
    if [ ! -d ${OPENSHIFT_DATA_DIR}media ]; then
        mkdir -p ${OPENSHIFT_DATA_DIR}media
    fi
    ln -snf ${OPENSHIFT_DATA_DIR}media $OPENSHIFT_REPO_DIR/wsgi/static/media

    ######################### end of file

    #!/bin/bash
    #this one is the deploy hook .openshift/action_hooks/deploy
    source $OPENSHIFT_HOMEDIR/python/virtenv/bin/activate
    cd $OPENSHIFT_REPO_DIR
    echo "Executing 'python manage.py migrate'"
    python manage.py migrate
    echo "Executing 'python manage.py collectstatic --noinput'"
    python manage.py collectstatic --noinput

    ########################### end of file

El primero crea la carpeta de "media" en el root del proyecto de OpenShift si esta no existe y crea un enlace simbólico a la ruta :code:`/wsgi/static/media` (recuerdan cuando creamos :code:`/wsgi/static/`?).

El segundo, activa la virtualenv en OpenShift, ejecuta las migraciones y el collectstatic_.

Debes añadir el atributo :code:`+x` a :code:`.openshift/action_hooks/build`, por lo que tienes que ejecutar lo siguiente en el terminal:

.. code-block:: bash

    user@pc:~/repo$ chmod +x .openshift/action_hooks/build

Esto lo vuelve un archivo ejecutable.

Seguimos con las modificaciones en 'settings'
*********************************************
Ya que el wsgi y los hooks están listos, tienes que modificar tu archivo 'settings' para que apunte en donde estan tus archivos 'static', 'media' y 'template':

Todas estas configuraciones están hechas para correr en los sitios predeterminados. Si hiciste algún cambio, refléjalo en tus settings.

¡Recuerda reemplazar **'tuAppDjango'** con el nombre de tu app!

.. code-block:: Python

    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'wsgi', 'static')
    MEDIA_ROOT = os.path.join(BASE_DIR, 'wsgi', 'static', 'media')
    STATICFILES_DIRS = (os.path.join(BASE_DIR, 'tuAppDjango', 'static'),)
    TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'tuAppDjango', 'templates'),)

Para finalizar, tienes que reconocer si estás en OpenShift o no, para que use tu base de datos local o la del servidor.

En tu archivo settings.py, debes agregar:

.. code-block:: Python

    ...

    import os
    BASE_DIR = os.path.dirname(os.path.dirname(__file__))

    # Agregar esto!
    ON_OPENSHIFT = False
    if 'OPENSHIFT_REPO_DIR' in os.environ:
        ON_OPENSHIFT = True
    # Fin

    ...

    ...

    # Database
    # https://docs.djangoproject.com/en/1.7/ref/settings/#databases
    # Agregar esto!
    if ON_OPENSHIFT:
        DEBUG = True
        TEMPLATE_DEBUG = False
        ALLOWED_HOSTS = ['*']
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'tu-base-de-datos-OpenShift',
                'USER': os.getenv('OPENSHIFT_MYSQL_DB_USERNAME'),
                'PASSWORD': os.getenv('OPENSHIFT_MYSQL_DB_PASSWORD'),
                'HOST': os.getenv('OPENSHIFT_MYSQL_DB_HOST'),
                'PORT': os.getenv('OPENSHIFT_MYSQL_DB_PORT'),
                }
        }
    else:
        DEBUG = True
        TEMPLATE_DEBUG = True
        ALLOWED_HOSTS = []
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
    # Fin

    ...

¡Recuerda reemplazar **'tu-base-de-datos-OpenShift'** con el nombre de la base de datos MySQL que te dió OpenShift!

¡Y listo!
---------

Ya todo debería de estar funcionando. en tu terminal escribe:

.. code-block:: bash
    
    user@pc:~/repo$ git status
    # Muestra todos los archivos que se van a agregar al commit

    user@pc:~/repo$ git add .
    user@pc:~/repo$ git commit -m "Initial commit"
    user@pc:~/repo$ git push
    # Por ahí se nos va la app!

Luego que termine el deployment de tu app, si visitas la URL deberías ver tu app corriendo sin ningún problema. Aveces me gusta revisar que la base de datos hizo bien las migraciones. Para eso usas PHPMyAdmin. Si no lo agregaste al comienzo del tutorial, puedes agregar el cartucho ahora.

Espero que hayas podido hacer tu deployment sin problema, y cualquier cosa, ¡No dudes en contactarme!.

Especiales agradecimientos al usuario `Luis Masuelli`_ de Stack-Overflow, que hizo `este maravilloso aporte`_.

Hasta la próxima.

`Parte 1: Preparando nuestro proyecto de Django`_

`Parte 2: Aplicación, Vistas, Modelos, Templates y URLS`_

`Parte 3: Django Admin y Formularios`_

.. _PaaS: https://es.wikipedia.org/wiki/Computaci%C3%B3n_en_la_nube#Plataforma_como_servicio_
.. _Openshift: https://openshift.redhat.com/
.. _configurar tu cuenta: https://developers.openshift.com/en/getting-started-overview.html
.. _collectstatic: https://docs.djangoproject.com/en/1.8/ref/contrib/staticfiles/#collectstatic
.. _wsgi: http://python.org.ar/wiki/WSGI
.. _Luis Masuelli: http://stackoverflow.com/users/1105249/luis-masuelli
.. _este maravilloso aporte: http://stackoverflow.com/questions/26871381/deploying-a-local-django-app-using-openshift/26874375#26874375
.. _`Parte 1: Preparando nuestro proyecto de Django`: {filename}/como-configurar-tu-proyecto-de-django-parte-1.rst
.. _`Parte 2: Aplicación, Vistas, Modelos, Templates y URLS`: {filename}/como-configurar-tu-proyecto-de-django-parte-2.rst
.. _`Parte 3: Django Admin y Formularios`: {filename}/como-configurar-tu-proyecto-de-django-parte-3.rst
¿Cómo hacer un PDF con Python y HTML?
#####################################

:date: 2015-12-21 16:10
:category: Programación
:author: Roger González
:summary: ¿Alguna vez has tenido que hacer un reporte por medio de un PDF en tu aplicación de Python? Aquí puedes aprender como hacerlo, usando **xhtml2pdf**.
:tags: python, pdf, reportes
:status: published

¿Alguna vez has tenido que hacer un reporte por medio de un PDF en tu aplicación de Python? Aquí puedes aprender como hacerlo, usando **xhtml2pdf**.

¿Qué es xhtml2pdf?
------------------
**xhtml2pdf** es un paquete que nos permite la creación de PDF's utilizando HTML. Aquí_ pueden encontrar la documentación completa.

Instalación
+++++++++++
Primero, necesitamos instalar los paquetes necesarios. En el terminal, colocamos:

.. code-block:: bash

    $ sudo apt-get install python-dev libjpeg-dev zlib1g-dev virtualenv

Ya que tenemos todo instalado, creamos una nueva virtualenv y la activamos.

.. code-block:: bash

    $ virtualenv env
    (Se crea la virtualenv)
    $ source env/bin/activate
    (env) $

Como siempre, para desactivar la virtualenv, :code:`deactivate`.

Ya que estamos en nuestra virtualenv, instalamos desde pip:

.. code-block:: bash
    
    (env) $ pip install xhtml2pdf jinja2
    (Se instalan los paquetes)

¡Y eso es todo! Ya podemos empezar a crear nuestro primer PDF.

Creando nuestro primer PDF
--------------------------

Por lo general, hay 3 formas de crear PDF's con xhtml2PDF:

- Con un HTML estático
- Con un HTML dinámico
- Con un framework web (Django, Flask, Pyramid, etc.)

Con un HTML estático
++++++++++++++++++++
Si solo necesitamos generar un reporte de un HTML estático, solo necesitamos lo siguiente:

.. code-block:: python

    from xhtml2pdf import pisa
    import os

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    sourceHtml = open(os.path.join(base_dir, 'ruta/a/nuestro/HTML')).read()
    outputFilename = "test.pdf"

    def convertHtmlToPdf(sourceHtml, outputFilename):
        resultFile = open(outputFilename, "w+b")

        pisaStatus = pisa.CreatePDF(
                sourceHtml,
                dest=resultFile)

        resultFile.close()

        return pisaStatus.err

    if __name__=="__main__":
        pisa.showLogging()
        convertHtmlToPdf(sourceHtml, outputFilename)

Iré explicando poco a poco.

1. Importamos :code:`pisa` (para renderizar los PDF) y :code:`os` (para ubicar nuestro archivo HTML).
2. Usamos :code:`os` para leer nuestro archivo HTML y le asignamos un nombre a nuestro resultado en PDF.
3. Creamos una función llamada :code:`convertHtmlToPdf`, la cual recibe el HTML a renderizar y el nombre del PDF que estamos generando.
4. En la función, creamos el archivo y renderizamos el PDF con :code:`pisa.CreatePDF()`, definiendo nuestro HTML y el archivo PDF creado.
5. Por último, cerramos el archivo, devolvemos los errores (en caso de existir errores) y corremos el :code:`main`

Bastante sencillo. Podemos tener un HTML como este:

.. code-block:: html

    <h1>Hola mundo!</h1>
    <p>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
        consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse
        cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non
        proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    </p>

Y nos devolvería exactamente lo mismo, pero en un PDF.

El problema de esta solución, es que no es automático. Si tenemos un script que genere cierto contenido, tendríamos que modificar el HTML a mano para crear nuestro PDF. Por eso vamos a la segunda forma de crear un PDF

Con un HTML dinámico
++++++++++++++++++++
Para hacer uso de un HTML dinámico, vamos a cargar nuestros templates con jinja2_, el compilador de HTML de Django.

Para eso, modificamos un poco nuestro script original:

.. code-block:: python

    from xhtml2pdf import pisa
    from jinja2 import Template #Nuevo!
    import os

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    sourceHtml = open(os.path.join(base_dir, 'ruta/a/nuestro/HTML')).read()
    outputFilename = "test.pdf"
    data = {'name' : 'roger', 'lastname' : 'gonzalez'} #Nuevo!

    def convertHtmlToPdf(data, sourceHtml, outputFilename): #Nuevo!
        resultFile = open(outputFilename, "w+b")

        template = Template(open(os.path.join(base_dir, sourceHtml)).read()) #Nuevo!
        html  = template.render(data) #Nuevo!

        pisaStatus = pisa.CreatePDF(
                html,
                dest=resultFile)
        resultFile.close()
        return pisaStatus.err

    if __name__=="__main__":
        pisa.showLogging()
        convertHtmlToPdf(data, sourceHtml, outputFilename)

¿Qué hacen las lineas nuevas?

1. Importamos :code:`Template`, que nos permitirá renderizar automáticamente los HTML.
2. Creamos un nuevo diccionario y lo añadimos a la función. jinja2 usa diccionarios para renderizar los datos en HTML.
3. Usamos :code:`Template` para abrir nuestro HTML y posteriormente renderizarlo con nuestro diccionario :code:`data`

Lo mejor de este método es que no es necesario estar pendiente de los HTML. Solo debes hacer una base y utilizar el poderoso sintaxis de jinja2.

Puedes tener este HTML:

.. code-block:: html

    <h1>Hola mundo!</h1>
    <p>{{ name }} {{ lastname }}</p>

El cual devolvería este PDF:

Hola mundo!
+++++++++++
roger gonzalez

Este es el método que más uso, cuando necesito que un script me devuelva un PDF para `mandarlo por correo`_.

Por último, pero no menos importante, el método de framework web.

Con un HTML de un framework web
+++++++++++++++++++++++++++++++
Este método es muy parecido al anterior, a excepción del uso de link callbacks para convertir los URIs de los HTML a rutas absolutas. Para este ejemplo, estoy usando Django.

.. code-block:: python

    import datetime
    import os

    from django.conf import settings
    from django.http import HttpResponse
    from django.template import Context
    from django.template.loader import get_template

    from xhtml2pdf import pisa


    def link_callback(uri, rel):

        sUrl = settings.STATIC_URL      # Typically /static/
        sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL       # Typically /static/media/
        mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

        if not os.path.isfile(path):
                raise Exception(
                    'media URI must start with %s or %s' % (sUrl, mUrl)
                )
        return path

    def generate_pdf(request):

        data = {}
        data['today'] = datetime.date.today()
        data['farmer'] = 'Old MacDonald'
        data['animals'] = [('Cow', 'Moo'), ('Goat', 'Baa'), ('Pig', 'Oink')]

        template = get_template('lyrics/oldmacdonald.html')
        html = template.render(Context(data))

        f = open(os.path.join(settings.MEDIA_ROOT, 'test.pdf'), "w+b")
        pisaStatus = pisa.CreatePDF(html, dest=f, link_callback=link_callback)

        file.seek(0)
        pdf = file.read()
        file.close()
        return HttpResponse(pdf, mimetype='application/pdf')

Más de lo mismo, lo único que cambia es que al final devuelve el PDF por medio de un :code:`HttpResponse` de Django.

¡Eso es todo!
-------------
Con este tutorial corto, pero informativo, pudimos aprender como usar xhtml2pdf para generar un reporte en PDF utilizando un HTML como base. Pero eso no es todo. xhtml2pdf tiene algunas limitaciones a la hora de renderizar HTML. Puedes conocerlas todas revisando la documentación_.

¡Hasta la próxima!

.. _Aquí: https://github.com/xhtml2pdf/xhtml2pdf/blob/master/doc/usage.rst
.. _jinja2: http://jinja.pocoo.org/docs/dev/
.. _mandarlo por correo: {filename}/enviar-un-mail-con-mailx.rst
.. _documentación: https://github.com/xhtml2pdf/xhtml2pdf/blob/master/doc/usage.rst
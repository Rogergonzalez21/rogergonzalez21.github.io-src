¿Cómo configurar tu primer proyecto de Django? Parte III
########################################################

:date: 2015-11-24 15:31
:category: Programación
:slug: como-configurar-tu-primer-proyecto-de-django-parte-III
:author: Roger González
:summary: Es hora de hacer tu primera aplicación web. En este pequeño tutorial, te voy a enseñar a utilizar el Django Admin y hacer formularios en Django.
:tags: django, python
:status: published

Siguiendo desde el `último tutorial`_, hoy vamos a usar el Django Admin y vamos a hacer nuestro primer formulario.

¿Qué es el Django admin?
------------------------
El `Django admin`_ es uno de los mejores elementos que tiene Django para el desarrollo web. Django automáticamente trae una interfaz de administrador, que lee tus modelos y te da opciones para añadir, editar y eliminar registros en tu base de datos. ¿Bastante útil, no?.

¿Cómo accedo al Django admin?
-----------------------------
Con nuestra **aplicación corriendo**, vamos al navegador a la dirección :code:`localhost:8000/admin`, y vamos a conseguir esto:

.. image:: {filename}/images/django_tutorial/django-admin-login.png
    :alt: django admin

Para entrar, usamos los datos del superusuario, que creamos en el tutorial anterior. Al entrar, nos conseguimos con el panel de administración de Django, pero con un problema: **no hay modelos para editar**.

Para registrar tus modelos, tienes que añadir lo siguiente en :code:`app_test/admin.py`:

.. code-block:: python

    from django.contrib import admin
    from app_test.models import Person

    admin.site.register(Person)

Si actualizamos en el navegador, veremos nuestro modelo listo para añadir, editar o eliminar registros.

.. image:: {filename}/images/django_tutorial/django-admin-model-registration.png
    :alt: django admin model registration

Si hacemos click en "Add" en el apartado de "Persons", podemos añadir a una persona.

.. image:: {filename}/images/django_tutorial/django-admin-add-person.png
    :alt: django admin model registration

Finalmente, si volvemos a :code:`localhost:8000/index`, vamos a ver a nuestra persona recientemente creada.

.. image:: {filename}/images/django_tutorial/first-person.png
    :alt: primera persona

Pero espera, esto no es para nada práctico
------------------------------------------
En lo más mínimo esto es práctico. Si estamos haciendo una aplicación para el público, es imposible pedirle a cada persona que la quiera usar que entre en el panel de administración para registrarse. Entonces, ¿Qué usamos para añadir nuevos registros a la base de datos? Claro que si, campeon. Un formulario.

Creando nuestro primer formulario
---------------------------------
Primero, tenemos que crear el archivo :code:`app_test/forms.py`. Allí, vamos a colocar lo siguiente:

.. code-block:: python

    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    from django import forms
    from app_test.models import Person

    class PersonForm(forms.ModelForm):
        name = forms.CharField(max_length=120, label="Nombre")
        email = forms.EmailField(max_length=120, label='Correo electrónico')
        phone_num = forms.CharField(max_length=20, label='Teléfono')
        address = forms.CharField(max_length=120, label="Dirección")

        class Meta:
            model = Person
            fields = ('name', 'email', 'phone_num', 'address')

Voy a explicar paso a paso lo que está pasando.

- Primero hacemos los imports. Importamos :code:`forms` y nuestro modelo, :code:`Person`.
- Creamos una clase llamada "PersonForm" que hereda de :code:`forms.ModelForm`. En Django, los formularios son Clases.
- Creamos cada uno de los campos, exactamente como en los modelos, pero esta vez viniendo de "Forms".
- Usamos la subclase :code:`Meta` para definir que estamos usando un modelo, y cuáles de los campos vamos a llenar.

¡Y listo! Ya tenemos nuestro formulario listo, y podemos usarlo en nuestras vistas.

En :code:`app_test/views.py`, creamos la siguiente vista:

.. code-block:: python
    
    from django.shortcuts import render, redirect
    from app_test.forms import PersonForm

    def index(request):
    # ...

    def addPerson(request):
        if request.method == 'POST':
            form = PersonForm(request.POST)
            if form.is_valid():
                form.save(commit=True)
                return redirect(index)
            else:
                print form.errors
        else:
            form = PersonForm()
        return render(request, 'add_person.html', {'form': form})

En esta vista:

- Importamos :code:`redirect`, para manejar las redirecciones de las vistas.
- Creamos la vista :code:`addPerson`, que va a manejar nuestro formulario.
- En la vista, chequeamos si se hizo una petición POST (si no sabes lo que es POST o las peticiones HTTP, puedes leerlo aquí_).

  + Si es un POST, chequea si el formulario es válido. Si es válido, guarda en la base de datos y redirecciona a :code:`index`, de lo contrario, devuelve los errores del formulario.
  + Si no es POST, entonces devuelve el formulario vacío.

Seguidamente, creamos el template que muestre el formulario. En :code:`app_test/templates/add_person.html`:

.. code-block:: html

    <!DOCTYPE html>
    <html>
        <head>
            <title>Añadir personas</title>
        </head>
        <body>
            <h1>Añadir personas</h1>
            <form method="post" action="">
                {% csrf_token %}
                {{ form.as_p }}
                <button type="submit">Guardar</button>
                <a href="{% url 'index' %}">Volver</a>
            </form>
        </body>
    </html>

Aquí hacemos uso del sistema de templates de Django, Jinja2_. Con :code:`{% url 'index' %}`, nos aseguramos que siempre ese link se dirija al URL con nombre :code:`index`.

Finalmente, colocamos la nueva URL que lleva hacia la vista. En :code:`app_test/urls.py`

.. code-block:: python
    
    # ...

    urlpatterns = patterns('',
        url(r'^index$', views.index, name='index'),
        url(r'^index/addPerson/$', views.addPerson, name='addPerson'), # <--- Agregar esta linea!

    )

Si vamos a :code:`localhost:8000/index/addPerson`, podemos ver nuestro formulario funcionando sin problemas. Si lo llenamos con datos y hacemos click en "Guardar", volveremos a la página principal y podremos ver nuestro nuevo registro.

.. image:: {filename}/images/django_tutorial/form1.png
    :alt: form

.. image:: {filename}/images/django_tutorial/form2.png
    :alt: form2

Para un mejor flujo, añadimos un link a "Añadir personas" desde la página principal. En :code:`app_test/templates/index.html`:

.. code-block:: html

        <!--Justo despues del cierre de la tabla-->
        </table>
        <a href="{% url 'addPerson' %}">Añadir persona</a>
    </body>

¡Y eso es todo!
---------------
Ahora tu proyecto debe verse así_. 

Aún falta mucho por cubrir, pero no hay tanto tiempo. Aún se le podría agregar `archivos estáticos`_, como hojas de estilo CSS, o scripts en JavaScript, y muchísimas otras cosas mas. Recuerda que el objetivo principal de este tutorial es demostrar lo sencillo que es crear una aplicación con Django.

En un próximo post, haré un tutorial para hacer deploy de tu aplicación de Django en OpenShift.

¡Hasta la próxima!

`Parte 1: Preparando nuestro proyecto de Django`_

`Parte 2: Aplicación, Vistas, Modelos, Templates y URLS`_


.. _último tutorial: {filename}/como-configurar-tu-proyecto-de-django-parte-2.rst
.. _Django admin: https://docs.djangoproject.com/en/1.8/ref/contrib/admin/
.. _aquí: https://es.wikipedia.org/wiki/Hypertext_Transfer_Protocol#M.C3.A9todos_de_petici.C3.B3n
.. _Jinja2: http://jinja.pocoo.org/docs/dev/
.. _archivos estáticos: https://docs.djangoproject.com/en/1.8/howto/static-files/
.. _así: https://github.com/Rogergonzalez21/django-tutorial/tree/bc9346efde23714d360e1170c18268535ed98871
.. _`Parte 1: Preparando nuestro proyecto de Django`: {filename}/como-configurar-tu-proyecto-de-django-parte-1.rst
.. _`Parte 2: Aplicación, Vistas, Modelos, Templates y URLS`: {filename}/como-configurar-tu-proyecto-de-django-parte-2.rst

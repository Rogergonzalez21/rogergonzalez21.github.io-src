¿Cómo enviar un mail desde el terminal con mailx?
#################################################

:date: 2015-10-30 15:59
:category: Tecnología
:slug: enviar-un-mail-con-mailx
:author: Roger González
:summary: Hoy vengo con un tutorial un poco más corto y directo al grano. **¿Cómo envío un correo por bash?**
:tags: mail, mailx, bash, script, tutorial
:status: published

Hoy vengo con un tutorial un poco más corto y directo al grano. **¿Cómo envío un correo por bash?**.

La respuesta, mailx

¿Qué es mailx?
--------------
mailx_ es un programa para enviar y recibir correo. También, es una versión mejorada de 'mail' en Unix. **mailx** es una herramienta muy útil para mandar correos por bash, ya que podemos **usarlo en un script** :code:`.sh`

Su instalación es muy sencilla:

.. code-block:: bash

    user@pc:~$ sudo apt-get install mailutils

    # Cuando nos salga una ventana preguntando la configuración, seleccionamos la segunda

Ya que tenemos mailx instalado, podemos hacer uso de ella.

Primeros pasos con mailx
------------------------

mailx es muy sencillo de utilizar. Podemos hacerlo de esta forma:

.. code-block:: bash

    user@pc:~$ mailx -s "Asunto del mail" "correo_destinatario@servidor.com"
    Cc: correo_de_copia@servidor.com
    Hola! Soy un correo de mailx!

    # Presionamos Cntrl + D para enviar el correo

¿Qué pasa aquí?
***************

Primero, estamos ejecutando :code:`mailx` con el parámetro :code:`-s`, que permite añadir un asunto al mail ("Asunto del mail"), y por último, el correo destinatario ("correo_destinatario@servidor.com").

Cuando presionamos enter, mailx nos da opciones de agregar un 'Cc' (Con copia) y el cuerpo del correo.

Pero esto no es muy automático... ¿Cómo puedo usarlo en un script?
******************************************************************

Hay muchas formas de usarlo en un script, pero yo uso solo 2.

La primera, solo envía un correo con "Asunto", pero sin cuerpo:

.. code-block:: bash

    user@pc:~$ mailx -s "Asunto del mail" "correo_destinatario@servidor.com" < /dev/null

Esta ejecución de mailx nos va a enviar un correo con asunto "Asunto del mail". Así de sencillo.

Si queremos que nos mande un correo con asunto y cuerpo, podemos usar:

.. code-block:: bash

    user@pc:~$ mailx -s "Asunto del mail" "correo_destinatario@servidor.com" < cuerpo-del-mensaje.txt

Dónde 'cuerpo-del-mensaje.txt' sea un archivo de texto plano que contenga el mensaje que quieres que sea enviado.

¡Eso es todo!
-------------

Usar mailx es muy util para multiples cosas. Yo lo uso cuando programo un `script con cron`_ y **quiero que me avise cuando se ejecute y cuando termine**. ¿Para qué lo usarías tu?

Hasta la próxima.

.. _mailx: https://es.wikipedia.org/wiki/Mailx
.. _script con cron: {filename}/como-descargar-ftp-wget-script.rst

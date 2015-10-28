¿Cómo enviar un mail desde el terminal con Mailx?
#################################################

:date: 2015-10-24 17:20
:category: Programación
:slug: enviar-un-mail-con-mailx
:author: Roger González
:summary: Hoy vengo con un tutorial un poco mas corto y directo al grano. **¿Cómo envío un correo por bash?**
:tags: mail, mailx, tutorial, bash, script

Hoy vengo con un tutorial un poco mas corto y directo al grano. **¿Cómo envío un correo por bash?**.

La respuesta, mailx

¿Qué es mailx?
--------------
mailx_ es un programa para enviar y recibir correo. Tambien, es una versión mejorada de 'mail' en Unix. **mailx** es una herramienta muy util para mandar correos por bash, ya que podemos **usarlo en un script :code:`.sh`**

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

.. _mailx: https://es.wikipedia.org/wiki/Mailx
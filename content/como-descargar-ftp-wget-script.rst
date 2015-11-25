¿Cómo descargar automáticamente de un FTP usando wget y cron?
#############################################################

:date: 2015-10-30 16:10
:category: Tecnología
:slug: descargar-ftp-usando-wget-y-cron
:author: Roger González
:summary: Hace unos días me mandaron a configurar una PC prehistorica para hacer respaldos automáticos de un servidor web. Una antigua Intel Dual Core con 2GB de Ram y un HDD de 320GB. Aprende a programar un script de bash que descargue la información de un FTP vía wget con cron.
:tags: wget, cron, ftp, descargar, script, bash, tutorial
:status: published

Hace unos días me mandaron a configurar una PC prehistorica para hacer respaldos automáticos de un servidor web. Una antigua Intel Dual Core con 2GB de Ram y un HDD de 320GB (los respaldos no son tan pesados, 8GB a lo sumo).

Lo mejor del proyecto: Me dieron total libertad. Por eso, decidí instalar `Lubuntu 15.10`_ (recien salido del horno) en contra del equipo de Windowseros TI que hay en la empresa.

Ya que la PC tenía Lubuntu, me dispuse a buscar opciones para descargar por FTP, y me consigo con wget, la herramienta de descargas que viene preinstalada en todas las distro Debian-based.

¿Qué es wget?
-------------
wget_ es una herramienta libre que permite la descarga de contenidos desde servidores web de una forma simple. Se caracteriza por ser muy **robusta** desde su lanzamiento en 1996 (justo en el boom de popularidad de la web).

¡Ya tengo la herramienta para hacer los backups! y lo mejor es que **viene incluida en la distribución**, por lo que no tengo que instalar paquetes externos.

Ahora, para programar las descargas me propuse usar **cron**.

¿Qué es cron?
-------------
cron_ es un demonio_ que ejecuta procesos o scripts_ a cierto minuto, hora, dia, semana o mes.

Ya que sabía lo que tenía que hacer, solo faltaba ponerme manos a la obra.

Manos a la obra
---------------
Primero, tenía que crear el script de bash_ :code:`(.sh)` que se iba a ejecutar. El script tiene que:

- Acceder a la carpeta de backups
- Crear una carpeta con la fecha del día del backup
- Descargar todo del FTP

Ok, ¡Empecemos!

.. code-block:: bash
    
    #! /bin/bash

    today=`date +"%d_%m_%Y"`
    
    cd ~/backups
    mkdir $today

    cd $today
    user@pc:~$ mailx -s "¡Backup comenzado!" "correo_destinatario@servidor.com" < /dev/null
    wget --timeout 20 -m -nH --user "ftpuser" --password "ftppassword" ftp://ftpserver.com
    user@pc:~$ mailx -s "¡Backup terminado!" "correo_destinatario@servidor.com" < /dev/null

¡No te asustes! Voy a explicar paso a paso lo que hace cada uno de los comandos.

- :code:`#! /bin/bash`: Sirve para indicar que lo que viene es un script de bash.
- :code:`today=`date +"%d_%m_%Y"``: Guarda la fecha de hoy, en formato 'dia_mes_Año', en la variable 'today'.
- :code:`cd ~/backups`:  Entra a una carpeta llamada 'backups', que voy a crear más adelante.
- :code:`mkdir $today`: Crea una carpeta con el día de hoy ('dia_mes_Año').
- :code:`cd $today`: Accede a la carpeta creada.
- :code:`mailx -s`: mailx es un programa que se usa para mandar correos. En esta_ entrada puedes saber mas de eso.

Aquí me voy a detener un poco y explicar pausadamente.

- :code:`wget --timeout 20 -m -nh`: Ejecuta wget con los parámetros:

  + :code:`--timeout 20`, para que reintente luego de 20 segundos de inactividad.
  + :code:`-m` para especificar que está haciendo un mirror.
  + :code:`-nH`, que especifica que no cree una subcarpeta, sino que descargue todo en donde está.

- :code:`--user "ftpuser" --password "ftppassword" ftp://ftpserver.com`: Son los datos de conexión de nuestro FTP. Debemos reemplazar cada uno de los campos con nuestros propios datos.

Ya que tenemos nuestro script, configuremos cron
------------------------------------------------

La configuración de cron es muchisimo mas sencilla. En nuestro terminal colocamos:

.. code-block:: bash
    
    crontab -e

(Aveces advierte que no tienes un editor predeterminado. Elegimos 'nano' o el de nuestra preferencia).

Se va a abrir nuestro archivo crontab. Si vamos a la última parte, veremos que podemos agregar nuevas instrucciones.

Los formatos de las instrucciones de crontab son las siguientes:

.. code-block:: bash

    a b c d e /ruta/del/script.sh

Donde:

- a = minuto (0-59)
- b = hora (0-23, 0 = medianoche)
- c = dia (1-31)
- d = mes (1-12)
- e = dia de la semana (0,6, 0 = domingo)

También podemos colocar '*' en día, mes y día de la semana, para especificar "cualquiera".

Con esta información, construí mi crontab:

.. code-block:: bash

    30 17 * * 2,4 /scripts/backup.sh

El script será ejecutado cada **martes** y **jueves**, a las **5:30PM**. Aquí_ tienes más información para crear tus propios cron.

Conclusión
----------

wget y cron son herramientas poderosas que vienen con nuestros sistemas operativos Linux, que con los conocimientos correctos pueden ser nuestras mejores amigas.

cron puede ser usado para muchas cosas de automatización, y wget tiene muchísimas más opciones además de descargar de un FTP. Te invito a leer cada uno de sus manuales (:code:`man wget` y :code:`man cron`).

Hasta la próxima.


.. _Lubuntu 15.10: http://lubuntu.net/
.. _wget: https://es.wikipedia.org/wiki/GNU_Wget
.. _cron: https://es.wikipedia.org/wiki/Cron_%28Unix%29
.. _demonio: https://es.wikipedia.org/wiki/Demonio_%28inform%C3%A1tica%29
.. _scripts: https://es.wikipedia.org/wiki/Script
.. _bash: https://es.wikipedia.org/wiki/Bash
.. _Aquí: https://help.ubuntu.com/community/CronHowto
.. _esta: {filename}/enviar-un-mail-con-mailx.rst
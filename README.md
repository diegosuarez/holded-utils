# holded-utils
Cosas de utilidad para Holded

# Instalacion:
## Requisitos:
* Selenium: `pip install selenium`
* chrome-driver: `apt install chromedriver`
## Ejecucion:
* Cambiar las variables arriba del todo del script.
* Para mas comodidad, establecer en un cron con los horarios que se desean "fichar", con un crontab como el que sigue. Ojo con la ruta del binario de python.

```
# m h  dom mon dow   command
# Antes de comer L-J
55 8 * * 1-4 /opt/python/bin/python /home/diego/ficheitor.py in
0 14 * * 1-4 /opt/python/bin/python /home/diego/ficheitor.py out 
# Despues de comer L-J
0 15 * * 1-4 /opt/python/bin/python /home/diego/ficheitor.py in
0 18 * * 1-4 /opt/python/bin/python /home/diego/ficheitor.py out 
# Jornada continua
55 7 * * 5 /opt/python/bin/python /home/diego/ficheitor.py in
0 15 * * 5 /opt/python/bin/python /home/diego/ficheitor.py out 
```

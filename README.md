# Tarea 3
## Algoritmos probabilísticos

### Setear el entorno virutal
#### En Windows
Basta con poner `pip install virtualenv` en la cmd y luego en un directorio `virtualenv .venv` y luego ejecutar `.venv/scripts/activate`
#### En linux y Mac
Ejectuar `python3 -m venv venv` y luego `source ./venv/bin/activate` 

### Instalar librerías
Se añadió un archivo *requirements.txt* en el que se muestran las librerías utilizadas, dichas librerías son las que estaban instaladas en el entorno virtual a la hora de ejecutar todo. Para instalarlas:
```
pip install -r requirements.txt
```

### Compilar
Para ejecutar los test de tiempo y generar el gráfico:
```
python3 testTime.py
```
Para ejecutar los test variando *m* y *k*:
```
python3 testratio.py
```

Lo anterior estando en la carpeta que contiene todos los códigos.

[Informe en Latex (lectura)](https://www.overleaf.com/read/nxwqhznpzmyc)

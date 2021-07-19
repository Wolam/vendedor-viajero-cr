# vendedor-viajero-cr #

Investigación sobre algoritmos probabilísticos para el problema del vendedor viajero con ciudades nacionales.

## Entorno virtual ##

Este proyecto requiere `Python 3`. Se sugiere utilizar un entorno virtual como paso previo a la instalación

```bash
python3 -m venv .venv
```

Para luego realizar la activación del mismo

``` bash
source .venv/bin/activate
```

## Instalación ##


Para instalar las dependencias correr:

```bash
pip3 install -r requirements.txt
```

## Pruebas ##

Para correr todas las pruebas automatizadas:

```bash
pytest
```

Para correr solo algunas pruebas automatizadas, por ejemplo todas las pruebas cuyo nombre inicia con `test_validar`:

```bash
pytest -v -k "test_validar" dominio_tsp_test.py
```


## Autores ##
---
* Diego Acuña @DAC125
* Joseph Valenciano @JosephV27
* Ricardo Murillo @ricardomj0499
* Ronald Esquivel @ITCRStevenLPZ
* Wilhelm Carstens @wolam


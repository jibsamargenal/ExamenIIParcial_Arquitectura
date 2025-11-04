# Monitoreo del Sistema con Django y Psutil

## Integrantes
* Jean Carlos Tejada Machado 202420010591
* Jibsam Alexander Argeñal Arias 202410010006
* Kricza Ruby Zelaya Hernández  202410010299

## Descripcion
Esta aplicación permite al usuario observar en tiempo real el uso del CPU, memoria
y disco duro. Además se ofrece información sobre el sistema como su tipo y versión
del sistema operativo y el número de núcleos del CPU.

El proyecto está construido con Django que nos permite brindar información dinámica
a la aplicación web. La información del sistema es obtenido por la librería Psutil.
Utilizamos los metodos de la librería en el *view* para guardar la información y
retornarla a la página web por medio de una API. Luego definimos la estructura de
la página web con HTML en el *template*. Se incluye un script que permite actualizar
el DOM con nueva información constantemente. Para el diseño de la página, utilizamos
la librería Bootstrap que nos brinda componentes como tarjetas para estructurar
mejor la información. Bootstrap también ofrece un sistema de cuadricula que permite
que la página se adapte a distintos tamaños de dispositivos.

## Instrucciones
1. Asegúrese de tener Python instalado en su máquina.
2. Clone el repositorio en su disco.
3. Acceda al directorio base del repositorio.
4. En la terminal, ejecute el comando ```python -m venv venv``` para crear un entorno virtual en Python.
5. Ejecute el comando ```source venv/bin/activate``` en Mac o ```venv\Scripts\Activate``` en Windows para activar el entorno virtual.
6. Ejecute el comando ```pip install -r requirements.txt``` para descargar las dependencias del proyecto.
7. En el directorio base, ejecute ```python manage.py runserver``` para correr el servidor web de Django.

## Componentes
### views.py
Aquí se importa la librería psutil para utilizar métodos como ```virtual_memory``` o ```disk_usage``` 
dentro de la función ```obtener_metricas del_sistema``` dondese obtiene información del sistema. Los 
datos se retornan como un archivo JSON por medio de la función```api_metricas_del_sistema```. La 
función ```dashboard_sistema``` renderiza el template para proveer laestructura en HTML de la página.

### templates/sistema/dashboard.html
El template recibe los datos de la API para actualizar el DOM con la información del sistema actual. La información
se encuentra dentro de divs que utilizan las clases de Bootstrap como card y container para mejorar visualmente
la aplicación y facilitar la información.

## urls.py
Aquí se definen las rutas para acceder al template y la API desde el navegador web.

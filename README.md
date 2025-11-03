# Monitoreo del Sistema con Django y Psutil

Esta aplicación utiliza el framework Django para crear una aplicación web que permita mostrar
las métricas sobre el uso del sistema en tiempo real. Utilizamos la libreria "psutil" para 
obtener esta informacion que se carga en el view. Los datos se traducen a formato JSON para
poder ser compartidos por medio de un API a las plantillas de HTML y CSS.

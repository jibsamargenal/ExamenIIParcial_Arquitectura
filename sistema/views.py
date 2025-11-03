import platform
import psutil
from django.shortcuts import render
from django.http import JsonResponse


def obtener_metricas_del_sistema():
    # Uso del CPU
    porcentaje_cpu = psutil.cpu_percent(interval=1)

    # Uso de Memoria
    informacion_memoria = psutil.virtual_memory()
    total_memoria_en_gb = round(informacion_memoria.total / (1024**3), 2)
    memoria_usada_en_gb = round(informacion_memoria.used / (1024**3), 2)
    porcentaje_memoria = informacion_memoria.percent

    # Uso del disco para la partición root
    try:
        informacion_disco = psutil.disk_usage('/')
        total_disco_en_gb = round(disk_info.total / (1024**3), 2)
        disco_usado_en_gb = round(disk_info.used / (1024**3), 2)
        porcentaje_disco = disk_info.percent
    except Exception:
        # Fallback en caso de no tener una partición root simple
        total_disco_en_gb, disco_usado_en_gb, porcentaje_disco = 'N/A', 'N/A', 'N/A'
    
    # Nucleos del CPU
    nucleos_cpu = psutil.cpu_count(logical=True)
    
    # Información del Sistema Operativo
    sistema_os = platform.system()
    lanzamiento_os = platform.release()
    version_os = platform.version()
    
    
    return {
        # Uso
        'uso_cpu': porcentaje_cpu,
        'uso_memoria': porcentaje_memoria,
        'uso_disco': porcentaje_disco,
        
        # Detalles
        'nucleos_cpu': nucleos_cpu,
        'total_memoria_en_gb': total_memoria_en_gb,
        'memoria_usada_en_gb': memoria_usada_en_gb,
        'total_disco_en_gb': total_disco_en_gb,
        'disco_usado_en_gb': disco_usado_en_gb,
        'informacion_sistema': f"{sistema_os} {lanzamiento_os} ({version_os})",
    }


def dashboard_sistema(request):
    """Vista para renderizar el dashboard del sistema."""
    context = obtener_metricas_del_sistema()
    return render(request, 'sistema/dashboard.html', context)

def api_metricas_sistema(request):
    """Endpoint del API para obtener las métricas del sistema en formato JSON."""
    stats = obtener_metricas_del_sistema()
    return JsonResponse(stats)
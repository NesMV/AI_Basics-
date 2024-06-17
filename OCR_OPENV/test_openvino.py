from openvino.runtime import Core

# Inicializar el motor de inferencia
core = Core()

# Imprimir los dispositivos disponibles
print("Dispositivos disponibles:", core.available_devices)

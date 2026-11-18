# TP N° 4 - Trabajo Práctico Integrador (Redes de Computadoras - 3643)

Repositorio del **Grupo 06** con los scripts en Python para interactuar con la API REST del Network Controller de Cisco Packet Tracer.

## Descripción de los scripts (carpeta `src/`)

* **`01_get-ticket.py`:** Envía las credenciales al endpoint `/api/v1/ticket` mediante una petición `POST` para obtener el token de autenticación (`serviceTicket`).
* **`02_get-network-device.py`:** Consulta la lista de dispositivos de red descubiertos por el controlador (`GET /api/v1/network-device`) y muestra su hostname, plataforma e IP de administración.
* **`03_get-host.py`:** Consulta los hosts conectados a la red (`GET /api/v1/host`) y lista su nombre, dirección IP, MAC e interfaz asociada.
* **`04_tabulate.py`:** Automatiza la obtención del ticket y consulta tanto los dispositivos de red como los hosts, mostrando ambos resultados ordenados en tablas por consola mediante la librería `tabulate`.
* **`05_inventario.py` (Script propio del grupo):** Se autentica automáticamente contra el Network Controller, consulta la lista unificada de dispositivos de red y hosts (manejando la excepción del router ISP sin acceso SSH) y exporta todo el inventario a un archivo `inventario_red.csv`.

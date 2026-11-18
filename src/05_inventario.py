import csv
import json
import requests

base_url = "http://localhost:58000/api/v1"

# 1. Obtener el ticket de autenticación automáticamente
headers = {"Content-Type": "application/json"}
body = {"username": "cisco", "password": "class"}
resp_ticket = requests.post(f"{base_url}/ticket", data=json.dumps(body), headers=headers)

ticket = resp_ticket.json()["response"]["serviceTicket"]
auth_headers = {"X-Auth-Token": ticket}

# 2. Consultar dispositivos de red y hosts
dispositivos = requests.get(f"{base_url}/network-device", headers=auth_headers).json()["response"]
hosts = requests.get(f"{base_url}/host", headers=auth_headers).json()["response"]

# 3. Exportar todo a un archivo CSV unificado
nombre_archivo = "inventario_red.csv"
with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Categoria", "Nombre", "Modelo / Tipo", "IP", "Estado / MAC"])

    for dev in dispositivos:
        writer.writerow([
            "Dispositivo de Red",
            dev.get("hostname", "ISP (Wrong credential)"),
            dev.get("platformId", "N/A"),
            dev.get("managementIpAddress", "N/A"),
            dev.get("reachabilityStatus", "N/A")
        ])

    for host in hosts:
        writer.writerow([
            "Host",
            host.get("hostName", "N/A"),
            host.get("hostType", "N/A"),
            host.get("hostIp", "N/A"),
            host.get("hostMac", "N/A")
        ])

print(f"Inventario exportado correctamente en '{nombre_archivo}'.")
print(f"Total procesado: {len(dispositivos)} dispositivos de red y {len(hosts)} hosts.")
### Sistema Cliente-Servidor para Operaciones Matemáticas

## Descripción
Este proyecto implementa un sistema cliente-servidor que permite a múltiples clientes conectarse simultáneamente para realizar operaciones matemáticas básicas (suma, resta, multiplicación y división). El servidor procesa las solicitudes y devuelve los resultados a los clientes correspondientes.

## Características principales
🚀 Soporte para múltiples clientes concurrentes mediante threads

➕ Operaciones soportadas: suma, resta, multiplicación y división

🛡️ Manejo robusto de errores (operaciones inválidas, división por cero, etc.)

🔄 Protocolo de comunicación simple basado en texto UTF-8

⚡ Conexiones persistentes para múltiples operaciones por sesión

## Requisitos
Python 3.x

No se requieren librerías adicionales (usa solo módulos estándar)

##Instalación
Clona el repositorio o descarga los archivos:

git clone https://github.com/tu-usuario/math-server-client.git
cd math-server-client

## Uso
Iniciar el servidor

python server.py

El servidor se iniciará por defecto en localhost:12345. Puedes modificar estos parámetros editando el código del servidor.

Conectar un cliente
python client.py [host] [port]

Ejemplo para conectar al servidor por defecto:
python client.py

Ejemplo para conectar a un servidor especifico:
python client.py 192.168.1.10 54321

## Operaciones soportadas:

sumar 5 3

restar 10 4

multiplicar 7 8

dividir 20 5

## Para desconectarte, escribe:
salir

## Configuración
Puedes modificar los siguientes parámetros editando los archivos correspondientes:

server.py:

host: Dirección IP del servidor (por defecto 'localhost')

port: Puerto del servidor (por defecto 12345)

max_clients: Número máximo de clientes simultáneos (por defecto 5)

client.py:

Los parámetros de conexión pueden especificarse como argumentos al ejecutar

## Limitaciones conocidas
No soporta operaciones matemáticas avanzadas (potencias, raíces, etc.)

No incluye autenticación de clientes

No registra logs de operaciones

## Licencia
Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo LICENSE para más información.

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request con tus sugerencias.

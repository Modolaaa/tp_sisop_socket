import socket
import threading

class MathServer:
    def __init__(self, host='localhost', port=12345, max_clients=5):
        self.host = host
        self.port = port
        self.max_clients = max_clients
        self.server_socket = None
        self.running = False
        self.client_threads = []

    def handle_client(self, client_socket, client_address):
        print(f"Conexión establecida con {client_address}")
        try:
            while True:
                data = client_socket.recv(1024).decode('utf-8').strip()
                if not data:
                    break

                if data.lower() == 'salir':
                    print(f"Cliente {client_address} solicitó salir")
                    break

                try:
                    response = self.process_operation(data)
                except Exception as e:
                    response = f"Error: {str(e)}"

                client_socket.sendall(f"{response}\n".encode('utf-8'))
        except ConnectionResetError:
            print(f"Cliente {client_address} se desconectó abruptamente")
        finally:
            client_socket.close()
            print(f"Conexión con {client_address} cerrada")

    def process_operation(self, data):
        parts = data.split()
        if len(parts) != 3:
            raise ValueError("Formato incorrecto. Uso: <operación> <operando1> <operando2>")

        operation = parts[0].lower()
        try:
            a = float(parts[1])
            b = float(parts[2])
        except ValueError:
            raise ValueError("Los operandos deben ser números válidos")

        if operation == 'sumar':
            result = a + b
        elif operation == 'restar':
            result = a - b
        elif operation == 'multiplicar':
            result = a * b
        elif operation == 'dividir':
            if b == 0:
                raise ValueError("División por cero no permitida")
            result = a / b
        else:
            raise ValueError(f"Operación no soportada: {operation}. Operaciones válidas: sumar, restar, multiplicar, dividir")

        return f"Resultado: {result}"

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(self.max_clients)
        self.running = True

        print(f"Servidor iniciado en {self.host}:{self.port}. Esperando conexiones...")

        try:
            while self.running:
                client_socket, client_address = self.server_socket.accept()
                if len(self.client_threads) >= self.max_clients:
                    client_socket.sendall("Error: Servidor ocupado. Intente más tarde\n".encode('utf-8'))
                    client_socket.close()
                    continue

                client_thread = threading.Thread(
                    target=self.handle_client,
                    args=(client_socket, client_address),
                    daemon=True
                )
                client_thread.start()
                self.client_threads.append(client_thread)
                print(f"Clientes conectados: {threading.active_count() - 1}")

        except KeyboardInterrupt:
            print("\nServidor detenido por el usuario")
        finally:
            self.stop()

    def stop(self):
        self.running = False
        if self.server_socket:
            self.server_socket.close()
        print("Servidor detenido")

if __name__ == "__main__":
    server = MathServer()
    server.start()
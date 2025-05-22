import socket
import sys

class MathClient:
    def __init__(self, host='localhost', port=12345):
        self.host = host
        self.port = port
        self.socket = None

    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            print(f"Conectado al servidor {self.host}:{self.port}")
            print("Ingrese operaciones en el formato: <operación> <operando1> <operando2>")
            print("Operaciones soportadas: sumar, restar, multiplicar, dividir")
            print("Escriba 'salir' para terminar la conexión")
            self.run()
        except ConnectionRefusedError:
            print(f"No se pudo conectar al servidor {self.host}:{self.port}")
        except Exception as e:
            print(f"Error: {str(e)}")
        finally:
            if self.socket:
                self.socket.close()

    def run(self):
        while True:
            try:
                message = input("> ")
                if not message:
                    continue

                self.socket.sendall(f"{message}\n".encode('utf-8'))

                if message.lower() == 'salir':
                    print("Desconectando del servidor...")
                    break

                response = self.socket.recv(1024).decode('utf-8').strip()
                print(response)

            except KeyboardInterrupt:
                print("\nDesconectando del servidor...")
                self.socket.sendall("salir\n".encode('utf-8'))
                break
            except ConnectionResetError:
                print("El servidor cerró la conexión abruptamente")
                break
            except Exception as e:
                print(f"Error: {str(e)}")
                break

if __name__ == "__main__":
    if len(sys.argv) == 3:
        host = sys.argv[1]
        port = int(sys.argv[2])
    else:
        host = 'localhost'
        port = 12345

    client = MathClient(host, port)
    client.connect()
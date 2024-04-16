import socket
import random
import time

host = 'localhost'
port = 9999

status_codes = [200, 201, 400, 404, 500, 503]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()

    print(f"Servidor iniciado em {host}:{port}. Aguardando conexões...")
    conn, addr = s.accept()
    with conn:
        print(f"Conectado por {addr}")
        while True:
            status_code = str(random.choice(status_codes))
            print(f"Enviando status code: {status_code}")
            conn.sendall(status_code.encode())
            time.sleep(2)

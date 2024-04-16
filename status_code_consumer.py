import socket

host = 'localhost'
port = 9999

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    print(f"Conectado a {host}:{port}")

    while True:
        status_code = s.recv(1024).decode()
        if not status_code:
            break

        status_code = int(status_code)

        if 200 <= status_code <= 299:
            print(f"Recebido status code de sucesso: {status_code}")
        elif 400 <= status_code <= 499:
            print(f"Recebido status code erro cliente: {status_code}")
        elif 500 <= status_code <= 599:
            print(f"Recebido status code erro servidor : {status_code}")
        else:
            print(f"Recebido status code desconhecido: {status_code}")
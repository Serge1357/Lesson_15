import socket
import logging

# Конфигурация логирования
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 55000))
sock.listen(10)
Dict = {"Hi": "Hello", "How are you?": "fine", "see you later": "good luck"}
while True:
    try:
        conn, addr = sock.accept()
        logging.info('Connected: %s', addr)

        data = conn.recv(1024)
        received_data = data.decode()
        logging.info('Received data: %s', received_data)

        response = Dict.get(received_data)
        if response:
            conn.send(response.encode())
            logging.info('Sent response: %s', response)
        else:
            conn.send('Unknown command'.encode())
            logging.warning('Unknown command: %s', received_data)

        conn.close()
    except Exception as e:
        logging.error('An error occurred: %s', str(e))

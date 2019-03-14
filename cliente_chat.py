import socket

IP = "192.168.0.157"
PORT = 8000

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(s)

try:
    s.connect((IP, PORT))

except OSError:
    print("Socket already used")
    # But first we need to disconnect
    s.close()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((IP, PORT))


while True:
    entrada = s.recv(2048).decode("utf-8")
    print("Mensaje del servidor: ", entrada)
    if entrada.lower() == "adios":
        break
    else:
        mensaje = input("Responde: ")
        salida = str.encode(mensaje)
        s.send(salida)
        if mensaje.lower() == "adios":
            break


s.close()

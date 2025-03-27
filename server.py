from socket import *           
from constCS import *         

s = socket(AF_INET, SOCK_STREAM)  
s.bind((HOST, PORT))              
s.listen(1)                       

print("Câmbio, Server na Escuta: Esperando conexões... Câmbio desligo.\n")

(conn, addr) = s.accept()         

def process_add(args):
  result = 0
  for arg in args:
    result += int(arg)
  return result

def process_subtract(args):
  result = 0
  for arg in args:
    result -= int(arg)
  return result

def process_multiply(args):
  result = 1
  for arg in args:
    result *= int(arg)
  return result

def process_divide(args):
  result = int(args[0])
  for arg in args[1:]:
    result /= int(arg)
  return result


def handle_request(decoded_data):
  command_map = {
    "add": process_add,
    "multiply": process_multiply,
    "subtract": process_subtract,
    "divide": process_divide
  }

  function = decoded_data.split()[0]

  func = command_map.get(function)

  if func:
    result = func(decoded_data.split()[1:])
    return str(result)
  else:
    return "Comando Desconhecido"

while True:  
    try:
        data = conn.recv(1024)  
        if not data:  
           print("Cliente desconectado.")
           break;
        decoded_data = bytes.decode(data)  
        print(f"Dados recebidos: {decoded_data}")
        response = handle_request(decoded_data)  
        conn.send(str.encode(response))  
    except KeyboardInterrupt:  
        print("\nServidor interrompido manualmente.")
        break  

















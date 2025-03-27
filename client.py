from socket  import *
from constCS import * #-


def send(s, data):
    s.send(str.encode(data))            
    response = s.recv(1024)             
    print (bytes.decode(response))

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))             

print("="*70)
print("======= SEJA BEM VINDO AO SISTEMA DE CALCULADORA REMOTA DA AWS =======")
print("="*70)

print("\nOPERAÇÕES DISPONÍVEIS:")
print("-" * 70)

print("   🧮 SOMA:         add a b c ... z")
print("   ➖ SUBTRAÇÃO:    subtract a b c ... z")
print("   ✖️ MULTIPLICAÇÃO: multiply a b c ... z")
print("   ➗ DIVISÃO:      divide a b c ... z")

print("-" * 70)
print("Se cansar, digite 'exit' e eu prometo que vou desligar. 🚪👋")

print("="*70)

def user_input_loop(s):
    while True:
        data = input("Digite sua mensagem (ou 'exit' para sair): ")
        if data.lower() == "exit":
            print("Saindo...")
            break
        send(s, data)

user_input_loop(s)

s.close()
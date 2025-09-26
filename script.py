import paho.mqtt.client as mqtt
import time
import random

BROKER = "test.mosquitto.org"
PORT = 1883
TOPICS = ["tamagochi/fome", "tamagochi/triste", "tamagochi/cansado"]

def enviar_estado(client):
    for topic in TOPICS:
        estado = random.choice(["sim", "não"])
        client.publish(topic, estado)
        print(f"Enviado: {topic} -> {estado}")

client = mqtt.Client()
client.connect(BROKER, PORT)

while True:
    enviar_estado(client)
    while True:
        aux = input('\nDeseja encerrar o programa? (S/N)')
        if aux == 'S':
            print('\nEncerrando...')
            time.sleep(3)
            exit()
        elif aux == 'N':
            print('\nRodando novamente...')
            time.sleep(3)
            break
        else:
            print('Valor inválido')

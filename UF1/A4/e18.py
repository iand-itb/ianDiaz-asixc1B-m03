import time

while True:
    for i in range(1, 86400):
        segundos = i % 60
        minutos = int(i / 60) % 60
        horas = int(i / 3600)
        print(f"{horas:02}:{minutos:02}:{segundos:02}", end="\r")
        time.sleep(1)
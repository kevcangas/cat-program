import time


start_time = time.time()
while 1:
    now_time = time.time()
    print("Gato")
    if now_time - start_time > 20:
        print("Listo")
        break
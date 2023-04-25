import time


start_time = time.time()
while 1:
    now_time = time.time()
    if now_time - start_time > 60:
        print("Listo")
        break
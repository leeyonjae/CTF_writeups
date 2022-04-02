
import subprocess
from timeit import default_timer
from tqdm import tqdm

pin = 0
result = open("sc1.txt", "w")
for a in range(100):
    pinchecker = subprocess.Popen("./pin_checker", stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    
    payload = str(48390500 + a).encode()
    timerbegin = default_timer()
    attack = pinchecker.communicate(payload)
    elapsed = default_timer() - timerbegin

    result.write(payload.decode() + " : " + str(round(elapsed, 5)) + "\n")
    
    if b"denied" not in attack[0]:
        print(attack[0].decode())
        pin = int(payload.decode())
        print("PIN: ", payload.decode())
        pinchecker.kill()
        break
    pinchecker.kill()

result.close()
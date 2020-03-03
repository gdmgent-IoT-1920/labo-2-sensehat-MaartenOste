from sense_emu import SenseHat
import sys
import time
import random

sense = SenseHat()
sense.set_imu_config(False, False, False)

def main():
    text = 'Hello! We are New Media Development :)'
    while True:
        rnd1 = random.randrange(0,255)
        rndb1 = random.randrange(0,rnd1)
        rnd2 = random.randrange(0,255)
        rndb2 = random.randrange(0,rnd2)
        rnd3 = random.randrange(0,255)
        rndb3 = random.randrange(0,rnd3)
        sense.show_message(text, 0.07, [rnd1,rnd2,rnd3], [rndb1,rndb2,rndb3])  
        time.sleep(3)
        
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()


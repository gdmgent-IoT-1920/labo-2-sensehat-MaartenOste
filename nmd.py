from sense_emu import SenseHat
import sys
import time
import random

sense = SenseHat()
sense.set_imu_config(False, False, False)



def main():
    text = input('welke tekst wil je weergeven?')
    speed = input('en hoe snel (in seconden per letter)')
    while True:
        for x in text:
            rnd1 = random.randrange(0,255)
            rnd2 = random.randrange(0,255)
            rnd3 = random.randrange(0,255)
            sense.show_letter(x, [rnd1,rnd2,rnd3], [0,0,0])
            time.sleep(float(speed))
        sense.clear()    
        time.sleep(3)
        
try:
    main()
except (KeyboardInterrupt, SystemExit):
    print('Programma sluiten')
finally:
    print('Opkuisen van de matrix')
    sense.clear()
    sys.exit()

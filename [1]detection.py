from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import time

sonar1 = GroveUltrasonicRanger(12) # pin12, slot D12
sonar2 = GroveUltrasonicRanger(16) # pin12, slot D12

print('Detecting distance...')
while True:
    print('1 : {} cm'.format(sonar1.get_distance()))
    print('2 : {} cm'.format(sonar2.get_distance()))
    time.sleep(1)
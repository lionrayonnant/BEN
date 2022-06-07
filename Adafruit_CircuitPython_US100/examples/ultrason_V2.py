from grove.grove_ultrasonic_ranger import GroveUltrasonicRanger
import time

sonar = GroveUltrasonicRanger(12) # pin12, slot D12

print('Detecting distance...')
while True:
    print('{} cm'.format(sonar.get_distance()))
    time.sleep(1)
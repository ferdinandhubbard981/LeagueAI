import numpy as np
import time
import mouse
def main():
    print("hi2")
    random_row = np.random.random_sample()*100
    random_col = np.random.random_sample()*10
    random_time = np.random.random_sample()*np.random.random_sample() * 100
    mouse.wheel(1000)
    mouse.wheel(-1000)
    mouse.move(random_row, random_col, absolute=False, duration=0.2)
    mouse.move(-random_row, -random_col, absolute=False, duration = 0.2)
    mouse.LEFT
    time.sleep(random_time)
if __name__ == '__main__':
    main()
    print("hi")
    while True:
        main()

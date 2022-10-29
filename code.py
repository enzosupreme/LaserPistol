
import time
import board
from digitalio import DigitalInOut, Direction, Pull
import audioio
import audiocore
import neopixel
from colorpallette import colors

#Audio Files
lase = "laser.wav"


# Button pins:
a = DigitalInOut(board.A4)
a.direction = Direction.INPUT
a.pull = Pull.UP


pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=1)

led1 = DigitalInOut(board.A1)
led2 = DigitalInOut(board.A2)
led3 = DigitalInOut(board.A3)
laser = DigitalInOut(board.A7)

led1.direction = Direction.OUTPUT
led2.direction = Direction.OUTPUT
led3.direction = Direction.OUTPUT
laser.direction = Direction.OUTPUT

#Color Pallete import
col = [
    colors.RED,
    colors.GREEN,
    colors.MINT,
    colors.BLUE,
    colors.CYAN,
    colors.NEON,
    colors.CYBER,
    colors.MAGENTA,
    colors.ORANGE,
]

lights = [
    led1,
    led2,
    led3
]

def play_file():
    print("Playing File " + lase)
    wave_file = open(lase, "rb")
    with audiocore.WaveFile(wave_file) as wave:
        with audioio.AudioOut(board.A0) as audio:
            audio.play(wave)
            while audio.playing:
                for i in range(len(pixels)):
                    pixels[i] = col[2]
                    time.sleep(0.1)
                pixels.fill(0)
                time.sleep(0.3)
                pixels.show()
                for i in range(3):
                    lights[i].value = True
                    time.sleep(0.2)
                laser.value = True
                time.sleep(1)

                for i in range(3):
                    lights[i].value = False
                    time.sleep(0.4)
                time.sleep(0.1)



while True:


    while not a.value:
        play_file()

    laser.value = False



    #if not a.value:
        #play_file(thanks,6)


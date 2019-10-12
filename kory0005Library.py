import math
import random
import time
from gfxhat import lcd
from gfxhat import backlight
lcd.clear()
lcd.show()


# Create a function that displays a vertical line at a given x coordinate on the gfx hat.
def verticalLine(arg1, arg2):
    while(arg2 <= 63):
        lcd.set_pixel(arg1, arg2, 1)
        arg2 = arg2 + 1
    lcd.show()
    return (arg2)



# Create a function that displays a horizontal line at a given y coordinate.
def horizontalLine(arg1, arg2):
    while(arg1 <= 127):
        lcd.set_pixel(arg1, arg2, 1)
        arg1 = arg1 + 1
    lcd.show()
    return(arg1)



# Create a function that displays random pixel on the screen for a given period of time specifies in seconds.
def randomPixel(counter):
    while (counter <= 4):
        lcd.set_pixel(random.randrange(1, 128, 1), random.randrange(1, 64, 1), 1)
        time.sleep(2)
        lcd.show()
        # lcd.clear()
    return(counter)



# Create a function clearBacklight() that resets the backlight color
def clearBacklight():
    while True:
        backlight.set_all(191, 0, 255)
        time.sleep(5)
        backlight.show()
    return ()

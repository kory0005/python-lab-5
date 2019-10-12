from kory0005Library import clearBacklight
from gfxhat import backlight
from gfxhat import lcd

backlight.set_all(128, 255, 0)
backlight.show()

lcd.clear()
print (clearBacklight())
lcd.show()
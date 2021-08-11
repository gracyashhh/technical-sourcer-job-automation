#### Rough Draft Playground ####
import pyautogui as pa
from time import sleep
import ctypes
MessageBox = ctypes.windll.user32.MessageBoxW
sleep(5)
hence=str(pa.position())
# pa.click(1182,352)
# pa.typewrite('<500\n',interval=0.5)
# pa.typewrite('Internet\n',interval=0.2)
# pa.click(1182,302)
# pa.click(794,349)
pa.click(1213,451) # + forprojects

MessageBox(None, hence, 'Magic', 0)
print(hence)


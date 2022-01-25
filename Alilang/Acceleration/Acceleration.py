import rpa as r
import os

r.init(visual_automation = True, chrome_browser = False,turbo_mode = True)

os.system('open /Applications/AliLang.app')

r.click('./Resources/Network.png')
r.click('./Resources/Acceleration.png')
r.click('./Resources/TurnOn.png')
r.click('./Resources/Agree.png')

r.close()
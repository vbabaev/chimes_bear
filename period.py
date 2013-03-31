import clock
import config
import voice

appConfig = config.Config()
specificVoice = voice.Voice(appConfig.get('root'), 1)

attempts = 0

while attempts < 25:
    try:
        currentClock = clock.Clock(specificVoice)
        currentClock.do_chimes_bong()
        break
    except:
        attempts += 1

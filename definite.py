import clock
import config
import voice

appConfig = config.Config()
specificVoice = voice.Voice(appConfig.get('root'), 0)

currentClock = clock.Clock(specificVoice)
currentClock.do_definite_bong()


import clock
import voice

currenDirectory = "~/Projects/chimes_bear/"
specificVoice = voice.Voice(currenDirectory)

currentClock = clock.Clock(specificVoice)
currentClock.do_hourly_bong()

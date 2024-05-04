# camera folder 

import audio.record_audio
import photo.capture 
import video.soot
import video.HD.record
import video.SLOW.slow








def main():
	print("Hi this is from main function")
	print('\n')
	audio.record_audio.record()
	print('\n')
	photo.capture.capture()
	print('\n')
	video.soot.soot()
	print('\n')
	video.HD.record.record_hd()
	print('\n')
	video.SLOW.slow.record_slow()




main()

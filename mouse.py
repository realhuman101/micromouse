import microbit
import pyautogui

SPEED = 50

symbols = {
			"N": microbit.Image.ARROW_N,
			"NE": microbit.Image.ARROW_NE,
			"NW": microbit.Image.ARROW_NW,

			"S": microbit.Image.ARROW_S,
			"SE": microbit.Image.ARROW_SE,
			"SW": microbit.Image.ARROW_SW,

			"E": microbit.Image.ARROW_E,
			"W": microbit.Image.ARROW_W,

			"": microbit.Image("00000:00000:00900:00000:00000")
		}

while True:
	microbit.display.show("S")
	
	if microbit.button_a.was_pressed() or microbit.button_b.was_pressed():
		idealX, idealY, idealZ = microbit.accelerometer.get_values()
		break

while True:
	accelerometerVal = microbit.accelerometer.get_values()
	x,y,z = accelerometerVal

	direction = ""

	if y>400+idealY:
		direction += "S"
		pyautogui.moveRel(0, SPEED)

	elif y<-400+idealY:
		direction += "N"
		pyautogui.moveRel(0, -SPEED)

	if x>100+idealX:
		direction += "E"
		pyautogui.moveRel(SPEED, 0)

	elif x<-100+idealX:
		direction += "W"
		pyautogui.moveRel(-SPEED, 0)

	if microbit.button_a.was_pressed() and microbit.button_b.was_pressed():
		while True:
			microbit.display.show("S")
			
			if microbit.button_a.was_pressed() or microbit.button_b.was_pressed():
				idealX, idealY, idealZ = microbit.accelerometer.get_values()
				break

	elif microbit.button_a.was_pressed():
		pyautogui.click()
		
	elif microbit.button_b.was_pressed():
		pyautogui.click(button='right')

	microbit.display.show(symbols[direction])

import microbit
import pyautogui

pyautogui.FAILSAFE = False

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
	if microbit.button_a.was_pressed() and microbit.button_b.was_pressed():
		while True:
			microbit.display.show("S")
			
			if microbit.button_a.was_pressed() or microbit.button_b.was_pressed():
				idealX, idealY, idealZ = microbit.accelerometer.get_values()
				break

	elif microbit.button_a.was_pressed():
		pyautogui.click(button='left')
		
	elif microbit.button_b.was_pressed():
		pyautogui.click(button='right')

	accelerometerVal = microbit.accelerometer.get_values()
	x,y,z = accelerometerVal

	direction = ""

	mY = 400+idealY
	mX = 150+idealX

	moveY, moveX = 0,0

	if y>mY:
		direction += "S"
		moveY = SPEED

	elif y<-mY:
		direction += "N"
		moveY = -SPEED

	if x>mX:
		direction += "E"
		moveX = SPEED

	elif x<-mX:
		direction += "W"
		moveX = -SPEED

	pyautogui.moveRel(moveX, moveY)

	microbit.display.show(symbols[direction])
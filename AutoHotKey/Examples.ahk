f7:: ;Differentiate vs double and single key press
KeyWait, f7, U, T0.2
KeyWait, f7, D, T0.2
if (ErrorLevel = 1) {
	msgbox singlepress
}
else {
	msgbox doublepress
}
return

f6::
pixelx := 922
pixely := 1007
PixelGetColor, beforecolor, pixelx, pixely
loop 50  
{
	PixelGetColor, color, pixelx, pixely
	if (color != beforecolor) 
	{
		msgbox color changed!
		return
	}
	sleep 100
}
msgbox color not changed!
return

~Del & 3:: ; Del & 3, Ends program
ExitApp

+^3:: ;Ctrl, Shift, 3 = Reloads the program
Reload
return

<!^3::Suspend ; Ctrl, Alt, 3 Suspends program

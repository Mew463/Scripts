#SingleInstance force
Menu, Tray, Icon, C:\Users\mingw\Documents\Scripts\AutoHotKey\Images\last-one.ico

f1:: ;Stop key
stop = 1
return

f2:: ;Auto warden hog 
stop = 0
Loop
{
	ImageSearch, x, y, 874, 0, 1051, 82, *100 C:\Users\mingw\Documents\Scripts\AutoHotKey\Images\wardenhog.PNG
	if (Errorlevel = 0)
	{
		sleep 680 ; Main delay
		Loop 2
		{
			send hjkilp8
		}

		stop = 1
	}

	if stop = 1
		break
	
}
return

f3:: ; Showoff in rocketleague
Click, Down Right
send {s down}
sleep 900
Click, Up Right
sleep 50
send {s up}
sleep 50
Click, Down
sleep 1000
Click, Up
return

f4:: ;Sweeper bot
stop := 0
Loop {
	StartTime := A_TickCount
	send {Space}
	send {q Down}
	sleep 450
	send {q Up}
	while A_TickCount - StartTime < 1800 {
		sleep 1
		if stop = 1 
			break
	}
	if stop = 1
		break
}

return

f5:: ;Autoclicker
stop = 0
Loop
{
if stop = 1
	break
Click
Sleep 250 ;Change delay for faster/slower clicks
}
return

f6:: ;Auto export for prusaslicer
send {ctrl Down}
send g
send {ctrl Up}
sleep 1000
send {Enter}
sleep 100
send {Left}
sleep 100
send {Enter}
return

f7:: ; Single click to reload Prismatik and double click to launch Prismatik menu
KeyWait, f7, U, T0.2
KeyWait, f7, D, T0.2
if (ErrorLevel = 1) {
	Process, Close, Prismatik.exe
	Sleep, 1000
	run "C:\Program Files\Prismatik\Prismatik.exe"
}
else {
	run "C:\Program Files\Prismatik\Prismatik.exe"
}
return

f8:: ;copies mouse coordinates to clipboard
MouseGetPos, xpos, ypos  
Clipboard = %xpos%, %ypos%
return

!f8:: ;Say pixel color and mouse position with Alt + f8
CoordMode, ToolTip, Screen
MouseGetPos, MouseX, MouseY
PixelGetColor, color, %MouseX%, %MouseY%
MsgBox The color at the %MouseX%, %MouseY% position is %color%.
return

^f8::
WinGetActiveTitle, Output
msgbox, %Output% || use ahk_exe (programname).exe if window name keeps changing
return

;Phasmophobia journal helper
~1::
IfWinActive, Phasmophobia 
{
	MouseGetPos, x, y
	MouseMove, 716, 80
	Click
	MouseMove, %x%, %y%
}
return

~2::
IfWinActive, Phasmophobia 
{
	MouseGetPos, x, y
	MouseMove, 856, 65
	Click
	MouseMove, %x%, %y%
}
return

~3::
IfWinActive, Phasmophobia 
{
	MouseGetPos, x, y
	MouseMove, 1016, 81
	Click
	MouseMove, %x%, %y%
}
return

~4::
IfWinActive, Phasmophobia 
{
	MouseGetPos, x, y
	MouseMove, 1165, 70
	Click
	MouseMove, %x%, %y%
}
return

~Tab::
IfWinActive, Phasmophobia 
{
	MouseGetPos, x, y
	MouseMove, 1429, 985
	Click
	MouseMove, %x%, %y%
}
return

~`::
IfWinActive, Phasmophobia 
{
	MouseGetPos, x, y
	MouseMove, 400, 953
	Click
	MouseMove, %x%, %y%
}
return

f9:: ; Toggle hotspot for phone
send {LWin}
sleep 1500 
send hot
sleep 500
send {Enter}
sleep 2000
ImageSearch, x, y, 31, 37, 1319, 332, *100 C:\Users\mingw\Documents\Scripts\AutoHotKey\Images\OffWifi.png
if (ErrorLevel = 0) 
{
	Goto continue
}
ImageSearch, x, y, 31, 37, 1319, 332, *100 C:\Users\mingw\Documents\Scripts\AutoHotKey\Images\OnWifi.png
if (ErrorLevel = 0) 
{
	Goto continue
}
msgbox failed to find on/off slider
return
continue: 
MouseMove, x, y+5
sleep 350
Click
sleep 1000 
send {alt Down}
send {f4}
send {alt Up}
return

f10::
return

f11::
return

f12::
return


~Del & 2:: ; Del & 2, Ends program
ExitApp

+^2:: ;Ctrl, Shift, 2 = Reloads the program
Reload
return

<!^2::Suspend ; Ctrl, Alt, 2 Suspends program



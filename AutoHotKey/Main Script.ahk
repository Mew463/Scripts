#SingleInstance, Force  
Menu, Tray, Icon, C:\Users\mingw\Documents\Scripts\AutoHotKey\Images\computer.ico

WindowHotkey(Window, ProgramFile) {
	if WinExist(Window) {
		IfWinActive, %Window%
		{
			WinMinimize, %Window%
			return
		}
		else
			WinActivate, %Window%
	}
	else {
		run, %ProgramFile%
	}

}

;Capslock to enter
CapsLock::Enter
return

;Windows Desktop Changer
<^XButton1::
send {CtrlDown}{LWinDown}{Left}{CtrlUp}{LWinUp}
return
<^XButton2::
send {CtrlDown}{LWinDown}{Right}{CtrlUp}{LWinUp}
return

RAlt:: ; Switch tabs in chrome 
send {Control down}
send {PGUP}
send {Control Up}
return

RCtrl:: ; Switch tabs in chrome
send {Control down}
send {PGDN}
send {Control Up}
return

`::
send {Media_Play_Pause}
return

>+`::
send {Media_Next}
return

>+Del::
send {Media_Prev}
return

PgUp::
send {Volume_Up 1}
return

>+PgUp::
send {Volume_Up 3}
return

PgDn::
send {Volume_Down 1}
return

>+PgDn::
send {Volume_Down 3}
return

+^<::
Winset, Alwaysontop, Off , A ;Set window not ontop
return
+^>::
Winset, Alwaysontop, On , A ;Set window not ontop
return

+^a:: ;Run Obsidian with Ctrl,Shift,a
WindowHotkey("ahk_exe Obsidian.exe", "C:\Users\mingw\AppData\Local\Obsidian\Obsidian.exe") ; add ahk_exe if the name changes
return

+^x:: ;Run Tick Tick with ctrl, shift, and x
WindowHotkey("TickTick", "C:\Program Files (x86)\TickTick\TickTick.exe")
return

+^s:: ;Run YouTube Music with ctrl, shift, and s 
WindowHotkey("YouTube Music", "C:\Users\mingw\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Chrome Apps\YouTube Music.lnk")
return

+^q:: ;Run PrusaSlicer with ctrl, shift, and s 
WindowHotkey("PrusaSlicer", "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Prusa3D\PrusaSlicer 2.5.0.lnk")
return

+^z:: ;Run Discord
WindowHotkey("ahk_exe Discord.exe", "C:\Users\mingw\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk") ; add ahk_exe if the name changes
return

~Del & 1:: ; Del & 1, Ends program
ExitApp

+^1:: ;Ctrl, Shift, 1 = Reloads the program
Reload
return

<!^1::Suspend ; Ctrl, Alt, 1 Suspends program



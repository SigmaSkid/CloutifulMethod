#Requires AutoHotkey v2.0+

global once := true
global duration := 60

; Function to generate random number following a bell curve
NormalRandom(mean, stddev) {
    static PI := 3.141592653589793
    U1 := Random()
    U2 := Random()
    R := Sqrt(-2 * Log(U1))
    Theta := 2 * PI * U2
    Z0 := R * Cos(Theta)
    return mean + Z0 * stddev
}

; When the "D" key is pressed down
$d::
{
    if (once)
    {
        global once := false
        global startTime := A_TickCount
    }
    
    Send("{d Down}")
}

; When the "D" key is released
$d Up::
{
    global once := true
    endTime := A_TickCount
    temp_duration := endTime - startTime
    
    if (temp_duration < 120)
    {
        global duration := temp_duration
    }
    
    Send("{d Up}")
    
    ; MsgBox("The 'D' key was held down for " . duration . " milliseconds.")
}

; Prevent "S" from being pressed by user.
#s:: 
{

}

; When the "S" key is released
$s Up::
{
    Send("{s Down}")

    ; Generate a delay with a bell curve (mean = duration, stddev = 5)
    noisyDelay := NormalRandom(duration, 5)
    noisyDelay := Round(noisyDelay)  ; Round to nearest integer

    Sleep(noisyDelay)
    Send("{s Up}")
    
    ; MsgBox("Simulated 'S' key press for " . noisyDelay . " milliseconds.")
}
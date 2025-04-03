 set kernel_options no_blank_lines
 set optimization speed
 set romsize 4k
 
 
 dim _up=a
 dim _down=b
 dim _left=c
 dim _right=d
 dim _frameCounter=e
 dim _velocity=f
 
 
__reset
 COLUPF=$06
 COLUBK=$0E
 scorecolor=$00
 player0y=55
 player0x=41
 player1x=0
 score=0
 
 gosub __pidle
 
__mainloop
 rem _frameCounter=_frameCounter+1
 rem if _frameCounter>=6 then missile0x=missile0x-_speed:score=score+_speed:_scoreTemp=_scoreTemp+_speed:_frameCounter=0
 

 
 drawscreen
 if switchreset then goto __reset
 goto __mainloop
 


 
 
 rem *********************
 rem GFX
 rem *********************
 
__pidle
 player0:
 %10000011
 %11000010
 %00100010
 %00111100
 %00111100
 %10111100
 %01111100
 %00111110
 %00111101
 %00111101
 %00111100
 %00111100
 %00111100
 %00100000
 %00111100
end
 return

__pwalk
 player0:
 %00101000
 %00010000
 %00101000
 %00100100
 %00111100
 %00111100
 %00111101
 %01111101
 %10111110
 %00111100
 %00111100
 %00111100
 %00111100
 %00111100
 %00100000
 %00111100
end
 return
 

 




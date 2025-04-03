 set kernel_options no_blank_lines
 set optimization speed
 set romsize 4k
 
 dim _Bit7_Flip_P1 = y
 
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
 
 

 




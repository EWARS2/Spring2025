 set kernel_options pfcolors no_blank_lines background
 set romsize 4k
 rem set smartbranching on
 
 rem COLUPF=$06 :rem PlayField Gray
 scorecolor=$06
 AUDV0=8
 player0x=41
 const pfres=3
 
 
 dim _velocity=a
 dim _frameCounter=b
 dim _rng=c
 dim _scoreTemp=d
 dim _speed=e
 dim _checkpointCount=f
 
 dim _Bit7_Flip_P1 = y


 
 
 
 
 


__title
 player0y=55
 player1x=0
 _speed=2
 score=0
 _scoreTemp=0
 _checkpointCount=0
 _velocity=10
 gosub __pfidle
 gosub __draw
 if !joy0fire && !joy0up then goto __title






__mainloop
 _frameCounter=_frameCounter+1
 if _frameCounter>=6 then missile0x=missile0x-_speed:score=score+_speed:_scoreTemp=_scoreTemp+_speed:_frameCounter=0
 if missile0x>200 then missile0x=missile0x+160
 player1x=player1x-_speed
 if player1x>200 then gosub __nextObj
 
 if _rng=3 then gosub __animBird else gosub __obcactus

 




 player0y=(player0y-_velocity)+10
 gosub __physics
 if joy0down then gosub __physics:gosub __pfduck
 
 
 if _scoreTemp>=100 then gosub __checkpoint
 
 
  
 if collision(player0,player1) then goto __gameover
 gosub __draw
 goto __mainloop

__draw
 if switchbw then gosub __bg_black else gosub __bg_white
 if _rng<3 && _Bit7_Flip_P1{7} then REFP1 = 8
 if _rng<=1 then NUSIZ1=$31 
 drawscreen
 AUDC0=0
 AUDF0=12
 if switchreset then pop:goto __title
 return

 
 
 
 


 
 
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
 
 

 




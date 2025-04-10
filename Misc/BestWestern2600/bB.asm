game
.L00 ;  set kernel_options no_blank_lines

.L01 ;  set optimization speed

.L02 ;  set romsize 4k

.
 ; 

.
 ; 

.L03 ;  dim _up = a

.L04 ;  dim _down = b

.L05 ;  dim _left = c

.L06 ;  dim _right = d

.L07 ;  dim _frameCounter = e

.L08 ;  dim _velocity = f

.
 ; 

.
 ; 

.__reset
 ; __reset

.L09 ;  COLUPF = $06

	LDA #$06
	STA COLUPF
.L010 ;  COLUBK = $0E

	LDA #$0E
	STA COLUBK
.L011 ;  scorecolor = $00

	LDA #$00
	STA scorecolor
.L012 ;  player0y = 55

	LDA #55
	STA player0y
.L013 ;  player0x = 41

	LDA #41
	STA player0x
.L014 ;  player1x = 0

	LDA #0
	STA player1x
.L015 ;  score = 0

	LDA #$00
	STA score+2
	LDA #$00
	STA score+1
	LDA #$00
	STA score
.
 ; 

.L016 ;  gosub __pidle

 jsr .__pidle

.
 ; 

.__mainloop
 ; __mainloop

.L017 ;  rem _frameCounter=_frameCounter+1

.L018 ;  rem if _frameCounter>=6 then missile0x=missile0x-_speed:score=score+_speed:_scoreTemp=_scoreTemp+_speed:_frameCounter=0

.
 ; 

.L019 ;  rem fix sound later lol

.L020 ;  if joy0fire  ||  joy0up then AUDC0 = 12 : _velocity = 13

 bit INPT4
	BMI .skipL020
.condpart0
 jmp .condpart1
.skipL020
 lda #$10
 bit SWCHA
	BNE .skip0OR
.condpart1
	LDA #12
	STA AUDC0
	LDA #13
	STA _velocity
.skip0OR
.
 ; 

.
 ; 

.
 ; 

.L021 ;  if _velocity > 0 then _velocity = _velocity - 1

	LDA #0
	CMP _velocity
     BCS .skipL021
.condpart2
	DEC _velocity
.skipL021
.
 ; 

.L022 ;  drawscreen

 jsr drawscreen
.L023 ;  if switchreset then goto __reset

 lda #1
 bit SWCHB
	BNE .skipL023
.condpart3
 jmp .__reset

.skipL023
.L024 ;  goto __mainloop

 jmp .__mainloop

.
 ; 

.
 ; 

.
 ; 

.
 ; 

.
 ; 

.L025 ;  rem *********************

.L026 ;  rem GFX

.L027 ;  rem *********************

.
 ; 

.__pidle
 ; __pidle

.L028 ;  player0:

	LDX #<playerL028_0
	STX player0pointerlo
	LDA #>playerL028_0
	STA player0pointerhi
	LDA #14
	STA player0height
.L029 ;  return

	RTS
.
 ; 

.__pwalk
 ; __pwalk

.L030 ;  player0:

	LDX #<playerL030_0
	STX player0pointerlo
	LDA #>playerL030_0
	STA player0pointerhi
	LDA #15
	STA player0height
.L031 ;  return

	RTS
.
 ; 

.
 ; 

.
 ; 

.
 ; 

.
 ; 

.
 ; 

 if (<*) > (<(*+14))
	repeat ($100-<*)
	.byte 0
	repend
	endif
playerL028_0
	.byte  %10000011
	.byte  %11000010
	.byte  %00100010
	.byte  %00111100
	.byte  %00111100
	.byte  %10111100
	.byte  %01111100
	.byte  %00111110
	.byte  %00111101
	.byte  %00111101
	.byte  %00111100
	.byte  %00111100
	.byte  %00111100
	.byte  %00100000
	.byte  %00111100
 if (<*) > (<(*+15))
	repeat ($100-<*)
	.byte 0
	repend
	endif
playerL030_0
	.byte  %00101000
	.byte  %00010000
	.byte  %00101000
	.byte  %00100100
	.byte  %00111100
	.byte  %00111100
	.byte  %00111101
	.byte  %01111101
	.byte  %10111110
	.byte  %00111100
	.byte  %00111100
	.byte  %00111100
	.byte  %00111100
	.byte  %00111100
	.byte  %00100000
	.byte  %00111100
 if ECHOFIRST
       echo "    ",[(scoretable - *)]d , "bytes of ROM space left")
 endif 
ECHOFIRST = 1
 
 
 

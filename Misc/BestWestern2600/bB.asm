game
.L00 ;  set kernel_options no_blank_lines

.L01 ;  set optimization speed

.L02 ;  set romsize 4k

.
 ; 

.L03 ;  dim _Bit7_Flip_P1  =  y

.
 ; 

.__reset
 ; __reset

.L04 ;  COLUPF = $00

	LDA #$00
	STA COLUPF
.L05 ;  COLUBK = $0E

	LDA #$0E
	STA COLUBK
.L06 ;  scorecolor = $06

	LDA #$06
	STA scorecolor
.L07 ;  player0y = 55

	LDA #55
	STA player0y
.L08 ;  player0x = 41

	LDA #41
	STA player0x
.L09 ;  player1x = 0

	LDA #0
	STA player1x
.L010 ;  score = 0

	LDA #$00
	STA score+2
	LDA #$00
	STA score+1
	LDA #$00
	STA score
.
 ; 

.L011 ;  gosub __pidle

 jsr .__pidle

.
 ; 

.__mainloop
 ; __mainloop

.
 ; 

.
 ; 

.
 ; 

.L012 ;  drawscreen

 jsr drawscreen
.L013 ;  if switchreset then goto __reset

 lda #1
 bit SWCHB
	BNE .skipL013
.condpart0
 jmp .__reset

.skipL013
.L014 ;  goto __mainloop

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

.L015 ;  rem *********************

.L016 ;  rem GFX

.L017 ;  rem *********************

.
 ; 

.__pidle
 ; __pidle

.L018 ;  player0:

	LDX #<playerL018_0
	STX player0pointerlo
	LDA #>playerL018_0
	STA player0pointerhi
	LDA #14
	STA player0height
.L019 ;  return

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

.
 ; 

 if (<*) > (<(*+14))
	repeat ($100-<*)
	.byte 0
	repend
	endif
playerL018_0
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
 if ECHOFIRST
       echo "    ",[(scoretable - *)]d , "bytes of ROM space left")
 endif 
ECHOFIRST = 1
 
 
 

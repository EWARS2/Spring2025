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

.
 ; 

.
 ; 

.
 ; 

.__reset
 ; __reset

.L07 ;  COLUPF = $06

	LDA #$06
	STA COLUPF
.L08 ;  COLUBK = $0E

	LDA #$0E
	STA COLUBK
.L09 ;  scorecolor = $00

	LDA #$00
	STA scorecolor
.L010 ;  player0y = 55

	LDA #55
	STA player0y
.L011 ;  player0x = 41

	LDA #41
	STA player0x
.L012 ;  player1x = 0

	LDA #0
	STA player1x
.L013 ;  score = 0

	LDA #$00
	STA score+2
	LDA #$00
	STA score+1
	LDA #$00
	STA score
.
 ; 

.L014 ;  gosub __pidle

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

.L015 ;  drawscreen

 jsr drawscreen
.L016 ;  if switchreset then goto __reset

 lda #1
 bit SWCHB
	BNE .skipL016
.condpart0
 jmp .__reset

.skipL016
.L017 ;  goto __mainloop

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

.L018 ;  rem *********************

.L019 ;  rem GFX

.L020 ;  rem *********************

.
 ; 

.__pidle
 ; __pidle

.L021 ;  player0:

	LDX #<playerL021_0
	STX player0pointerlo
	LDA #>playerL021_0
	STA player0pointerhi
	LDA #14
	STA player0height
.L022 ;  return

	RTS
.
 ; 

.__pwalk
 ; __pwalk

.L023 ;  player0:

	LDX #<playerL023_0
	STX player0pointerlo
	LDA #>playerL023_0
	STA player0pointerhi
	LDA #15
	STA player0height
.L024 ;  return

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
playerL021_0
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
playerL023_0
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
 
 
 

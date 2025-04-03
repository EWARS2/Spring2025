game
.L00 ;  set kernel_options pfcolors no_blank_lines background

.L01 ;  set romsize 4k

.L02 ;  rem set smartbranching on

.
 ; 

.L03 ;  rem COLUPF=$06 :rem PlayField Gray

.L04 ;  scorecolor = $06

	LDA #$06
	STA scorecolor
.L05 ;  AUDV0 = 8

	LDA #8
	STA AUDV0
.L06 ;  player0x = 41

	LDA #41
	STA player0x
.L07 ;  const pfres = 3

.
 ; 

.
 ; 

.L08 ;  dim _velocity = a

.L09 ;  dim _frameCounter = b

.L010 ;  dim _rng = c

.L011 ;  dim _scoreTemp = d

.L012 ;  dim _speed = e

.L013 ;  dim _checkpointCount = f

.
 ; 

.L014 ;  dim _Bit7_Flip_P1  =  y

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

.
 ; 

.
 ; 

.__title
 ; __title

.L015 ;  player0y = 55

	LDA #55
	STA player0y
.L016 ;  player1x = 0

	LDA #0
	STA player1x
.L017 ;  _speed = 2

	LDA #2
	STA _speed
.L018 ;  score = 0

	LDA #$00
	STA score+2
	LDA #$00
	STA score+1
	LDA #$00
	STA score
.L019 ;  _scoreTemp = 0

	LDA #0
	STA _scoreTemp
.L020 ;  _checkpointCount = 0

	LDA #0
	STA _checkpointCount
.L021 ;  _velocity = 10

	LDA #10
	STA _velocity
.L022 ;  gosub __pfidle

 jsr .__pfidle

.L023 ;  gosub __draw

 jsr .__draw

.L024 ;  if !joy0fire  &&  !joy0up then goto __title

 bit INPT4
	BPL .skipL024
.condpart0
 lda #$10
 bit SWCHA
	BEQ .skip0then
.condpart1
 jmp .__title

.skip0then
.skipL024
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

.__mainloop
 ; __mainloop

.L025 ;  _frameCounter = _frameCounter + 1

	INC _frameCounter
.L026 ;  if _frameCounter >= 6 then missile0x = missile0x - _speed : score = score + _speed : _scoreTemp = _scoreTemp + _speed : _frameCounter = 0

	LDA _frameCounter
	CMP #6
     BCC .skipL026
.condpart2
	LDA missile0x
	SEC
	SBC _speed
	STA missile0x
	SED
	CLC
	LDA score+2
	ADC _speed
	STA score+2
	LDA score+1
	ADC #0
	STA score+1
	LDA score
	ADC #0
	STA score
	CLD
	LDA _scoreTemp
	CLC
	ADC _speed
	STA _scoreTemp
	LDA #0
	STA _frameCounter
.skipL026
.L027 ;  if missile0x > 200 then missile0x = missile0x + 160

	LDA #200
	CMP missile0x
     BCS .skipL027
.condpart3
	LDA missile0x
	CLC
	ADC #160
	STA missile0x
.skipL027
.L028 ;  player1x = player1x - _speed

	LDA player1x
	SEC
	SBC _speed
	STA player1x
.L029 ;  if player1x > 200 then gosub __nextObj

	LDA #200
	CMP player1x
     BCS .skipL029
.condpart4
 jsr .__nextObj

.skipL029
.
 ; 

.L030 ;  if _rng = 3 then gosub __animBird else gosub __obcactus

	LDA _rng
	CMP #3
     BNE .skipL030
.condpart5
 jsr .__animBird
 jmp .skipelse0
.skipL030
 jsr .__obcactus

.skipelse0
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

.L031 ;  player0y =  ( player0y - _velocity )  + 10

; complex statement detected
	LDA player0y
	SEC
	SBC _velocity
	CLC
	ADC #10
	STA player0y
.L032 ;  gosub __physics

 jsr .__physics

.L033 ;  if joy0down then gosub __physics : gosub __pfduck

 lda #$20
 bit SWCHA
	BNE .skipL033
.condpart6
 jsr .__physics
 jsr .__pfduck

.skipL033
.
 ; 

.
 ; 

.L034 ;  if _scoreTemp >= 100 then gosub __checkpoint

	LDA _scoreTemp
	CMP #100
     BCC .skipL034
.condpart7
 jsr .__checkpoint

.skipL034
.
 ; 

.
 ; 

.
 ; 

.L035 ;  if collision(player0,player1) then goto __gameover

	bit 	CXPPMM
	BPL .skipL035
.condpart8
 jmp .__gameover

.skipL035
.L036 ;  gosub __draw

 jsr .__draw

.L037 ;  goto __mainloop

 jmp .__mainloop

.
 ; 

.__draw
 ; __draw

.L038 ;  if switchbw then gosub __bg_black else gosub __bg_white

 lda #8
 bit SWCHB
	BNE .skipL038
.condpart9
 jsr .__bg_black
 jmp .skipelse1
.skipL038
 jsr .__bg_white

.skipelse1
.L039 ;  if _rng < 3  &&  _Bit7_Flip_P1{7} then REFP1  =  8

	LDA _rng
	CMP #3
     BCS .skipL039
.condpart10
	BIT _Bit7_Flip_P1
	BPL .skip10then
.condpart11
	LDA #8
	STA REFP1
.skip10then
.skipL039
.L040 ;  if _rng <= 1 then NUSIZ1 = $31

	LDA #1
	CMP _rng
     BCC .skipL040
.condpart12
	LDA #$31
	STA NUSIZ1
.skipL040
.L041 ;  drawscreen

 jsr drawscreen
.L042 ;  AUDC0 = 0

	LDA #0
	STA AUDC0
.L043 ;  AUDF0 = 12

	LDA #12
	STA AUDF0
.L044 ;  if switchreset then pop : goto __title

 lda #1
 bit SWCHB
	BNE .skipL044
.condpart13
	pla
	pla
 jmp .__title

.skipL044
.L045 ;  return

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

.L046 ;  rem **********

.L047 ;  rem Reused suff

.L048 ;  rem **********

.
 ; 

.__physics
 ; __physics

.L049 ;  if player0y  >=  55 then gosub __touchingGnd else gosub __gravity

	LDA player0y
	CMP #55
     BCC .skipL049
.condpart14
 jsr .__touchingGnd
 jmp .skipelse2
.skipL049
 jsr .__gravity

.skipelse2
.L050 ;  return

	RTS
.
 ; 

.__touchingGnd
 ; __touchingGnd

.L051 ;  player0y = 55

	LDA #55
	STA player0y
.L052 ;  _velocity = 10

	LDA #10
	STA _velocity
.L053 ;  if _frameCounter = 1 then gosub __input

	LDA _frameCounter
	CMP #1
     BNE .skipL053
.condpart15
 jsr .__input

.skipL053
.L054 ;  if _frameCounter < 3 then gosub __pf2 else gosub __pf3

	LDA _frameCounter
	CMP #3
     BCS .skipL054
.condpart16
 jsr .__pf2
 jmp .skipelse3
.skipL054
 jsr .__pf3

.skipelse3
.L055 ;  return

	RTS
.
 ; 

.__input
 ; __input

.L056 ;  if joy0fire  ||  joy0up then AUDC0 = 12 : _velocity = 13

 bit INPT4
	BMI .skipL056
.condpart17
 jmp .condpart18
.skipL056
 lda #$10
 bit SWCHA
	BNE .skip2OR
.condpart18
	LDA #12
	STA AUDC0
	LDA #13
	STA _velocity
.skip2OR
.L057 ;  return

	RTS
.
 ; 

.__gravity
 ; __gravity

.L058 ;  if _velocity > 0  &&  _frameCounter = 4 then _velocity = _velocity - 1

	LDA #0
	CMP _velocity
     BCS .skipL058
.condpart19
	LDA _frameCounter
	CMP #4
     BNE .skip19then
.condpart20
	DEC _velocity
.skip19then
.skipL058
.L059 ;  gosub __pfidle

 jsr .__pfidle

.L060 ;  return

	RTS
.
 ; 

.__nextObj
 ; __nextObj

.L061 ;  _rng =  ( rand & 3 ) 

; complex statement detected
 jsr randomize
	AND #3
	STA _rng
.L062 ;  player1x = 157 +  ( _rng ) 

; complex statement detected
	LDA #157
	CLC
	ADC _rng
	STA player1x
.L063 ;  if _rng = 3 then player1y = 46 else player1y = 55

	LDA _rng
	CMP #3
     BNE .skipL063
.condpart21
	LDA #46
	STA player1y
 jmp .skipelse4
.skipL063
	LDA #55
	STA player1y
.skipelse4
.L064 ;  _Bit7_Flip_P1{7}  =  !_Bit7_Flip_P1{7}

	LDA _Bit7_Flip_P1
	AND #128
  PHP
	LDA _Bit7_Flip_P1
	AND #127
  PLP
	.byte $D0, $02
	ORA #128
	STA _Bit7_Flip_P1
.L065 ;  return

	RTS
.
 ; 

.__animBird
 ; __animBird

.L066 ;  if _frameCounter < 3 then gosub __obbird1 else gosub __obbird2

	LDA _frameCounter
	CMP #3
     BCS .skipL066
.condpart22
 jsr .__obbird1
 jmp .skipelse5
.skipL066
 jsr .__obbird2

.skipelse5
.L067 ;  return

	RTS
.
 ; 

.__checkpoint
 ; __checkpoint

.L068 ;  AUDF0 = 5

	LDA #5
	STA AUDF0
.L069 ;  AUDC0 = 12

	LDA #12
	STA AUDC0
.L070 ;  if _checkpointCount >= 3  &&  _speed < 4 then _speed = _speed + 1 : _checkpointCount = 0 else _scoreTemp = 0 : _checkpointCount = _checkpointCount + 1

	LDA _checkpointCount
	CMP #3
     BCC .skipL070
.condpart23
	LDA _speed
	CMP #4
     BCS .skip23then
.condpart24
	INC _speed
	LDA #0
	STA _checkpointCount
 jmp .skipelse6
.skip23then
.skipL070
	LDA #0
	STA _scoreTemp
	INC _checkpointCount
.skipelse6
.L071 ;  return

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

.__gameover
 ; __gameover

.L072 ;  AUDC0 = 7

	LDA #7
	STA AUDC0
.L073 ;  gosub __pfdead

 jsr .__pfdead

.
 ; 

.__gameover1
 ; __gameover1

.L074 ;  gosub __draw

 jsr .__draw

.L075 ;  if joy0fire  ||  joy0up then goto __gameover1

 bit INPT4
	BMI .skipL075
.condpart25
 jmp .condpart26
.skipL075
 lda #$10
 bit SWCHA
	BNE .skip5OR
.condpart26
 jmp .__gameover1

.skip5OR
.
 ; 

.__gameover2
 ; __gameover2

.L076 ;  gosub __draw

 jsr .__draw

.L077 ;  if !joy0fire  &&  !joy0up then goto __gameover2

 bit INPT4
	BPL .skipL077
.condpart27
 lda #$10
 bit SWCHA
	BEQ .skip27then
.condpart28
 jmp .__gameover2

.skip27then
.skipL077
.
 ; 

.__gameover3
 ; __gameover3

.L078 ;  gosub __draw

 jsr .__draw

.L079 ;  if joy0fire  ||  joy0up then goto __gameover3

 bit INPT4
	BMI .skipL079
.condpart29
 jmp .condpart30
.skipL079
 lda #$10
 bit SWCHA
	BNE .skip7OR
.condpart30
 jmp .__gameover3

.skip7OR
.L080 ;  goto __title

 jmp .__title

.
 ; 

.__bg_white
 ; __bg_white

.L081 ;  rem COLUBK=$0F

.
 ; 

.L082 ;  pfcolors:

 lda # $0F
 sta COLUPF
 ifconst pfres
 lda #>(pfcolorlabel13-132+pfres*pfwidth)
 else
 lda #>(pfcolorlabel13-84)
 endif
 sta pfcolortable+1
 ifconst pfres
 lda #<(pfcolorlabel13-132+pfres*pfwidth)
 else
 lda #<(pfcolorlabel13-84)
 endif
 sta pfcolortable
.
 ; 

.L083 ;  return

	RTS
.
 ; 

.__bg_black
 ; __bg_black

.L084 ;  rem COLUBK=$00

.L085 ;  ENAM0 = 2

	LDA #2
	STA ENAM0
.
 ; 

.L086 ;  pfcolors:

 lda # $00
 sta COLUPF
 ifconst pfres
 lda #>(pfcolorlabel13-131+pfres*pfwidth)
 else
 lda #>(pfcolorlabel13-83)
 endif
 sta pfcolortable+1
 ifconst pfres
 lda #<(pfcolorlabel13-131+pfres*pfwidth)
 else
 lda #<(pfcolorlabel13-83)
 endif
 sta pfcolortable
.
 ; 

.L087 ;  return

	RTS
.
 ; 

.
 ; 

.L088 ;  rem *********************

.L089 ;  rem Area reserved for GFX

.L090 ;  rem *********************

.
 ; 

.__pf2
 ; __pf2

.__pf3
 ; __pf3

.__pfdead
 ; __pfdead

.__pfidle
 ; __pfidle

.
 ; 

.L091 ;  player0:

	LDX #<playerL091_0
	STX player0pointerlo
	LDA #>playerL091_0
	STA player0pointerhi
	LDA #12
	STA player0height
.L092 ;  return

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

.__pfduck
 ; __pfduck

.L093 ;  player0:

	LDX #<playerL093_0
	STX player0pointerlo
	LDA #>playerL093_0
	STA player0pointerhi
	LDA #7
	STA player0height
.L094 ;  return

	RTS
.
 ; 

.__obcactus
 ; __obcactus

.L095 ;  player1:

	LDX #<playerL095_1
	STX player1pointerlo
	LDA #>playerL095_1
	STA player1pointerhi
	LDA #12
	STA player1height
.L096 ;  return

	RTS
.
 ; 

.__obbird1
 ; __obbird1

.L097 ;  player1:

	LDX #<playerL097_1
	STX player1pointerlo
	LDA #>playerL097_1
	STA player1pointerhi
	LDA #9
	STA player1height
.L098 ;  return

	RTS
.
 ; 

.__obbird2
 ; __obbird2

.L099 ;  player1:

	LDX #<playerL099_1
	STX player1pointerlo
	LDA #>playerL099_1
	STA player1pointerhi
	LDA #10
	STA player1height
.L0100 ;  return

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

.
 ; 

.
 ; 

.
 ; 

.
 ; 

.L0101 ;  vblank

vblank_bB_code
.L0102 ;  asm

 sta HMCLR

 sta WSYNC

 lda #$ff

 sta HMM0

 lda #$c0

 sta WSYNC

 sta HMOVE

 sleep 5

 sta HMM0

.L0103 ;  return

	RTS
.
 ; 

.L0104 ;  
 ifconst pfres
 if (<*) > (254-pfres*pfwidth)
	align 256
	endif
 if (<*) < (136-pfres*pfwidth)
	repeat ((136-pfres*pfwidth)-(<*))
	.byte 0
	repend
	endif
 else
 if (<*) > 206
	align 256
	endif
 if (<*) < 88
	repeat (88-(<*))
	.byte 0
	repend
	endif
 endif
pfcolorlabel13
 .byte  $0F, $00,0,0
 .byte  $0F, $00,0,0
 .byte  $0F, $00,0,0
 .byte  $0F, $00,0,0
 .byte  $0F, $00,0,0
 .byte  $0F, $00,0,0
 .byte  $0F, $00,0,0
 .byte  $06, $06,0,0
 .byte  $0F, $00,0,0
 .byte  $0F, $00,0,0
 .byte  $0F, $00,0,0
 if (<*) > (<(*+12))
	repeat ($100-<*)
	.byte 0
	repend
	endif
playerL091_0
	.byte  %00101000
	.byte  %00101000
	.byte  %00101000
	.byte  %01111000
	.byte  %11111010
	.byte  %11111110
	.byte  %10111000
	.byte  %10011000
	.byte  %00001110
	.byte  %00001000
	.byte  %00001111
	.byte  %00001011
	.byte  %00000110
 if (<*) > (<(*+7))
	repeat ($100-<*)
	.byte 0
	repend
	endif
playerL093_0
	.byte  %10100000
	.byte  %10101000
	.byte  %11111110
	.byte  %11111000
	.byte  %11111111
	.byte  %10111111
	.byte  %10001011
	.byte  %00000110
 if (<*) > (<(*+12))
	repeat ($100-<*)
	.byte 0
	repend
	endif
playerL095_1
	.byte  %00111000
	.byte  %00111000
	.byte  %00111000
	.byte  %00111110
	.byte  %00111111
	.byte  %00111011
	.byte  %11111011
	.byte  %10111011
	.byte  %10111011
	.byte  %10111011
	.byte  %10111000
	.byte  %00111000
	.byte  %00010000
 if (<*) > (<(*+9))
	repeat ($100-<*)
	.byte 0
	repend
	endif
playerL097_1
	.byte  %00010000
	.byte  %00011000
	.byte  %00011100
	.byte  %00011111
	.byte  %00011110
	.byte  %00011111
	.byte  %00111100
	.byte  %11110000
	.byte  %01100000
	.byte  %00100000
 if (<*) > (<(*+10))
	repeat ($100-<*)
	.byte 0
	repend
	endif
playerL099_1
	.byte  %00000000
	.byte  %00000000
	.byte  %00000000
	.byte  %00000000
	.byte  %00000000
	.byte  %00011111
	.byte  %00111110
	.byte  %11111111
	.byte  %01101110
	.byte  %00101100
	.byte  %00001000
 if ECHOFIRST
       echo "    ",[(scoretable - *)]d , "bytes of ROM space left")
 endif 
ECHOFIRST = 1
 
 
 

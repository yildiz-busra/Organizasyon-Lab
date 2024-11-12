#start=Grafik.exe#

#make_bin#

name "ucgen"



BASLA:
	MOV BL, 00H
	MOV AL, 00H
YUKSEK:
    PUSH AX	
    call waitport    
    POP AX
    OUT 160, AL
    INC AL
    CMP AL,0FFH
	JNZ YUKSEK
	MOV AL, 0FFH
    
ALCAK:  
    PUSH AX	
    call waitport    
    POP AX
    OUT 160, AL
    DEC AL
    CMP AL,0FFH

	JNZ ALCAK
	
	;JMP BASLA


hlt
    
waitport:
    wait3:           ; loop to ensure the printer
    in al, 160d     ; is ready, it clears
    or al, 0        ; the port when this is true.
    jnz wait3
    ret

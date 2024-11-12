#start=Grafik.exe#

#make_bin#

name "kare"


    MOV CX,3
KARE:	
    MOV BL, 00H
	MOV AX, 01H
YUKSEK:
    PUSH AX	
    call waitport
    
    POP AX
    OUT 160, AL
    
    INC BL
    CMP BL,19H
	JNZ YUKSEK
	
	MOV BL, 00H
	;MOV AX, 0FAH
EGIK:
    PUSH AX	
    call waitport
    
    POP AX
    OUT 160, AL 
    ADD AL, 0AH
    CMP AL, 0FBH
    JNZ EGIK
    
ALCAK:  
    PUSH AX	
    call waitport
    
    POP AX
    OUT 160, AL

    INC BL
    CMP BL,19H

	JNZ ALCAK
	
	LOOP KARE

hlt

waitport:
    wait3:           ; loop to ensure the printer
    in al, 160d     ; is ready, it clears
    or al, 0        ; the port when this is true.
    jnz wait3
    ret
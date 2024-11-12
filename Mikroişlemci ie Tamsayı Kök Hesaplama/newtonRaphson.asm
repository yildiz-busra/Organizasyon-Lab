	ORG 0100H
	MOV DH, 28H
	MOV AL, 03H
	MOV SI, 0130H
	MOV CH, 0F
DONGU:	
	INC CH
	MOV [SI], AL
	MOV [SI+1], AL
	ADD [SI+1], AL
	MUL AL
	ADD AL, DH
	MOV BH, [SI+1]
	DIV BH
	CMP AL,[SI]
	JZ FINISH
 	JMP DONGU	

       
	

FINISH:	MOV     BX,0000H  ;Returns to PAT System
        MOV     AH,04H       
        INT     028H
                    

                        
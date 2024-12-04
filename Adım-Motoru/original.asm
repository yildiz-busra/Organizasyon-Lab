#start=original.exe

name "stepper"

#make_bin#

steps_before_direction_change = 8h ;32 decimal

jmp start

datcw   db 0000_0110b
        db 0000_0100b
        db 0000_0011b
        db 0000_0010b
        
start:
mov bx, offset datcw 
mov si, 0
mov cx, 0 
mov dx, 0

next_step:
wait:   in al, 7
        test al, 10000000h
        jz wait
        
mov di, dx
delay2:
sub di, 2h
nop
jnz delay2

cmp cx, 4h
jb azaltim
jmp arttirim
add dx, 2h

arttirim:  
    add dx, 2h
    jmp devam
    
azaltim:
    sub dx, 2h
    jmp devam
    
devam:
mov al, [bx][si]
out 7, al

inc si

cmp si, 4
jb next_step
mov si, 8

inc cx 
cmp cx, steps_before_direction_change
int 21h
end    
    
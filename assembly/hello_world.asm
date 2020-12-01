; hello_world.asm
;
; Author: Patrick Cullinane
; Date: 1-Dec-2020

global start

section .text

start:
    mov rax, 0x02000004
    mov rdi, 1
    mov rsi, message
    mov rdx, 13
    syscall
    mov rax, 0x02000001
    xor rdi, rdi
    syscall
    
    section .data

message:
    db  "Hello, World", 10 


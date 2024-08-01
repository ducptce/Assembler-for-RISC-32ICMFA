.text

#Initializes the value for 31 registers:
Initialize:
	addi    x0, x0, 98
	addi    x1, x0, 68
	addi    x2, x0, 185
	addi    x3, x0, 3
	addi    x4, x0, 153
	addi    x5, x0, 97
	addi    x6, x0, 184
	addi    x7, x0, 59
	addi    x8, x0, 95
	addi    x9, x0, 2
	addi    x10, x0, 181
	addi    x11, x0, 153
	addi    x12, x0, 199
	addi    x13, x0, 74
	addi    x14, x0, 119
	addi    x15, x0, 189
	addi    x16, x0, 118
	addi    x17, x0, 59
	addi    x18, x0, 81
	addi    x19, x0, 103
	addi    x20, x0, 172
	addi    x21, x0, 145
	addi    x22, x0, 26
	addi    x23, x0, 157
	addi    x24, x0, 36
	addi    x25, x0, 49
	addi    x26, x0, 191
	addi    x27, x0, 193
	addi    x28, x0, 169
	addi    x29, x0, 146
	addi    x30, x0, 7
	addi    x31, x0, 140

Main:
	sw      x27 , 296 (x0) 
	blt     x17 , x2 , 180 
	slt     x23 , x1 , x19 
	lhu     x6 , 632 (x0) 
	lbu     x5 , 616 (x0) 
	lb      x1 , 212 (x0) 
	srl     x13 , x31 , x3 
	bge     x30 , x2 , 204 
	addi    x28 , x26 , 3 
	lhu     x8 , 512 (x0) 
	auipc   x3 , 87 
	srli    x1 , x25 , 31 
	ori     x9 , x23 , 30 
	slt     x9 , x12 , x15 
	sw      x28 , 432 (x0) 
	sb      x13 , 128 (x0) 
	bgeu    x30 , x25 , 124 
	bne     x16 , x21 , 232 
	sra     x14 , x18 , x30 
	slti    x12 , x20 , 72 
	beq     x11 , x20 , 108 
	lb      x23 , 660 (x0) 
	lb      x27 , 240 (x0) 
	sltiu   x8 , x10 , 85 
	bne     x20 , x2 , 388 
	sh      x10 , 140 (x0) 
	lw      x31 , 180 (x0) 
	lhu     x14 , 528 (x0) 
	sw      x1 , 316 (x0) 
	slti    x29 , x26 , 194 
	sw      x5 , 96 (x0) 
	jalr    x29 , 476(x0) 
	bne     x13 , x3 , 56 
	sw      x31 , 188 (x0) 
	bne     x12 , x28 , 348 
	lb      x9 , 192 (x0) 
	xor     x15 , x17 , x3 
	slt     x13 , x18 , x6 
	lw      x1 , 548 (x0) 
	srl     x21 , x12 , x1 
	sw      x2 , 356 (x0) 
	and     x6 , x26 , x22 
	sb      x10 , 644 (x0) 
	or      x6 , x16 , x24 
	blt     x29 , x12 , 144 
	bne     x29 , x20 , 372 
	jal     x4 , 56 
	sra     x13 , x24 , x15 
	lw      x24 , 556 (x0) 
	srl     x5 , x15 , x10 
	jal     x27 , 336 
	ori     x6 , x14 , 58 
	blt     x5 , x15 , 188 
	and     x9 , x13 , x10 
	srli    x16 , x2 , 25
	sb      x10 , 752 (x0) 
	sw      x30 , 628 (x0) 
	lbu     x27 , 424 (x0) 
	srli    x8 , x19 , 15 
	ori     x10 , x14 , 144 
	or      x26 , x8 , x16 
	or      x3 , x20 , x27 
	andi    x20 , x22 , 102 
	lbu     x11 , 372 (x0) 
	bge     x17 , x22 , 56 
	slt     x5 , x19 , x7 
	sltu    x26 , x8 , x21 
	lui     x20 , 99 
	srl     x12 , x1 , x15 
	sb      x16 , 600 (x0) 
	blt     x18 , x25 , 36 
	blt     x12 , x27 , 172 
	jal     x18 , 104 
	sb      x26 , 640 (x0) 
	auipc   x26 , 45 
	srli    x31 , x17 , 19 
	or      x2 , x15 , x13 
	sw      x15 , 268 (x0) 
	sb      x20 , 468 (x0) 
	bltu    x9 , x19 , 292 
	sll     x4 , x5 , x28 
	lb      x18 , 676 (x0) 
	and     x24 , x17 , x12 
	jalr    x15 , 360(x0) 
	slti    x12 , x10 , 71 
	srli    x31 , x6 , 7 
	lh      x9 , 644 (x0) 
	lhu     x3 , 352 (x0) 
	sw      x29 , 360 (x0) 
	lb      x24 , 168 (x0) 
	sltu    x12 , x5 , x25 
	lw      x15 , 332 (x0) 
	sw      x3 , 692 (x0) 
	sw      x1 , 112 (x0) 
	sh      x11 , 472 (x0) 
	lbu     x19 , 672 (x0) 
	sub     x14 , x15 , x28 
	sh      x23 , 792 (x0) 
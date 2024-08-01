start:	c.beqz x8, main
	addi x17, x0, 76
	c.li x18, 4
	c.jalr x17
main:	c.li x1, 3
	c.addi x2, 16
	c.mv x3, x1
	c.slli x3, 3
	c.lui x4, 1
	c.addi4spn x8, 12 
	c.addi16sp 32
	c.mv x7, x2
	c.mv x9, x2
	c.srai x8, 2
	c.srli x15, 2
	c.mv x5, x8
	c.andi x9, 31
	c.sub x10, x8
	c.xor x11, x9
	c.or x12, x10
	c.and x10, x8
	c.add x14, x12
	c.sw x12, 0 (x11)
	c.swsp x3, 0
	c.lwsp x19, 0
	c.lw x13, 0(x11)
	c.j result1
noise1:	c.li x1, 1
	c.li x2, 2
	c.li x3, 3
	c.li x4, 4
result1:	c.jal result2
noise2:	c.li x1, 2
	c.li x2, 3
	c.li x3, 4
	c.li x4, 5
result2:	c.bnez x9, start
pass:	addi x1, x0, 84
	c.jr x1
fail:	c.li x1, 70
end:	

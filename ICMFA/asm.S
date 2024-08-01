.DATA
.TEXT
MAIN: FLW f1, 4(x1) 				//0
FSW f2, 4(x1)					//4
FADD.S f2, f1, f2				//8
FSUB.S f2, f1, f2				//12
FMUL.S f2, f1, f2				//16
TAG1: //TAG1 HERE				//20
FDIV.S f2, f1, f2				//24
FMIN.S f2, f1, f2				//28
FMAX.S f2, f1, f2				//32
FSQRT.S f2, f1					//36
FCVT.W.S x1, f1					//40
FCVT.WU.S x1, f1				//44
FCVT.S.W f2, x1					//48
FCVT.S.WU f2, x1				//52
TAG2: #THIS IS TAG2				//56
FSGNJ.S f2, f1, f2				//60
FSGNJN.S f2, f1, f2				//64
FSGNJX.S f2, f1, f2				//68
FMV.X.W x1, f1					//72
FMV.W.X f2, x1  //THIS IS MOVE INSTRUCTION	//76
FLT.S x2, f1, f2				//80   ///
FLE.S x2, f1, f2				//84   ///
FEQ.S x2, f1, f2				//88   ///
FCLASS.S x1, f1					//92
FMADD.S f1, f1, f2, f3				//96
FMSUB.S f1, f1, f2, f4				//100
END: 	FNMADD.S f1, f1, f2, f5			//104
FNMSUB.S f1, f1, f2, f6				//108

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 21:57:03 2024

@author: admin
"""
import os
import argparse

parser = argparse.ArgumentParser(description= 'this is 1st line')
parser.add_argument('--sum', )

FP_FMT = {
    'S' : '00',
    'D' : '01',
    'H' : '10',
    'Q' : '11'
    }

OPCODE = {
    'LOAD'        : '0000011',
    'LOAD_FP'     : '0000111',
    'OP_IMM'      : '0010011',
    'AUIPC'       : '0010111',
    'STORE'       : '0100011',
    'STORE_FP'    : '0100111',
    'AMO'         : '0101111',
    'OP'          : '0110011',
    'LUI'         : '0110111',
    'MADD'        : '1000011',
    'MSUB'        : '1000111',
    'NMSUB'       : '1001011',
    'NMADD'       : '1001111',
    'OP_FP'       : '1010011',
    'BRANCH'      : '1100011',
    'JALR'        : '1100111',
    'JAL'         : '1101111'
    }
DATA = {
    # I-Type
    'FLW'           : {'isa' : 'RV32F', 'fmt' : 'I-Type', 'funct3' : '010', 'opcode' : '0000111'},
    'LB'            : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct3' : '000', 'opcode' : '0000011'},
    'LH'            : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct3' : '001', 'opcode' : '0000011'},
    'LW'            : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct3' : '010', 'opcode' : '0000011'},
    'LBU'           : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct3' : '100', 'opcode' : '0000011'},
    'LHU'           : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct3' : '101', 'opcode' : '0000011'},
    'ADDI'          : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct3' : '000', 'opcode' : '0010011'},
    'SLTI'          : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct3' : '010', 'opcode' : '0010011'},
    'SLTIU'         : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct3' : '011', 'opcode' : '0010011'},
    'XORI'          : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct3' : '100', 'opcode' : '0010011'},
    'ORI'           : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct3' : '110', 'opcode' : '0010011'},
    'ANDI'          : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct3' : '111', 'opcode' : '0010011'},
    'JALR'          : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct3' : '000', 'opcode' : '1100111'},
    'NOP'           : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct3' : '000', 'opcode' : '0010011'},
    'SLLI'          : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct7' : '0000000', 'funct3' : '001', 'opcode' : '0010011'}, 
    'SRLI'          : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct7' : '0000000', 'funct3' : '101', 'opcode' : '0010011'},
    'SRAI'          : {'isa' : 'RV32I', 'fmt' : 'I-Type', 'funct7' : '0100000', 'funct3' : '101', 'opcode' : '0010011'},
    # S-Type
    'FSW'           : {'isa' : 'RV32F', 'fmt' : 'S-Type', 'funct3' : '010', 'opcode' : '0100111'},
    'SB'            : {'isa' : 'RV32I', 'fmt' : 'S-Type', 'funct3' : '000', 'opcode' : '0100011'},
    'SH'            : {'isa' : 'RV32I', 'fmt' : 'S-Type', 'funct3' : '001', 'opcode' : '0100011'},
    'SW'            : {'isa' : 'RV32I', 'fmt' : 'S-Type', 'funct3' : '010', 'opcode' : '0100011'},
    # R-Type
    'FADD.S'        : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '00000', 'fp_fmt' : FP_FMT['S'], 'funct3' : '111', 'opcode' : '1010011'},
    'FSUB.S'        : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '00001', 'fp_fmt' : FP_FMT['S'], 'funct3' : '111', 'opcode' : '1010011'},
    'FMUL.S'        : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '00010', 'fp_fmt' : FP_FMT['S'], 'funct3' : '111', 'opcode' : '1010011'},
    'FDIV.S'        : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '00011', 'fp_fmt' : FP_FMT['S'], 'funct3' : '111', 'opcode' : '1010011'},
    'FMIN.S'        : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '00101', 'fp_fmt' : FP_FMT['S'], 'funct3' : '000', 'opcode' : '1010011'},
    'FMAX.S'        : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '00101', 'fp_fmt' : FP_FMT['S'], 'funct3' : '001', 'opcode' : '1010011'},
    'FSQRT.S'       : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '01011', 'fp_fmt' : FP_FMT['S'], 'funct3' : '111', 'opcode' : '1010011'},
    'FCVT.W.S'      : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '11000', 'fp_fmt' : FP_FMT['S'], 'funct3' : '111', 'opcode' : '1010011'},
    'FCVT.WU.S'     : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '11000', 'fp_fmt' : FP_FMT['S'], 'funct3' : '111', 'opcode' : '1010011'},
    'FCVT.S.W'      : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '11010', 'fp_fmt' : FP_FMT['S'], 'funct3' : '111', 'opcode' : '1010011'},
    'FCVT.S.WU'     : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '11010', 'fp_fmt' : FP_FMT['S'], 'funct3' : '111', 'opcode' : '1010011'},
    'FSGNJ.S'       : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '00100', 'fp_fmt' : FP_FMT['S'], 'funct3' : '000', 'opcode' : '1010011'},
    'FSGNJN.S'      : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '00100', 'fp_fmt' : FP_FMT['S'], 'funct3' : '001', 'opcode' : '1010011'},
    'FSGNJX.S'      : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '00100', 'fp_fmt' : FP_FMT['S'], 'funct3' : '010', 'opcode' : '1010011'},
    'FMV.X.W'       : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '11100', 'fp_fmt' : FP_FMT['S'], 'funct3' : '000', 'opcode' : '1010011'},
    'FMV.W.X'       : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '11110', 'fp_fmt' : FP_FMT['S'], 'funct3' : '000', 'opcode' : '1010011'},
    'FLT.S'         : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '10100', 'fp_fmt' : FP_FMT['S'], 'funct3' : '001', 'opcode' : '1010011'},
    'FLE.S'         : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '10100', 'fp_fmt' : FP_FMT['S'], 'funct3' : '000', 'opcode' : '1010011'},
    'FEQ.S'         : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '10100', 'fp_fmt' : FP_FMT['S'], 'funct3' : '010', 'opcode' : '1010011'},
    'FCLASS.S'      : {'isa' : 'RV32F', 'fmt' : 'R-Type', 'funct5' : '11100', 'fp_fmt' : FP_FMT['S'], 'funct3' : '001', 'opcode' : '1010011'},
    'ADD'           : {'isa' : 'RV32I', 'fmt' : 'R-Type', 'funct7' : '0000000', 'funct3' : '000', 'opcode' : '0110011'},
    'SUB'           : {'isa' : 'RV32I', 'fmt' : 'R-Type', 'funct7' : '0100000', 'funct3' : '000', 'opcode' : '0110011'},
    'SLL'           : {'isa' : 'RV32I', 'fmt' : 'R-Type', 'funct7' : '0000000', 'funct3' : '001', 'opcode' : '0110011'},
    'SLT'           : {'isa' : 'RV32I', 'fmt' : 'R-Type', 'funct7' : '0000000', 'funct3' : '010', 'opcode' : '0110011'},
    'SLTU'          : {'isa' : 'RV32I', 'fmt' : 'R-Type', 'funct7' : '0000000', 'funct3' : '011', 'opcode' : '0110011'},
    'XOR'           : {'isa' : 'RV32I', 'fmt' : 'R-Type', 'funct7' : '0000000', 'funct3' : '100', 'opcode' : '0110011'},
    'SRL'           : {'isa' : 'RV32I', 'fmt' : 'R-Type', 'funct7' : '0000000', 'funct3' : '101', 'opcode' : '0110011'},
    'SRA'           : {'isa' : 'RV32I', 'fmt' : 'R-Type', 'funct7' : '0100000', 'funct3' : '101', 'opcode' : '0110011'},
    'OR'            : {'isa' : 'RV32I', 'fmt' : 'R-Type', 'funct7' : '0000000', 'funct3' : '110', 'opcode' : '0110011'},
    'AND'           : {'isa' : 'RV32I', 'fmt' : 'R-Type', 'funct7' : '0000000', 'funct3' : '111', 'opcode' : '0110011'},
    'MUL'           : {'isa' : 'RV32M', 'fmt' : 'R-Type', 'funct7' : '0000001', 'funct3' : '000', 'opcode' : '0110011'},
    'MULH'          : {'isa' : 'RV32M', 'fmt' : 'R-Type', 'funct7' : '0000001', 'funct3' : '001', 'opcode' : '0110011'},
    'MULHSU'        : {'isa' : 'RV32M', 'fmt' : 'R-Type', 'funct7' : '0000001', 'funct3' : '010', 'opcode' : '0110011'},
    'MULHU'         : {'isa' : 'RV32M', 'fmt' : 'R-Type', 'funct7' : '0000001', 'funct3' : '011', 'opcode' : '0110011'},
    'DIV'           : {'isa' : 'RV32M', 'fmt' : 'R-Type', 'funct7' : '0000001', 'funct3' : '100', 'opcode' : '0110011'},
    'DIVU'          : {'isa' : 'RV32M', 'fmt' : 'R-Type', 'funct7' : '0000001', 'funct3' : '101', 'opcode' : '0110011'},
    'REM'           : {'isa' : 'RV32M', 'fmt' : 'R-Type', 'funct7' : '0000001', 'funct3' : '110', 'opcode' : '0110011'},
    'REMU'          : {'isa' : 'RV32M', 'fmt' : 'R-Type', 'funct7' : '0000001', 'funct3' : '111', 'opcode' : '0110011'},
    'LR.W'          : {'isa' : 'RV32A', 'fmt' : 'R-Type', 'funct5' : '00010', 'funct3' : '010', 'opcode' : '0101111'},
    'SC.W'          : {'isa' : 'RV32A', 'fmt' : 'R-Type', 'funct5' : '00011', 'funct3' : '010', 'opcode' : '0101111'},
    'AMOSWAP.W'     : {'isa' : 'RV32A', 'fmt' : 'R-Type', 'funct5' : '00001', 'funct3' : '010', 'opcode' : '0101111'},
    'AMOADD.W'      : {'isa' : 'RV32A', 'fmt' : 'R-Type', 'funct5' : '00000', 'funct3' : '010', 'opcode' : '0101111'},
    'AMOXOR.W'      : {'isa' : 'RV32A', 'fmt' : 'R-Type', 'funct5' : '00100', 'funct3' : '010', 'opcode' : '0101111'},
    'AMOAND.W'      : {'isa' : 'RV32A', 'fmt' : 'R-Type', 'funct5' : '01100', 'funct3' : '010', 'opcode' : '0101111'},
    'AMOOR.W'       : {'isa' : 'RV32A', 'fmt' : 'R-Type', 'funct5' : '01000', 'funct3' : '010', 'opcode' : '0101111'},
    'AMOMIN.W'      : {'isa' : 'RV32A', 'fmt' : 'R-Type', 'funct5' : '10000', 'funct3' : '010', 'opcode' : '0101111'},
    'AMOMAX.W'      : {'isa' : 'RV32A', 'fmt' : 'R-Type', 'funct5' : '10100', 'funct3' : '010', 'opcode' : '0101111'},
    'AMOMINU.W'     : {'isa' : 'RV32A', 'fmt' : 'R-Type', 'funct5' : '11000', 'funct3' : '010', 'opcode' : '0101111'},
    'AMOMAXU.W'     : {'isa' : 'RV32A', 'fmt' : 'R-Type', 'funct5' : '11100', 'funct3' : '010', 'opcode' : '0101111'},
    # B-Type
    'BEQ'           : {'isa' : 'RV32I', 'fmt' : 'B-Type', 'funct3' : '000', 'opcode' : '1100011'},
    'BNE'           : {'isa' : 'RV32I', 'fmt' : 'B-Type', 'funct3' : '001', 'opcode' : '1100011'},
    'BLT'           : {'isa' : 'RV32I', 'fmt' : 'B-Type', 'funct3' : '100', 'opcode' : '1100011'},
    'BGE'           : {'isa' : 'RV32I', 'fmt' : 'B-Type', 'funct3' : '101', 'opcode' : '1100011'},
    'BLTU'          : {'isa' : 'RV32I', 'fmt' : 'B-Type', 'funct3' : '110', 'opcode' : '1100011'},
    'BGEU'          : {'isa' : 'RV32I', 'fmt' : 'B-Type', 'funct3' : '111', 'opcode' : '1100011'},
    # U-Type
    'AUIPC'         : {'isa' : 'RV32I', 'fmt' : 'U-Type', 'opcode' : '0010111'},
    'LUI'           : {'isa' : 'RV32I', 'fmt' : 'U-Type', 'opcode' : '0110111'},
    # J-Type
    'JAL'           : {'isa' : 'RV32I', 'fmt' : 'J-Type', 'opcode' : '1101111'},
    # R4-Type
    'FMADD.S'       : {'isa' : 'RV32F', 'fmt' : 'R4-Type', 'fp_fmt' : FP_FMT['S'], 'funct3' : '111', 'opcode' : '1000011'},
    'FMSUB.S'       : {'isa' : 'RV32F', 'fmt' : 'R4-Type', 'fp_fmt' : FP_FMT['S'], 'funct3' : '111', 'opcode' : '1000111'},
    'FNMADD.S'      : {'isa' : 'RV32F', 'fmt' : 'R4-Type', 'fp_fmt' : FP_FMT['S'], 'funct3' : '111', 'opcode' : '1001111'},
    'FNMSUB.S'      : {'isa' : 'RV32F', 'fmt' : 'R4-Type', 'fp_fmt' : FP_FMT['S'], 'funct3' : '111', 'opcode' : '1001011'},
    # CR-Type
    'C.JR'          : {'isa' : 'RV32C', 'fmt' : 'CR-Type', 'funct4' : '1000', 'opcode' : '10'},
    'C.JALR'        : {'isa' : 'RV32C', 'fmt' : 'CR-Type', 'funct4' : '1001', 'opcode' : '10'},
    'C.MV'          : {'isa' : 'RV32C', 'fmt' : 'CR-Type', 'funct4' : '1000', 'opcode' : '10'},
    'C.ADD'         : {'isa' : 'RV32C', 'fmt' : 'CR-Type', 'funct4' : '1001', 'opcode' : '10'},
    # CI-Type
    'C.LWSP'        : {'isa' : 'RV32C', 'fmt' : 'CI-Type', 'funct3' : '010', 'opcode' : '10'},
    'C.FLWSP'       : {'isa' : 'RV32C', 'fmt' : 'CI-Type', 'funct3' : '011', 'opcode' : '10'},
    'C.LI'          : {'isa' : 'RV32C', 'fmt' : 'CI-Type', 'funct3' : '010', 'opcode' : '01'},
    'C.LUI'         : {'isa' : 'RV32C', 'fmt' : 'CI-Type', 'funct3' : '011', 'opcode' : '01'},
    'C.ADDI'        : {'isa' : 'RV32C', 'fmt' : 'CI-Type', 'funct3' : '000', 'opcode' : '01'},
    'C.ADDI16SP'    : {'isa' : 'RV32C', 'fmt' : 'CI-Type', 'funct3' : '011', 'opcode' : '01'},
    'C.SLLI'        : {'isa' : 'RV32C', 'fmt' : 'CI-Type', 'funct3' : '000', 'opcode' : '10'},
    'C.NOP'         : {'isa' : 'RV32C', 'fmt' : 'CI-Type', 'funct3' : '000', 'opcode' : '01'},
    # CSS-Type
    'C.SWSP'        : {'isa' : 'RV32C', 'fmt' : 'CSS-Type', 'funct3' : '110', 'opcode' : '10'},
    'C.FSWSP'       : {'isa' : 'RV32C', 'fmt' : 'CSS-Type', 'funct3' : '111', 'opcode' : '10'},
    # CIW-Type
    'C.ADDI4SPN'    : {'isa' : 'RV32C', 'fmt' : 'CIW-Type', 'funct3' : '000', 'opcode' : '00'},
    # CL-Type
    'C.LW'          : {'isa' : 'RV32C', 'fmt' : 'CL-Type', 'funct3' : '010', 'opcode' : '00'},
    'C.FLW'         : {'isa' : 'RV32C', 'fmt' : 'CL-Type', 'funct3' : '011', 'opcode' : '00'},
    # CS-Type
    'C.SW'          : {'isa' : 'RV32C', 'fmt' : 'CS-Type', 'funct3' : '110', 'opcode' : '00'},
    'C.FSW'         : {'isa' : 'RV32C', 'fmt' : 'CS-Type', 'funct3' : '111', 'opcode' : '00'},
    # CA-Type
    'C.AND'         : {'isa' : 'RV32C', 'fmt' : 'CA-Type', 'funct6' : '100011', 'funct2' : '11', 'opcode' : '01'},
    'C.OR'          : {'isa' : 'RV32C', 'fmt' : 'CA-Type', 'funct6' : '100011', 'funct2' : '10', 'opcode' : '01'},
    'C.XOR'         : {'isa' : 'RV32C', 'fmt' : 'CA-Type', 'funct6' : '100011', 'funct2' : '01', 'opcode' : '01'},
    'C.SUB'         : {'isa' : 'RV32C', 'fmt' : 'CA-Type', 'funct6' : '100011', 'funct2' : '00', 'opcode' : '01'},
    # CB-Type
    'C.BEQZ'        : {'isa' : 'RV32C', 'fmt' : 'CB-Type', 'funct3' : '110', 'opcode' : '01'},
    'C.BNEZ'        : {'isa' : 'RV32C', 'fmt' : 'CB-Type', 'funct3' : '111', 'opcode' : '01'},
    'C.SRLI'        : {'isa' : 'RV32C', 'fmt' : 'CB-Type', 'funct3' : '100', 'shamt5' : '0', 'funct2' : '00', 'opcode' : '01'},
    'C.SRAI'        : {'isa' : 'RV32C', 'fmt' : 'CB-Type', 'funct3' : '100', 'shamt5' : '0', 'funct2' : '01', 'opcode' : '01'},
    'C.ANDI'        : {'isa' : 'RV32C', 'fmt' : 'CB-Type', 'funct3' : '100', 'funct2' : '10', 'opcode' : '01'},
    # CJ-Type
    'C.J'           : {'isa' : 'RV32C', 'fmt' : 'CJ-Type', 'funct3' : '101', 'opcode' : '01'},
    'C.JAL'         : {'isa' : 'RV32C', 'fmt' : 'CJ-Type', 'funct3' : '001', 'opcode' : '01'},
    } 
REGISTER = {
    'zero' : "x0",
    'ra'  :  "x1",
    'sp'  :  "x2",
    'gp'  :  "x3",
    'tp'  :  "x4",
    't0'  :  "x5",
    't1'  :  "x6",
    't2'  :  "x7",
    's0'  :  "x8",
    's1'  :  "x9",
    'a0'  :  "x10",
    'a1'  :  "x11",
    'a2'  :  "x12",
    'a3'  :  "x13",
    'a4'  :  "x14",
    'a5'  :  "x15",
    'a6'  :  "x16",
    'a7'  :  "x17",
    's2'  :  "x18",
    's3'  :  "x19",
    's4'  :  "x20",
    's5'  :  "x21",
    's6'  :  "x22",
    's7'  :  "x23",
    's8'  :  "x24",
    's9'  :  "x25",
    's10' : "x26",
    's11' : "x27",
    't3'  :  "x28",
    't4'  :  "x29",
    't5'  :  "x30",
    't6'  :  "x31",
    'fp'  :  "x8"  # at bottom to conserve order for ABI indexing
    }

FLOAT_REGISTER = {
    'ft0':  "f0",
    'ft1':  "f1",
    'ft2':  "f2",
    'ft3':  "f3",
    'ft4':  "f4",
    'ft5':  "f5",
    'ft6':  "f6",
    'ft7':  "f7",
    'fs0':  "f8",
    'fs1':  "f9",
    'fa0':  "f10",
    'fa1':  "f11",
    'fa2':  "f12",
    'fa3':  "f13",
    'fa4':  "f14",
    'fa5':  "f15",
    'fa6':  "f16",
    'fa7':  "f17",
    'fs2':  "f18",
    'fs3':  "f19",
    'fs4':  "f20",
    'fs5':  "f21",
    'fs6':  "f22",
    'fs7':  "f23",
    'fs8':  "f24",
    'fs9':  "f25",
    'fs10': "f26",
    'fs11': "f27",
    'ft8':  "f28",
    'ft9':  "f29",
    'ft10': "f30",
    'ft11': "f31",
    }

def DecimalToBin(Dec, nbit = 32):
    #Convert from decimal to 2's complement 
    Dec = Dec % 2**nbit
    Dec = bin(2**nbit + Dec)[3:].rjust(nbit, '1') if Dec > 2**(nbit-1)-1 else bin(Dec)[2:].zfill(nbit)
    return Dec

def ABItoRegNum(reg, floatReg = False):
    #Convert from ABI name to x<num>, f<num>
    try:
        if floatReg:
            return FLOAT_REGISTER[reg]
        else:
            return REGISTER[reg]
    except KeyError:
        return reg

def encLOAD(a, label):
    isFrd = DATA[a[0]]['isa'] == "RV32F"
    if len(a) != 5:
        raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
    else:
        if isFrd:
            if a[1] not in list(FLOAT_REGISTER.keys()) + list(FLOAT_REGISTER.values()):
                raise Exception(f"Invalid or unknown float register format: {a[1]}")
        else:
            if a[1] not in list(REGISTER.keys()) + list(REGISTER.values()): 
                raise Exception(f"Invalid or unknown register format: {a[1]}")
            if a[3] not in list(REGISTER.keys()) + list(REGISTER.values()):
                raise Exception(f"Invalid or unknown register format: {a[3]}")
        if not a[2].isdigit():
            raise Exception(f"Invalid offset field format: {a[2]}")
        elif int(a[2]) not in range(-2**11, 2**11):
            raise Exception(f"Invalid offset field (out of range): {int(a[2])}")
            
    rd = DecimalToBin(int(ABItoRegNum(a[1], isFrd)[1:]), 5) 
    rs1 = DecimalToBin(int(ABItoRegNum(a[3])[1:]), 5)
    offset = DecimalToBin(int(a[2]), 12)
    return offset + rs1 + DATA[a[0]]['funct3'] + rd + DATA[a[0]]['opcode']

def encOP_IMM(a, label):
    if a[0] == 'NOP':
        if len(a) != 2:
            raise Exception(f"Invalid instruction format {' '.join(a[:len(a)-1])}")
    else:
        if len(a) != 5:
            raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
        else:
            if a[1] not in list(REGISTER.keys()) + list(REGISTER.values()):
                raise Exception(f"Invalid or unknown register format: {a[1]}")
            if a[2] not in list(REGISTER.keys()) + list(REGISTER.values()):
                raise Exception(f"Invalid or unknown register format: {a[2]}")
            if a[0] in ['SLLI', 'SRLI', 'SRAI']:
                if not a[3].isdigit():
                    raise Exception(f"Insvalid shamt field format: {a[3]}")
                elif int(a[3]) not in range(0, 2**5):
                    raise Exception(f"Invalid shamt field (out of range): {a[3]}")
            elif a[0] in ['ADDI', 'SLTI', 'SLTIU', 'XORI', 'ORI', 'ANDI']:
                if a[3][0] in "+-":
                    if not a[3][1:].isdigit():
                        raise Exception(f"Invalid imme field format: {a[3]}")
                elif not a[3].isdigit():
                    raise Exception(f"Invalid imme field format: {a[3]}")
                elif int(a[3]) not in range(-2**11, 2**11):
                    raise Exception(f"Invalid imme field (out of range): {a[3]}")
        
    rd = DecimalToBin(int(ABItoRegNum(a[1])[1:]), 5) 
    rs1 = DecimalToBin(int(ABItoRegNum(a[2])[1:]), 5)
    imme = DecimalToBin(int(a[3]), 12)
    if a[0] == 'NOP':
        return '00000000000000000000000000010011'
    elif a[0] in ['SRLI', 'SLLI', 'SRAI']:
        return DATA[a[0]]['funct7'] + imme[7:] + rs1 + DATA[a[0]]['funct3'] + rd + DATA[a[0]]['opcode']
    else:
        return imme + rs1 + DATA[a[0]]['funct3'] + rd + DATA[a[0]]['opcode']

def encJALR(a, label):
    if len(a) != 5:
        raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
    else:
        if a[1] not in list(REGISTER.keys()) + list(REGISTER.values()): 
            raise Exception(f"Invalid or unknown register format: {a[1]}")
        if a[3] not in list(REGISTER.keys()) + list(REGISTER.values()):
            raise Exception(f"Invalid or unknown register format: {a[3]}")
        if not a[2].isdigit():
            raise Exception(f"Invalid offset format: {a[2]}")
        else:
            if int(a[2]) not in range(-2**11, 2**11):
                raise Exception(f"Invalid offset field (out of range): {a[2]}")
        
    rd = DecimalToBin(int(ABItoRegNum(a[1])[1:]), 5) 
    rs1 = DecimalToBin(int(ABItoRegNum(a[3])[1:]), 5)
    imme = DecimalToBin(int(a[2]), 12)
    return imme + rs1 + DATA[a[0]]['funct3'] + rd + DATA[a[0]]['opcode']

def encSTORE(a, label):
    isFrs2 = DATA[a[0]]['isa'] == "RV32F"
    if len(a) != 5:
        raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
    else:
        if isFrs2:
            if a[1] not in list(FLOAT_REGISTER.keys()) + list(FLOAT_REGISTER.values()):
                raise Exception(f"Invalid or unknown float register format: {a[1]}")
        else:
            if a[1] not in list(REGISTER.keys()) + list(REGISTER.values()): 
                raise Exception(f"Invalid or unknown register format: {a[1]}")
            if a[3] not in list(REGISTER.keys()) + list(REGISTER.values()):
                raise Exception(f"Invalid or unknown register format: {a[3]}")
        if not a[2].isdigit():
            raise Exception(f"Invalid offset field format: {a[2]}")
        elif int(a[2]) not in range(-2**11, 2**11):
            raise Exception(f"Invalid offset field (out of range): {int(a[2])}")
        
    rs2 = DecimalToBin(int(ABItoRegNum(a[1], isFrs2)[1:]), 5) 
    rs1 = DecimalToBin(int(ABItoRegNum(a[3])[1:]), 5)
    offset = DecimalToBin(int(a[2]), 12)
    return offset[:7] + rs2 + rs1 + DATA[a[0]]['funct3'] + offset[7:] + DATA[a[0]]['opcode']

def encOP_FP(a, label):
    isFrd = True 
    isFrs1 = True
    if DATA[a[0]]['funct5'][0] == '1':
        if DATA[a[0]]['funct5'][3] == '0':
            isFrd = False 
        else:
            isFrs1 = False
    if a[0] in ['FSQRT.S', 'FCVT.S.W', 'FCVT.S.WU', 'FCVT.W.S', 'FCVT.WU.S', 'FMV.X.W', 'FMV.W.X', 'FCLASS.S']:
        if len(a) != 4:
            raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
    else:
        if len(a) != 5:
            raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
        
    if isFrd:
        if a[1] not in list(FLOAT_REGISTER.keys()) + list(FLOAT_REGISTER.values()):
            raise Exception(f"Invalid or unknown float register format: {a[1]}")
    else:
        if a[1] not in list(REGISTER.keys()) + list(REGISTER.values()): 
            raise Exception(f"Invalid or unknown register format: {a[1]}")
    if isFrs1:
        if a[2] not in list(FLOAT_REGISTER.keys()) + list(FLOAT_REGISTER.values()):
            raise Exception(f"Invalid or unknown float register format: {a[2]}")
    else:
        if a[2] not in list(REGISTER.keys()) + list(REGISTER.values()): 
            raise Exception(f"Invalid or unknown register format: {a[2]}")
    if len(a) == 5:
        if a[3] not in list(FLOAT_REGISTER.keys()) + list(FLOAT_REGISTER.values()):
            raise Exception(f"Invalid or unknown float register format: {a[3]}")
    
    rs1 = DecimalToBin(int(ABItoRegNum(a[2], isFrs1)[1:]), 5)
    rd = DecimalToBin(int(ABItoRegNum(a[1], isFrd)[1:]), 5)
    if len(a) == 5:
        rs2 = DecimalToBin(int(ABItoRegNum(a[3], True)[1:]), 5) 
    elif len(a) == 4:
        if a[0] in ['FCVT.WU.S', 'FCVT.S.WU']:
            rs2 = '00001'
        else:
            rs2 = '00000'
    return DATA[a[0]]['funct5'] + DATA[a[0]]['fp_fmt'] + rs2 + rs1 + DATA[a[0]]['funct3'] + rd + DATA[a[0]]['opcode']

def encOP(a, label):
    if len(a) != 5:
        raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
    else:
        if a[1] not in list(REGISTER.keys()) + list(REGISTER.values()):
            raise Exception(f"Invalid or unknown register format: {a[1]}")
        if a[2] not in list(REGISTER.keys()) + list(REGISTER.values()):
            raise Exception(f"Invalid or unknown register format: {a[2]}")
        if a[3] not in list(REGISTER.keys()) + list(REGISTER.values()):
            raise Exception(f"Invalid or unknown register format: {a[3]}")
        
    rs2 = DecimalToBin(int(ABItoRegNum(a[3])[1:]), 5)
    rs1 = DecimalToBin(int(ABItoRegNum(a[2])[1:]), 5)
    rd = DecimalToBin(int(ABItoRegNum(a[1])[1:]), 5)
    return DATA[a[0]]['funct7'] + rs2 + rs1 + DATA[a[0]]['funct3'] + rd + DATA[a[0]]['opcode']

def encAMO(a, label):
    if a[0] == "LR.W":
        if len(a) != 4:
            raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
    else:
        if len(a) != 5:
            raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
        
    if a[1] not in list(REGISTER.keys()) + list(REGISTER.values()):
        raise Exception(f"Invalid or unknown register format: {a[1]}")
    if a[2] not in list(REGISTER.keys()) + list(REGISTER.values()):
        raise Exception(f"Invalid or unknown register format: {a[2]}")
    if len(a) == 5:
        if a[3] not in list(REGISTER.keys()) + list(REGISTER.values()):
            raise Exception(f"Invalid or unknown register format: {a[3]}") 
    aq = '0'
    rl = '0'
    if a[0] == 'LR.W':
        rs2 = '00000'  
        rs1 = DecimalToBin(int(ABItoRegNum(a[2])[1:]), 5) 
    else:
        rs2 = DecimalToBin(int(ABItoRegNum(a[2])[1:]), 5)
        rs1 = DecimalToBin(int(ABItoRegNum(a[3])[1:]), 5) 
    rd = DecimalToBin(int(ABItoRegNum(a[1])[1:]), 5)
    return DATA[a[0]]['funct5'] + aq + rl + rs2 + rs1 + DATA[a[0]]['funct3'] + rd + DATA[a[0]]['opcode']

def encBRANCH(a, label):
    if len(a) != 5:
        raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
    else:
        if a[1] not in list(REGISTER.keys()) + list(REGISTER.values()):
            raise Exception(f"Invalid or unknown register format: {a[1]}")
        if a[2] not in list(REGISTER.keys()) + list(REGISTER.values()):
            raise Exception(f"Invalid or unknown register format: {a[2]}")
        if not a[3].isdigit():
            if a[3] not in label.keys():
                raise Exception(f"Invalid offset field (undefined label): {a[3]}")
            if label[a[3]] - a[len(a) - 1] not in range(-2**12, 2**12):
                raise Exception(f"Invalid offset field (target out of range): {a[3]}")
        else:
            if int(a[3]) not in range(-2**12, 2**12):
                raise Exception(f"Invalid offset field (target out of range): {a[3]}")
             
    rs2 = DecimalToBin(int(ABItoRegNum(a[2])[1:]), 5)
    rs1 = DecimalToBin(int(ABItoRegNum(a[1])[1:]), 5)
    #Convert label to address
    imme = DecimalToBin(int(a[3]), 13) if a[3].isdigit() else DecimalToBin(label[a[3]] - a[len(a) - 1], 13)
    return imme[0] + imme[2:8] + rs2 + rs1 + DATA[a[0]]['funct3'] + imme[8:12] + imme[1] + DATA[a[0]]['opcode']

def encUType(a, label):
    if len(a) != 4:
        raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
    else:
        if a[1] not in list(REGISTER.keys()) + list(REGISTER.values()):
            raise Exception(f"Invalid or unknown register format: {a[1]}")
        if not a[2].isdigit():
            raise Exception(f"Invalid imme field format: {a[2]}")
        else:
            if int(a[2]) not in range(-2**31, 2**31):
                raise Exception(f"Invalid imme field (out of range): {a[2]}")
            
    imme = DecimalToBin(int(a[2]), 20)
    rd = DecimalToBin(int(ABItoRegNum(a[1])[1:]), 5)
    return imme + rd + DATA[a[0]]['opcode']

def encJAL(a, label):
    if len(a) != 4:
        raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
    else:
        if a[1] not in list(REGISTER.keys()) + list(REGISTER.values()):
            raise Exception(f"Invalid or unknown register format: {a[1]}")
        if not a[2].isdigit():
            if a[2] not in label.keys():
                raise Exception(f"Invalid offset field (undefined label): {a[2]}")
            if label[a[2]] - a[len(a) - 1] not in range(-2**20, 2**20):
                raise Exception(f"Invalid offset field (target out of range): {a[2]}")
        else:
            if int(a[2]) not in range(-2**20, 2**20):
                raise Exception(f"Invalid offset field (target out of range): {a[2]}")
    #Convert label to address
    imme = DecimalToBin(int(a[2]), 21) if a[2].isdigit() else DecimalToBin(label[a[2]] - a[len(a) - 1], 21)
    rd = DecimalToBin(int(ABItoRegNum(a[1])[1:]), 5)
    return imme[0] + imme[10:20] + imme[9] + imme[1:9] + rd + DATA[a[0]]['opcode']

def encR4Type(a, label):
    if len(a) != 6:
        raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
    else:
        if a[1] not in list(FLOAT_REGISTER.keys()) + list(FLOAT_REGISTER.values()):
            raise Exception(f"Invalid or unknown float register format: {a[1]}")
        if a[2] not in list(FLOAT_REGISTER.keys()) + list(FLOAT_REGISTER.values()):
            raise Exception(f"Invalid or unknown float register format: {a[2]}")
        if a[3] not in list(FLOAT_REGISTER.keys()) + list(FLOAT_REGISTER.values()):
            raise Exception(f"Invalid or unknown float register format: {a[3]}") 
        if a[4] not in list(FLOAT_REGISTER.keys()) + list(FLOAT_REGISTER.values()):
            raise Exception(f"Invalid or unknown float register format: {a[4]}")
        
    rs3 = DecimalToBin(int(ABItoRegNum(a[4], True)[1:]), 5)
    rs2 = DecimalToBin(int(ABItoRegNum(a[3], True)[1:]), 5)
    rs1 = DecimalToBin(int(ABItoRegNum(a[2], True)[1:]), 5)
    rd = DecimalToBin(int(ABItoRegNum(a[1], True)[1:]), 5)
    return rs3 + DATA[a[0]]['fp_fmt'] + rs2 + rs1 + DATA[a[0]]['funct3'] + rd + DATA[a[0]]['opcode']

def encCR(a, label): 
    if a[0] in ['C.JR', 'C.JALR']:
        if len(a) != 3:
            raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
    else:
        if len(a) != 4:
            raise Exception(f"Invalid instruction format: {' '.join(a[:len(a)-1])}")
    if a[1] not in list(REGISTER.keys()) + list(REGISTER.values()):
        raise Exception(f"Invalid register format: {a[1]}")
    if len(a) == 4:
        if a[2] not in list(REGISTER.keys()) + list(REGISTER.values()):
            raise Exception(f"Invalid register format: {a[2]}")
        
    if len(a) == 3:
        rs2 = '00000'
    elif len(a) == 4:
        rs2 = DecimalToBin(int(ABItoRegNum(a[2])[1:]), 5)
    rd_rs1 = DecimalToBin(int(ABItoRegNum(a[1])[1:]), 5)
    return DATA[a[0]]['funct4'] + rd_rs1 + rs2 + DATA[a[0]]['opcode']

def encCI(a, label): 
    if a[0] == 'C.NOP':
        return '0000000000000001'
    elif a[0] == 'C.ADDI16SP':
        imme = DecimalToBin(int(a[1]), 10)
        rd = '00010'
        return DATA[a[0]]['funct3'] + imme[0] + rd + imme[5] + imme[3] + imme[1:3] + imme[4] + DATA[a[0]]['opcode']
    elif a[0] in ['C.FLWSP', 'C.LWSP']:
        isFrd = True if a[0] == 'C.FLWSP' else False
        rd = DecimalToBin(int(ABItoRegNum(a[1], isFrd)[1:]), 5)
        imme = DecimalToBin(int(a[2]), 8)
        return DATA[a[0]]['funct3'] + imme[2] + rd + imme[3:6] + imme[0:2] + DATA[a[0]]['opcode']
    elif a[0] in ['C.LI', 'C.ADDI', 'C.SLLI']:
        rd = DecimalToBin(int(ABItoRegNum(a[1])[1:]), 5)
        imme = DecimalToBin(int(a[2]), 6)
        return DATA[a[0]]['funct3'] + imme[0] + rd + imme[1:] + DATA[a[0]]['opcode']
    elif a[0] == 'C.LUI':
        rd = DecimalToBin(int(ABItoRegNum(a[1])[1:]), 5)
        imme = DecimalToBin(int(a[2]), 6)
        return DATA[a[0]]['funct3'] + imme[0] + rd + imme[1:] + DATA[a[0]]['opcode']
        
def encCSS(a, label): 
    isFrs2 = True if a[0] in ['C.FSWSP'] else False
    imme = DecimalToBin(int(a[2]), 8)
    rs2 = DecimalToBin(int(ABItoRegNum(a[1], isFrs2)[1:]), 5)
    return DATA[a[0]]['funct3'] + imme[2:6] + imme[0:2] + rs2 + DATA[a[0]]['opcode']
    
def encCIW(a, label): 
    imme = DecimalToBin(int(a[2]), 9)
    rd = DecimalToBin(int(ABItoRegNum(a[1])[1:]), 3)
    return DATA[a[0]]['funct3'] + imme[5:7] + imme[1:5] + imme[8] + imme[7] + rd + DATA[a[0]]['opcode']
    
def encCL(a, label): 
    isFrd = True if a[0] in ['C.FLW'] else False
    imme = DecimalToBin(int(a[2]), 7)
    rd = DecimalToBin(int(ABItoRegNum(a[1], isFrd)[1:]), 3)
    rs1 = DecimalToBin(int(ABItoRegNum(a[3])[1:]), 3)
    return DATA[a[0]]['funct3'] + imme[1:4] + rs1 + imme[4] + imme[0] + rd + DATA[a[0]]['opcode']

def encCS(a, label): 
    isFrs2 = True if a[0] in ['C.FSW'] else False
    imme = DecimalToBin(int(a[2]), 7)
    rs1 = DecimalToBin(int(ABItoRegNum(a[3])[1:]), 3)
    rs2 = DecimalToBin(int(ABItoRegNum(a[1], isFrs2)[1:]), 3)
    return DATA[a[0]]['funct3'] + imme[2:5] + rs1 + imme[5] + imme[1] + rs2 + DATA[a[0]]['opcode']
    
def encCA(a, label): 
    rd_rs1 = DecimalToBin(int(ABItoRegNum(a[1])[1:]), 3)
    rs2 = DecimalToBin(int(ABItoRegNum(a[2])[1:]), 3)
    return DATA[a[0]]['funct6'] + rd_rs1 + DATA[a[0]]['funct2'] + rs2 + DATA[a[0]]['opcode']

def encCB(a, label): 
    imme = DecimalToBin(int(a[2]), 9) if a[2].isdigit() else DecimalToBin(label[a[2]] - a[len(a) - 1], 9)
    rd_rs1 = DecimalToBin(int(ABItoRegNum(a[1])[1:]), 3)
    if a[0] in ['C.BEQZ', 'C.BNEZ']:
        return DATA[a[0]]['funct3'] + imme[0] + imme[4:6] + rd_rs1 + imme[1:3] + imme[6:8] + imme[3] + DATA[a[0]]['opcode']
    elif a[0] in ['C.SRLI', 'C.SRAI']:
        return DATA[a[0]]['funct3'] + DATA[a[0]]['shamt5'] + DATA[a[0]]['funct2'] + rd_rs1 + imme[4:9] + DATA[a[0]]['opcode']
    elif a[0] in ['C.ANDI']:
        return DATA[a[0]]['funct3'] + imme[3] + DATA[a[0]]['funct2'] + rd_rs1 + imme[4:9] + DATA[a[0]]['opcode']
    
def encCJ(a, label): 
    imme = DecimalToBin(int(a[1]), 12) if a[1].isdigit() else DecimalToBin(label[a[1]] - a[len(a) - 1], 12)
    return DATA[a[0]]['funct3'] + imme[0] + imme[7] + imme[2:4] + imme[1] + imme[5] + imme[4] + imme[8:11] + imme[6] + DATA[a[0]]['opcode']
    
def FileSetup(a):
    #label = []
    label = {}
    ins = []
    idx = 0
    for i in range(len(a)):
        if a[i].find('#') != -1:
            a[i] = a[i].replace(a[i][a[i].find('#'):], '') 
        if a[i].find('/') != -1:
            a[i] = a[i].replace(a[i][a[i].find('/'):], '')
        if a[i].find('(') != -1:
            a[i] = a[i].replace('(', ' ')
        if a[i].find(')') != -1:
            a[i] = a[i].replace(')', ' ')
        if a[i].find(',') != -1:
            a[i] = a[i].replace(',', ' ')
        a[i] = a[i].split()
    a = [i for i in a if i != [] and i[0].lower() not in ['.data', '.text']]    
    '''for i in a:
        if len(i) > 1:
            if i[0].endswith(":"): 
                #label.append([i[0], idx])
                label.update({i[0][:-1] : idx})
                idx = idx + 4
                i.remove(i[0])
            else:
                idx = idx + 4
        else:
            if i[0].endswith(":"): 
                #label.append([i[0], idx])
                label.update({i[0][:-1] : idx})
                a.remove(i)'''
    i = 0
    temp = len(a)
    while i < temp:
        if len(a[i]) > 1:
            if a[i][0].endswith(":"):
                label.update({a[i][0][:-1] : idx})
                a[i].append(idx)
                idx = idx + 4 if not a[i][1].upper().startswith("C.") else idx + 2
                a[i].remove(a[i][0])
                i = i + 1
            else:
                a[i].append(idx)
                idx = idx + 4 if not a[i][0].upper().startswith("C.") else idx + 2
                i = i + 1
        else:
            if a[i][0].endswith(":"): 
                label.update({a[i][0][:-1] : idx})
                a.remove(a[i])
                temp = temp - 1
            else:
                if not a[i][0].upper().startswith("C."):
                    a[i].append(idx)
                    idx = idx + 4
                    i = i + 1
                else:
                    a[i].append(idx)
                    idx = idx + 2
                    i = i + 1
    for i in range(len(a)):
        a[i][0] = a[i][0].upper()
    return a, label

def recursive(a, out, a32):
    flag = 0
    try:
        os.chdir(a)
        print(a)
    except NotADirectoryError:
        print(a)
        flag = 1
        if a.endswith('.S'):
            ins = []
            d = a
            d = d.replace(os.getcwd().replace('\\', '/') + '/', '')
            f = open(a, 'r')
            a = f.readlines()
            f.close()
            a, label = FileSetup(a)
            #print(a)
            for i in a:
                print(i)
                if DATA[i[0]]['isa'] == 'RV32C':
                    if DATA[i[0]]['fmt'] == 'CR-Type':
                        ins.append(encCR(i, label))
                    elif DATA[i[0]]['fmt'] == 'CI-Type':
                        ins.append(encCI(i, label))
                    elif DATA[i[0]]['fmt'] == 'CSS-Type':
                        ins.append(encCSS(i, label))
                    elif DATA[i[0]]['fmt'] == 'CIW-Type':
                        ins.append(encCIW(i, label))
                    elif DATA[i[0]]['fmt'] == 'CL-Type':
                        ins.append(encCL(i, label))
                    elif DATA[i[0]]['fmt'] == 'CS-Type':
                        ins.append(encCS(i, label))
                    elif DATA[i[0]]['fmt'] == 'CA-Type':
                        ins.append(encCA(i, label))
                    elif DATA[i[0]]['fmt'] == 'CB-Type':
                        ins.append(encCB(i, label))
                    elif DATA[i[0]]['fmt'] == 'CJ-Type':
                        ins.append(encCJ(i, label))
                    else:
                        raise Exception("Invalid Instruction")
                else:
                    if DATA[i[0]]['opcode'] == OPCODE['OP']:
                        ins.append(encOP(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['OP_FP']:
                        ins.append(encOP_FP(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['AMO']:
                        ins.append(encAMO(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['JALR']:
                        ins.append(encJALR(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['LOAD']:
                        ins.append(encLOAD(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['LOAD_FP']:
                        ins.append(encLOAD(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['OP_IMM']:
                        ins.append(encOP_IMM(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['STORE']:
                        ins.append(encSTORE(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['STORE_FP']:
                        ins.append(encSTORE(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['BRANCH']:
                        ins.append(encBRANCH(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['LUI']:
                        ins.append(encUType(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['AUIPC']:
                        ins.append(encUType(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['JAL']:
                        ins.append(encJAL(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['MADD']:
                        ins.append(encR4Type(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['MSUB']:
                        ins.append(encR4Type(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['NMADD']:
                        ins.append(encR4Type(i, label))
                    elif DATA[i[0]]['opcode'] == OPCODE['NMSUB']:
                        ins.append(encR4Type(i, label))
                    else:
                        raise Exception("Invalid Instruction")
            '''ins = '\n'.join(ins)
            ins += '\n'
            path = os.getcwd()
            os.chdir(out)
            f = open(f'{d}.bin', 'w')
            f.writelines(ins)
            f.close()
            os.chdir(path)   '''
            
            ''''''''''''''''''
            
            if a32:
                i = 0
                temp = ins
                ins = ''
                _flag = False
                while(i < len(temp)):
                    if len(temp[i]) == 16:
                        if i == len(temp) - 1:
                            ins = ins + '0'*16 + temp[i] + '\n'
                            break
                        else:
                            if len(temp[i+1]) == 32:
                                ins = ins + temp[i+1][16:32] + temp[i] + '\n'
                                _flag = True
                                i = i + 1
                            elif len(temp[i+1]) == 16:
                                ins = ins + temp[i+1][:16] + temp[i] + '\n'
                                _flag = False
                                i = i + 2
                    else:
                        if flag:
                            if i == len(temp) - 1:
                                ins = ins + '0'*16 + temp[i][:16] + '\n'
                                i = i + 1
                                break
                            ins = ins + temp[i+1][:16] + temp[i][:16] + '\n'
                            if len(temp[i+1]) == 32:
                                _flag = True
                                i = i + 1
                            elif len(temp[i+1]) == 16:
                                _flag = False
                                i = i + 2
                        else:
                            ins = ins + temp[i] + '\n'
                            i = i + 1
                    print(i)
                
            path = os.getcwd()
            os.chdir(out)
            f = open(f'{d}.bin', 'w')
            f.writelines(ins)
            f.close()
            os.chdir(path) 
    if flag == 0:
        List = os.listdir()
        print(List)
        if len(List) != 0:
            _flag = False
            for i in List:
                if i.find('.S') != -1:
                    out = out + f'/{os.path.basename(os.getcwd())}'
                    if os.path.exists(out):
                        pass
                    else:
                        os.mkdir(out)
                    _flag = True
                    break
            for i in List:
                recursive(i, out, a32)
                if List.index(i) == len(List) - 1:
                    try:
                        os.chdir(os.path.dirname(os.getcwd()))
                        if _flag:
                            out = out.replace('/' + os.path.basename(os.getcwd()), '')
                    except: pass
        else:
            try: os.chdir(os.path.dirname(os.getcwd()))
            except: pass
if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-o", "--output", help = "-o: Directory where the binary files are generated in")
    ap.add_argument("-i", "--input", help = "-i: Directory of assembly files that should be converted to binary files recursively")
    #ap.add_argument("-a16", "--align16", help = "-o: InsMem will have 16-bit width", action = "store_true")
    ap.add_argument("-a32", "--align32", help = "-o: InsMem will have 32-bit width", action= "store_true")
    args = ap.parse_args()
    _out = args.output
    _in  = args.input
    #a16 = args.a16
    a32 = args.align32
    if os.path.exists(_out):
        pass
    else:
        os.mkdir(_out)
    os.chdir(_out)
    chdir = []
    recursive(_in, _out, a32)
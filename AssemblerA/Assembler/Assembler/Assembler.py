
import os
import argparse

#Chuyen bin sang hex
dict_hex = {
    '0000' : '0',
    '0001' : '1',
    '0010' : '2',
    '0011' : '3',
    '0100' : '4',
    '0101' : '5',
    '0110' : '6',
    '0111' : '7',
    '1000' : '8',
    '1001' : '9',
    '1010' : 'A',
    '1011' : 'B',
    '1100' : 'C',
    '1101' : 'D',
    '1110' : 'E',
    '1111' : 'F'
    }
#khai báo các thanh ghi
Reg = {
       'zero'   : 'x0',
       'ra'     : 'x1',
       'sp'     : 'x2',
       'gp'     : 'x3',
       'tp'     : 'x4',
       't0'     : 'x5',
       't1'     : 'x6',
       't2'     : 'x7',
       's0'     : 'x8',
       'fp'     : 'x8',
       's1'     : 'x9',
       'a0'     : 'x10',
       'a1'     : 'x11',
       'a2'     : 'x12',
       'a3'     : 'x13',
       'a4'     : 'x14',
       'a5'     : 'x15',
       'a6'     : 'x16',
       'a7'     : 'x17',
       's2'     : 'x18',
       's3'     : 'x19',
       's4'     : 'x20',
       's5'     : 'x21',
       's6'     : 'x22',
       's7'     : 'x23',
       's8'     : 'x24',
       's9'     : 'x25',
       's10'    : 'x26',
       's11'    : 'x27',
       't3'     : 'x28',
       't4'     : 'x29', 
       't5'     : 'x30', 
       't6'     : 'x31',
       }
dict_reg = {
    'x0' : '00000' ,
    'x1' : '00001' ,
    'x2' : '00010' ,
    'x3' : '00011' ,
    'x4' : '00100' ,
    'x5' : '00101' ,
    'x6' : '00110' ,
    'x7' : '00111' ,
    'x8' : '01000' ,
    'x9' : '01001' ,
    'x10' : '01010' ,
    'x11' : '01011' ,
    'x12' : '01100' ,
    'x13' : '01101' ,
    'x14' : '01110' ,
    'x15' : '01111' ,
    'x16' : '10000' ,
    'x17' : '10001' ,
    'x18' : '10010' ,
    'x19' : '10011' ,
    'x20' : '10100' ,
    'x21' : '10101' ,
    'x22' : '10110' ,
    'x23' : '10111' ,
    'x24' : '11000' ,
    'x25' : '11001' ,
    'x26' : '11010' ,
    'x27' : '11011' ,
    'x28' : '11100' ,
    'x29' : '11101' ,
    'x30' : '11110' ,
    'x31' : '11111' 
    }

#khai báo opcode
op = '0101111'
dict_opcode = {
    'lr.w' : op,
    'sc.w' : op,
    'amoadd.w' : op,
    'amoand.w' : op,
    'amomax.w' : op,
    'amomaxu.w'  : op,
    'amomin.w'  : op,
    'amominu.w' : op,
    'amoor.w' : op,
    'amoswap.w' : op,
    'amoxor.w' : op,
    }

# khai báo funct3
f3 = '010'
dict_funct3 = {
    'lr.w' : f3,
    'sc.w' : f3,
    'amoadd.w' : f3,
    'amoand.w' : f3,
    'amomax.w' : f3,
    'amomaxu.w'  : f3,
    'amomin.w'  : f3,
    'amominu.w' : f3,
    'amoor.w' : f3,
    'amoswap.w' : f3,
    'amoxor.w' : f3,
    }

# khai báo 2 bit aquire và release trong funct7
dict_mop ={
    '''
    truy cập bộ nhớ không đồng bộ. Điều này có nghĩa là không có
    yêu cầu cụ thể về sự đồng bộ hóa nào đối với truy cập này. 
    Thông thường, truy cập không đồng bộ sẽ không đảm bảo thứ tự của các 
    truy cập khác nhau và không có cơ chế bảo vệ dữ liệu chia sẻ.
    '''
    
    'asynchronous' : '00',
    
    '''
    truy cập bộ nhớ với release. Truy cập này được xác định là kết thúc một 
    loạt các truy cập đồng bộ hoặc sửa đổi bộ nhớ. Trong một loạt các truy cập, 
    truy cập cuối cùng
    được ghi nhận là release, cho phép các truy cập khác đồng bộ với nó.
    '''
    
    'release' : '01',
    
    '''
    Truy cập bộ nhớ với acquire. Truy cập này được xác định là bắt đầu 
    một loạt các truy cập đồng bộ. Trong một loạt các truy cập, truy cập 
    đầu tiên được ghi nhận là acquire,
    cho phép các truy cập khác đồng bộ với nó.
    '''
   
    'accquire' : '10',
   
    '''
    Truy cập bộ nhớ đồng bộ hoàn toàn. Truy cập này được xác định là cả bắt 
    đầu và kết thúc một loạt các truy cập đồng bộ. Trong một loạt các 
    truy cập, truy cập đầu tiên được ghi nhận là acquire và truy cập cuối cùng 
    được ghi nhận là release, phép các truy cập khác đồng bộ với nó.
    '''
   
    'synchronous' : '11'
    }

dict_funct5 = {
    'lr.w' : '00010',
    'sc.w' : '00011',
    'amoadd.w' : '00000',
    'amoand.w' : '01100',
    'amomax.w' : '10100',
    'amomaxu.w'  : '11100',
    'amomin.w'  : '10000',
    'amominu.w' : '11000',
    'amoor.w' : '01000',
    'amoswap.w' : '00001',
    'amoxor.w' : '00100',
    }

dict_ins = {
    '32A' : ['lr.w', 'sc.w' , 'amoswap.w', 'amoadd.w', 'amoxor.w', 'amoand.w', 'amomax.w'
             ,'amomaxu.w', 'amomin.w', 'amominu.w', 'amoor.w' ]
    }

# dùng để chuyển đổi giá trị Imme
def decimal_to_binary(decimal_num):
    binary_num = ""
    
    # Chia liên tục cho 2 và lưu dư vào chuỗi nhị phân
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary_num = str(remainder) + binary_num
        decimal_num //= 2
    
    # Thêm các số 0 vào đầu chuỗi để đảm bảo có 5 bit
    while len(binary_num) < 5:
        binary_num = '0' + binary_num
    
    return binary_num[-5:]


#form instr Rd, Rs2, Rs1
def FileSetup(a):
    label = []
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
    for i in a:
        if len(i) > 1:
            if i[0].endswith(":"): 
                label.append([i[0], idx])
                idx = idx + 4
                i.remove(i[0])
            else:
                idx = idx + 4
        else:
            if i[0].endswith(":"): 
                label.append([i[0], idx])
                a.remove(i)
    a = [i + [j*4] for j , i in enumerate(a)]
    return a, label

def Atomic(a, label):
    global dict_funct5, dict_mop, dict_reg, dict_funct3, dict_opcode
    if a[0] in dict_ins['32A']:
        if a[1] not in dict_reg.keys() and a[2] not in dict_reg.keys():
            raise Exception("The register in rd and rs1 field must be Integer Register x0-x31")
    else:
        if a[1] not in dict_reg.keys() and a[2] not in dict_reg.keys() and a[3] not in dict_reg.keys():   
            raise Exception("The register in rd and rs2 and rs1 field must be Integer Register x0-x31")
    
    if a[0] == 'lr.w':
        return dict_funct5[a[0]] + '00' + '00000' + dict_reg[a[2]] + dict_funct3[a[0]] + dict_reg[a[1]] + dict_opcode[a[0]]
    else:
        return dict_funct5[a[0]] + '11' + dict_reg[a[2]] + dict_reg[a[3]] + dict_funct3[a[0]] + dict_reg[a[1]] + dict_opcode[a[0]]

def process_w_file(file_path, out):
    ins = []
    with open(file_path, 'r') as f:
        lines = f.readlines()
    lines, label = FileSetup(lines)
    for line in lines:
        if line[0] in dict_opcode.keys():
            ins.append(Atomic(line, label))
        else:
            raise Exception("Invalid Instruction")
    ins = '\n'.join(ins)
    ins += '\n'
    file_name = os.path.basename(file_path).split('.')[0] + '.txt'
    with open(os.path.join(out, file_name), 'w') as f:
        f.write(ins)

def ScanFile(a, out):
    if os.path.isfile(a) and a.endswith('.S'):
        process_w_file(a, out)
    elif os.path.isdir(a):
        for entry in os.listdir(a):
            entry_path = os.path.join(a, entry)
            if os.path.isfile(entry_path) and entry.endswith('.S'):
                process_w_file(entry_path, out)
            elif os.path.isdir(entry_path):
                ScanFile(entry_path, out)
    else:
        print(f"{a} is not a valid file or directory")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", required=True, help="input file name or directory")
    parser.add_argument("-o", "--output", required=True, help="output directory")
    args = parser.parse_args()

    input_path = args.input
    output_path = args.output

    print(f"Input path: {input_path}")
    print(f"Output path: {output_path}")

    if not os.path.exists(input_path):
        print(f"File or directory {input_path} does not exist.")
    else:
       if not os.path.exists(output_path):
            os.makedirs(output_path)

    ScanFile(input_path, output_path)
#! /bin/python3

assemblyDictionary = {
    "ADD"   :  "1000",
    "SHR"   :  "1001",
    "SHL"   :  "1010",
    "NOT"   :  "1011",
    "AND"   :  "1100",
    "OR"    :  "1101",
    "XOR"   :  "1110",
    "CMP"   :  "1111",

    "LOAD"  :  "0000",
    "STORE" :  "0001",
    "DATA"  :  "001000",

    "JMPR"  :  "001100",
    "JMP"   :  "01000000",

    "JZ"    :  "01010001",
    "JE"    :  "01010010",
    "JEZ"   :  "01010011",
    "JA"    :  "01010100",
    "JAZ"   :  "01010101",
    "JAE"   :  "01010110",
    "JAEZ"  :  "01010111",
    "JC"    :  "01011000",
    "JCZ"   :  "01011001",
    "JCE"   :  "01011010",
    "JCEZ"  :  "01011011",
    "JCA"   :  "01011100",
    "JCAZ"  :  "01011101",
    "JCAE"  :  "01011110",
    "JCAEZ" :  "01011111",

    "CLF"   :  "01100000",
    "END"   :  "11001111",

    "R0"    :  "00",
    "R1"    :  "01",
    "R2"    :  "10",
    "R3"    :  "11"
}


with open("program.asm", "r") as file:
    source = file.read()

    for code in assemblyDictionary:
        source = source.replace(f"{code} ",\
            f"{assemblyDictionary[code]} ")
        
        source = source.replace(f" {code}",\
            f" {assemblyDictionary[code]}")

    source = source.replace(" ", "")
    with open("program.bin", "w") as file:
        file.write(source)


with open("program.bin", "r") as fileBin:
    with open("program.hex", "w") as fileHex:
        for binaryNumber in fileBin:
            hexNumber = hex(int(binaryNumber, 2))
            fileHex.write(f"{hexNumber[2:]}\n")
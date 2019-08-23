import socket

alphabetDict = { 'A' : 1,	'B' : 2,	'C' : 3,	'D' : 4,	'E' : 5,	'F' : 6,	'G' : 7,	'H' : 8,	'I' : 9,\
               'J' : 10,	'K' : 11,	'L' : 12,	'M' : 13,	'N' : 14,	'O' : 15,	'P' : 16,	'Q' : 17,\
               'R' : 18,	'S' : 19,	'T' : 20,	'U' : 21,	'V' : 22,	'W' : 23,	'X' : 24,	'Y' : 25,\
               'Z' : 26,	'a' : 27,	'b' : 28,	'c' : 29,	'd' : 30,	'e' : 31,	'f' : 32,	'g' : 33,\
               'h' : 34,	'i' : 35,	'j' : 36,	'k' : 37,	'l' : 38,	'm' : 39,	'n' : 40,	'o' : 41,\
               'p' : 42,	'q' : 43,	'r' : 44,	's' : 45,	't' : 46,	'u' : 47,	'v' : 48,	'w' : 49,\
                'x' : 50,	'y' : 51,	'z' : 52,	' ' : 53,	'.' : 54,	'!' : 55,	'@' : 56,	'£' : 57,\
               '$' : 58,	'%' : 59,	'^' : 60,	'&' : 61,	'*' : 62,	'(' : 63,	')' : 64,	'-' : 65,\
               '_' : 66,	'+' : 67,	'{' : 68,	'}' : 69,	',' : 70,	'/' : 71,	'?' : 72,	';' : 73,\
               ':' : 74,	'#' : 75,	'|' : 76,	']' : 77}

def invertDict(inputDict):
    tempDict = {v: k for k, v in inputDict.items()}
    return tempDict

def encryptStringDict(input_string,encrypt):
    # The encryption key will normally be unique to each host and read from a file
    keyEncrypt = "Crazy Horse"
    output_string = ""
    invertAlphabet = invertDict(alphabetDict)
    for inputIndex in range(len(input_string)):
        charValue = alphabetDict[input_string[inputIndex]]
        keyValue = alphabetDict[keyEncrypt[inputIndex%len(keyEncrypt)]]
        if encrypt:
            output_string += invertAlphabet[(charValue + keyValue) %len(alphabetDict)]
        else:
            output_string += invertAlphabet[(charValue - keyValue) %len(alphabetDict)]

    return output_string

def encryptStringAscii(input_string,encrypt):
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name).replace(".", "")
    keyEncrypt = "Crazy Horse"
    output_string = ""

    for inputIndex in range(len(input_string)):
        charAscii = ord(input_string[inputIndex])
        ipAscii = int(host_ip[inputIndex%len(host_ip)])
        keyAscci = ord(keyEncrypt[inputIndex%len(keyEncrypt)])
        if encrypt:
            output_string += chr(charAscii + ipAscii + keyAscci)
        else:
            output_string += chr(charAscii - (ipAscii + keyAscci))

    return output_string

input_string  = "Hello World"

output_string = encryptStringDict(input_string,True)
print(output_string)
output_string = encryptStringDict(output_string,False)
print(output_string)
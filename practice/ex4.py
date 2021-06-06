

def hex_output():

    hex_value = input('Enter a number to convert: ')

    decnum = 0
    
    for power, digit in enumerate(reversed(hex_value)):
        decnum += int(digit, 16) * (16 ** power)

    print(decnum)    

hex_output()

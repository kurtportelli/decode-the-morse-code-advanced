def decodeBits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    import re
    
    stripped_bits = bits.strip('0')
    bits_groups = re.findall(r'(0+|1+)', stripped_bits)
    time_unit = min(len(bits_group) for bits_group in bits_groups)
    
    return stripped_bits.replace('111' * time_unit, '-').replace('1' * time_unit, '.') \
            .replace('0000000' * time_unit, '   ').replace('000' * time_unit, ' ') \
            .replace('0' * time_unit, '')

def decodeMorse(morse_code):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return ' '.join(
        ''.join(MORSE_CODE[char] for char in word.split())
        for word in morse_code.strip().split('   ')
    )

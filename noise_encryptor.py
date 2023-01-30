import numpy as np

message = 'Just for fun tra la la'

key = 256


def enc(key, message):
    encoded_message = ''

    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_low = alph.lower()
    non_alph = r'0123456789!"#$%&\'()*+,-./:;<=>?@ [\\]^_`{|}~'
    cho = []
    for a in alph:
        cho.append(a)
    for al in alph_low:
        cho.append(al)
    for na in non_alph:
        cho.append(na)
    for spaces in range(int(len(message)/np.random.choice([n for n in range(1,11)]))):
        cho.append(' ')

    for l in message:
        for k in range(0, key):
            encoded_message = encoded_message + np.random.choice(cho, 1)[0]
        encoded_message = encoded_message + l 
    for k in range(0, key):
        encoded_message = encoded_message + np.random.choice(cho, 1)[0]
    """
    #spaces amount check
    space_count = 0
    for l in encoded_message:
        if l.isspace():
            space_count+=1
    print(space_count)
    """
    
    return encoded_message

print(enc(key, message))


def decoder(encoded_message, key):
    return print(encoded_message[key::key+1])

decoder(enc(key, message), key)

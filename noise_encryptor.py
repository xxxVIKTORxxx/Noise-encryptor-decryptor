import numpy as np

message = 'CorRect mesSAge'

key = 1024


def enc(key, message):
    encoded_message = ''

    alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alph_low = alph.lower()
    non_alph = r'0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    cho = []
    for a in alph:
        cho.append(a)
    for al in alph_low:
        cho.append(al)
    for na in non_alph:
        cho.append(na)

    for l in message:
        for k in range(0, key):
            encoded_message = encoded_message + np.random.choice(cho, 1)[0]
        encoded_message = encoded_message + l
    def space_enc_index(key):
        if key < len(cho) and key >= 0:
            return key
        elif key > len(cho):
            return key // len(cho)
        elif key < 0:
            key * -1
            if key < len(cho):
                return key
            elif key > len(cho):
                return key // len(cho)
    encoded_message = encoded_message.replace(' ', cho[space_enc_index(key)])
    return encoded_message

print(enc(key, message))


def decoder(encoded_message, key):
    return print(encoded_message[key::key+1])

decoder(enc(key, message), key)
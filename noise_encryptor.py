import numpy as np

message = 'Just for fun tra la la bam bam!'

key = 256


def enc(key, message, spaces_count, spaces_method):
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
    if spaces_method == 'spaces_noise':
        for spaces in range(int(len(message)/np.random.choice([n for n in range(1,11)]))):
            cho.append(' ')
        

    #two methods of dealing with spaces:
    # 1: 'spaces_noise' adds random spaces and allows to return decoded message with spaces
    # 2: 'spaces_encode' encodes spaces by random sign for make encoded message spaceless, but decoder do not decodes spaces, it returns a random letter or symbol instead of spaces
    for l in message:
        for k in range(0, key):
            encoded_message = encoded_message + np.random.choice(cho, 1)[0]
        encoded_message = encoded_message + l 
    for k in range(0, key):
        encoded_message = encoded_message + np.random.choice(cho, 1)[0]
    if spaces_method == 'spaces_encode':
        encoded_message = encoded_message.replace(' ', np.random.choice(cho))
    
    #spaces count (optional)
    if spaces_count == True:
        space_count = 0
        for l in encoded_message:
            if l.isspace():
                space_count+=1
        print(space_count)
    else: 
        pass

    return encoded_message

print(enc(key, message, spaces_count = False, spaces_method = 'spaces_noise'))


def decoder(encoded_message, key):
    encmsg = str(encoded_message)
    return print(encmsg[key::key+1])

#decoding check
decoder(enc(key, message, spaces_count = True, spaces_method = 'spaces_encode'), key)

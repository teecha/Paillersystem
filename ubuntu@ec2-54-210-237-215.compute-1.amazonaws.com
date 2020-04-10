from textwrap import wrap
with open('h.txt') as f:
    priv = [int(x) for x in f]
    #print(priv[0])
    priv = priv[0]
with open('pub.txt') as f:
    pub = [int(x) for x in f]
    #print("public key")
    #print(type(pub[0]))
    pub = pub[0]
    #print(pub[1])
with open('pub1.txt') as f:
    pub1 = [int(x) for x in f]
    #print("public1 key")
    #print(pub1)
    pub1 = pub1[0]
with open('cipher.txt') as f:
    cipher = [int(x) for x in f]
    #print("cipher")
    #print(cipher[0])
    cipher = cipher[0]
with open('priv1.txt') as f:
    priv1 = [int(x) for x in f]
    #print("priv1")
    #print(priv1[0])
    priv1 = priv1[0]
def decrypt(priv, priv1, pub, pub1, cipher):
    x = pow(cipher, priv, pub1) - 1
    plain = ((x // pub) * priv1) % pub
    return plain
with open('tot.txt') as f:
    tot = [int(x) for x in f]
    tot = tot[0]
l = decrypt(priv, priv1, pub, pub1, cipher)
final = str(l - tot)
rever = wrap(final,3)
intlist = list(map(lambda x: int(x),rever))
test = list(map(lambda x: chr(x),intlist))
print(''.join(test))



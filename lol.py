"""
Created on Fri Mar 22 08:09:24 2019
@author: tejassk
"""

"""importing all the required libraries"""
import time
import math
import primes
import subprocess

"""declaring all the varialbes used in the code"""
keytime = []
brightval = []
dectime = []
public = []
private = []
privatetest = []
def invmod(a, p, maxiter=1000000):
    if a == 0:
        raise ValueError('0 has no inverse mod %d' % p)
    r = a
    d = 1
    for i in range(min(p, maxiter)):
        d = ((p // r + 1) * d) % p
        r = (d * a) % p
        if r == 1:
            break
    else:
        raise ValueError('%d has no inverse mod %d' % (a, p))
    return d

def modpow(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent & 1 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

def PrivateKey( p, q, n):
        l = (p-1) * (q-1)
        m = invmod(l, n)
        return l,m

def PublicKey(n):
        n = n
        q = n * n
        g = n + 1
        return n,q,g


def generate_keypair(bits):
    p = primes.generate_prime(bits)
    q = primes.generate_prime(bits)
    n = p * q
    return PrivateKey(p, q, n), PublicKey(n)

def encrypt(pub, plain):
    while True:
        r = primes.generate_prime(round(math.log(pub[0], 2)))
        if r > 0 and r < pub[0]:
            break
    x = pow(r, pub[0], pub[1])
    cipher = (pow(pub[2], plain, pub[1]) * x) % pub[1]
    return cipher

def e_add(pub, a, b):
    """Add one encrypted integer to another"""
    return a * b % pub[1]

def e_add_const(pub, a, n):
    """Add constant n to an encrypted integer"""
    return a * modpow(pub[2], n, pub[1]) % pub[1]

def e_mul_const(pub, a, n):
    """Multiplies an ancrypted integer by a constant"""
    return modpow(a, n, pub[1])

def decrypt(priv, pub, cipher):
    x = pow(cipher, priv[0], pub[1]) - 1
    plain = ((x // pub[0]) * priv[1]) % pub[0]
    return plain

with open('sensitive.txt') as f:
    a1 = [int(x) for x in f]
    print(a1[0])
    a = a1[0]

a = c = a1[0]
tot=0
while(c>0):
    dig=c%10
    tot=tot+dig
    c=c//10
#print("The total sum of digits is:",tot)

b = tot #counting the sum of digits
i = 0 #initializing a count variable i to 0
priv,pub = generate_keypair(192)


"""The real encryption happens here"""
encrypt_sttime = time.time()
x = encrypt(pub, a) #encryption of a with the public key
y = encrypt(pub, b) #encryption of b with the public key
z = e_add(pub, x, y) #addition of the both the encryptions
encrypt_endtime = time.time()
print("Time taken for encryption is ", encrypt_endtime-encrypt_sttime)
b = decrypt(priv, pub, z)
#print(b-tot)

'''writing total into a file'''
f = open("tot.txt","w")
a = tot
#print(a)
f.write('{}'.format(tot))
f.close

'''writing cipher text into a file'''
f = open("cipher.txt","w")
a = z
#print(a)
f.write('{}'.format(z))
f.close

'''writing first half of private key into a file'''
f = open("h.txt","w")
a = int(priv[0])
#print(a)
f.write('{}'.format(a))
f.close

'''writing the second private key part into a file'''
f = open("priv1.txt","w")
#print(priv[1])
f.write('{}'.format(priv[1]))
f.close

'''writing the public key into a file'''
f = open("pub.txt","w")
a = int(pub[0])
#print(a)
f.write('{}'.format(a))
f.close

'''writing the publickey second part into a file'''
f = open("pub1.txt","w")
a = int(pub[1])
#print(a)
f.write('{}'.format(a))
f.close

f = open("test.txt","w")
f.close

subprocess.call("./copy.sh", shell = "TRUE")


"""amazon account ---
    usrname ---
    pwd ---
"""

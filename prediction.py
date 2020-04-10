#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 00:10:03 2019

@author: tejassk
"""

a=raw_input()
b=raw_input()
c=raw_input()
d=raw_input('Enter your credit score')
e=raw_input('enter your gender 1->male 0->female')
f=raw_input('enter youe age')
g=raw_input('enter tour tenure with this company')
h=raw_input('enter your current bank balance')
i=raw_input('enter no of products purchased')
j=raw_input('do you have a credit card 1->yes 0-> no')
k=raw_input('do you think you are an active member 1->yes 0-> no')
l=raw_input('what is your estimated salary per month')
from keras.models import load_model
import numpy as np
model = load_model('test.h5');
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
y_p=model.predict(np.array([[a,b,c,d,e,f,g,h,i,j,k,l]]))
print(y_p > 0.3)
if y_p >=0.3:
    f=open("sensitive.txt",'a')
    f.write(a)
    f.write(b)
    f.write(c)
    f.write(d)
    f.write(e)
    f.write(f)
    f.write(g)
    f.write(i)
    f.write(j)
    f.write(k)
    f.write(l)
    f.close()
else:
    z=open("notsenstivie.txt",'a')
    z.write(a)
    z.write(b)
    z.write(c)
    z.write(d)
    z.write(e)
    z.write(f)
    z.write(g)
    z.write(i)
    z.write(j)
    z.write(k)
    z.write(l)
    z.close()

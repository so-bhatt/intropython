# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 18:01:55 2018

@author: Soumyadeep B
"""
import numpy
def guess_my_no_upto(n_1):
    n=n_1/2
    mini=0
    maxi=n_1
    while True:
        print('Please think of a number between 0 and n_1!')
        print('Is your secret number'+str(n)+'?')
        indication=input('Enter h for "Too high". Enter l for "Too Low". Enter c for "COORRECT"\n')
        if indication=='l':
            mini=n
            n=numpy.ceil((maxi+n)/2)
        elif indication=='h':
            maxi=n
            n=numpy.ceil((mini+n)/2)
        elif indication=='c':
            print('Game over. Your secret number was:'+ str(n))
            break
        else:
            print('Sorry, I did not understand your input.')
    
    #        break
        

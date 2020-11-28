# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 21:06:11 2018

@author: Soumyadeep B
"""


# run, then write game()
# betting game

import random
def game():
    user=100
    comp=100
    lifelines=3
    promotions_300=1
    wins=0
    loses=0
    while (comp>=0 and user>0) or (comp>=0 and lifelines>0):
        bet=int(input('how much do you bet '))
        if bet>user:
            bet=int(input('you can not bet more than what you have. How much do you bet '))
        n=random.randrange(0,2)
        if n==1:
            user+=bet
            comp-=bet
            wins+=1
            print('wow you got '+str(bet)+' stars '+"you have "+str(user)+' stars')
        else :
            user-=bet
            comp+=bet
            loses+=1
            print('ughh you lost '+str(bet)+' stars'+" you have "+str(user)+' stars')
#    if user==0:
#        return('you lost')
        if user<=0 and lifelines>0:
            lifeline_Q=input('do you want to use a lifeline ')
            if lifeline_Q=='yes':
                user+=100
                lifelines-=1
            else:
                return('you lost')
                
        if promotions_300==1 and user>=300:
            user+=300
            promotions_300=0
            print('you just got a promotion to '+str(user))
        if wins==15 :
            user+=300
    if comp<=0:
        return('you won')
    else:
        return('you lost')
        
        
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 20:28:16 2018

@author: Soumyadeep B
"""#ord(string[g])+13>122
#
#string='Hello, World!'
#for g in range (0,len(string)):
#    if (65<=ord(string[g])<=90 or 97<=ord(string[g])<=122 ):
#        if(65<=(ord(string[g])+13)<=90 or 97<=(ord(string[g])+13)<=122):
#            
#            print(chr(ord(string[g])+13))
#        else:
#             print(chr(ord(string[g])-13))   
#    else :
#        print(string[g])
        
#        
#        
def rot13(string):
 n_str=''
 for g in range (0,len(string)):
  if (65<=ord(string[g])<=90 or 97<=ord(string[g])<=122 ):
    if (65<=ord(string[g])<=90):
        if(65<=(ord(string[g])+13)<=90):        
#            print(string[g]+'->' +chr(ord(string[g])+13))
            n_str+=(chr(ord(string[g])+13))
        else:
#             print(string[g]+'->'+chr(ord(string[g])-13))
             n_str+=(chr(ord(string[g])-13))
    if (97<=ord(string[g])<=122):
        if(97<=(ord(string[g])+13)<=122):        
#            print(string[g]+'->' +chr(ord(string[g])+13))
            n_str+=(chr(ord(string[g])+13))
        else:
#             print(string[g]+'->' +chr(ord(string[g])-13))
             n_str+=(chr(ord(string[g])-13))
  else :
#        print(string[g])
      n_str+=string[g]
 return n_str       
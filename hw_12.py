# -*- coding: utf-8 -*-
"""
Created on Thu May 24 08:43:06 2018

@author: Soumyadeep B
"""

import numpy

#this is the array that will act as the connect 4 gridfor the game
arr=numpy.zeros([6,7])
#who=input("for which letter are you playing??? playing for x means 1 playing for 0 means 2. My value is ")



who=1
#A funtion is defined for display purpose
def Print_Grid(arr):
   connect4grid="0 1 2 3 4 5 6\n"
   for l in range(0,numpy.size(arr,0)):
     for k in range(0,numpy.size(arr,1)):
        if(arr[l,k]==0):
            connect4grid+='. '
        if(arr[l,k]==1):
            connect4grid+='x '
        if(arr[l,k]==2):
            connect4grid+='o '  
     connect4grid+='\n' 
   print(connect4grid)

#A funtion is defined to determine who won
def who_won(arr,who):
    #for row in range (1, numpy.size(arr,0)):
    x=numpy.where(arr==1)
    row=x[0]
    col=x[1]
    
    if len(col)>=4 :          #to see if any user won by putting coins straight in a column
        z=numpy.unique(col)
        for ind in range(0,len(z)):
            
            col_ind=numpy.where(col==z[ind])[0]
            if len(col_ind)>=4:
                row_ind=row[col_ind]
    #            for ind_1 in range (0,3):
                if row_ind[0]+3==row_ind[1]+2==row_ind[2]+1==row_ind[3]:
                    print(str(who)+' won')               
                    return(1)
                    
    if len(row)>=4 :            #to see if any user won by putting coins straight in a row
        z=numpy.unique(row)
        for ind in range(0,len(z)):
            
            row_ind=numpy.where(row==z[ind])[0]
            if len(row_ind)>=4:
                col_ind=col[row_ind]
    #            for ind_1 in range (0,3):
                if col_ind[0]+3==col_ind[1]+2==col_ind[2]+1==col_ind[3]:
                    print(str(who)+' won')                
                    return(1)
             
    if len(row)>=4 :          #to see if any user won by putting coins strainght in a diagonal
        r=numpy.unique(row)
#        c=numpy.unique(col)
        for ind in range(0,len(r)):
            row_ind=numpy.where(row==r[ind])[0]
            if len(row_ind)>=4:
                col_ind=col[row_ind]
                if col_ind[0]+3==col_ind[1]+2==col_ind[2]+1==col_ind[3] and row_ind[0]+3==row_ind[1]+2==row_ind[2]+1==row_ind[3]:
                    print(str(who)+' won')
                    return(1)
    return(0)                        


#for gaming/accumulating purpose
while len(numpy.where(arr==0))>0:        
    who=int(input('for which number are you playing??? Enter only 1 or 2. Choose one for the entire Game'))
    c=int(input("what column do want to put your coin in??"))
    while 6<c or c<0:
        print("wrong input! entear a value between 0 to 6")
        c=int(input("what column do want to put your coin in???"))
    ind=0   
    while ind==0:
        if arr[5,c]==0:
            ind=1
            arr[5,c]=who
        elif arr[4,c]==0:
            ind=1
            arr[4,c]=who    
        elif arr[3,c]==0:
            ind=1
            arr[3,c]=who  
        elif arr[2,c]==0:
            ind=1
            arr[2,c]=who 
        elif arr[1,c]==0:
            ind=1
            arr[1,c]=who  
        else :
            c=int(input("comlumn overflow!!!Choose another column."))
    Print_Grid(arr)
    if who_won(arr,who)==1:
        break
    

        
    
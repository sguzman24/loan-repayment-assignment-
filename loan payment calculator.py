# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 17:43:17 2023

@author: sguzman24
"""
"""
 pmt = r * PV/(1-(1+)**-n)
 pmt is how you pay back/mo
 n is number of months
 r is interest rate per month
 n is number of month
 """
def notsure(PV, r, n):
     """
     Parameters
     ----------
     PV : present value (amt borrow)
     r : intrest rate apr
     n : number of months to pay back

     Returns
     -------
     pmt : amount paid per month
     """
     pmt = r * PV/(1-(1+r)**-n)
     return pmt
 
 # input the pv
 
import numpy as np
    
n = 48
pv = input('enter pv: ')
pv = float(pv)

# equivalently pv = float(input('enter pv: '))
print(f"pv = {pv}")
r = input('interest APR: ')
r = float(r)/100
r = r/12

print(f"interest = {r} ")
pmt = notsure(pv, r, n)
pmt = np.round(pmt, 2)

print(f"payment is {pmt} per month")



    
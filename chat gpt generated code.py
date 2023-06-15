# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 18:35:29 2023

@author: sguzman24
"""

def calculate_monthly_repayment(PV, r, n):
    """
    Calculates the monthly repayment amount for a loan.

    Args:
        PV (float): Present Value (loan amount).
        r (float): Annual Percentage Rate (APR).
        n (int): Number of months.

    Returns:
        float: Monthly repayment amount.
    """
    # Convert APR to monthly interest rate
    r = r / 100 / 12

    # Calculate the monthly repayment amount
    Pmt = r * PV / (1 - (1 + r) ** -n)

    return Pmt

# Test the function with the given values
PV = 12000
r = 7.45
n = 48

monthly_repayment = calculate_monthly_repayment(PV, r, n)
print("Monthly Repayment Amount: $", round(monthly_repayment, 2))

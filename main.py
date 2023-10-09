# File: main.py
# Author: Luke Sapp
# Date: October 8th 2023
# Description: This script performs both ecludian GCD, and middle-school gcd
# License: MIT License


def con_ecludian(m,n):
  '''
  Function: To implement the Euclidean algorithm for finding the gcd

  Arguments: int m,n

  Returns: int t
  '''

  """"
  Step 1 Assign the value of min{m, n} to t."
  Step 2 Divide m by t. If the remainder of this division is 0, go to Step 3; 
  otherwise, go to Step 4.
  Step 3 Divide n by t. If the remainder of this division is 0, return the value of
  t as the answer and stop; otherwise, proceed to Step 4.
  Step 4 Decrease the value of t by 1. Go to Step 2
   - From Textbook, [Levition, 5]
    """
  solved=0
  t = min(m,n)
  while solved!=0:
    if(m%t==0 and n%t==0):
        solved=1
        return t
    else:
      t=t-1


def middle_school(m,n):
  '''
  Function:implement the middle school algo for finding gcd, according to specs below

  Arguments: int m,n

  Returns: int y
  '''
  
  """
  Middle-school procedure for computing gcd(m, n):
  Step 1 Find the prime factors of m.
  Step 2 Find the prime factors of n.
  Step 3 Identify all the common factors in the two prime expansions found in
  Step 1 and Step 2. (If p is a common factor occurring pm and pn times
  in m and n, respectively, it should be repeated min{pm, pn} times.)
  Step 4 Compute the product of all the common factors and return it as the
  greatest common divisor of the numbers given
  - from the textbook, [Leviton,33]
  """
  
  common_prime = []
  prime_m = []
  prime_n = []
  div = 2

# Prime nums for m
  while m>1:
    if m%div==0:
      prime_m.append(div)
      m=m/div
    div+=1

  div = 2
  #Prime nums for n
  while n>1:
    if n%div==0:
      prime_n.append(div)
      n=n/div
    div+=1

# Compute the product of all common prime nums
  for i in prime_m:
    if prime_m[i]==prime_n[i]:
      common_prime.append(prime_m[i])
      
  y = 1 
  for i in common_prime:
    x = common_prime[i]
    y = y*x

  return y


def main():
  '''
  Function: Serves as a driver, and displays the menu. 

  Arguments: int a,b to con_ecludian and int a,b to middle_school

  Returns: t from con_ecludian and y from middle_school
  '''
  
  a=input('What would you use for your first number in the extended ecludian ? ')
  b=input('What would you use for your second number in the extended ecludian ? ')
  
  gcd=con_ecludian(a,b)
  print(f"GCD({a}, {b}) = {gcd}" )

  a2=input('What would you use for your first number in the Middle School algo? ')
  b2=input('What would you use for your second number in the Middle School algo? ')
  gcd2=middle_school(a2,b2)
  print(f"GCD{a2},{b2}) = {gcd2}")

if __name__=="__main__":
  main()
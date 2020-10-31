def gcd (a,b):
    '''returns the greatest common divisor of two nonnegative integers'''
    if a == 0: #base case
        return b
    
    elif b == 0:
        return a

    else: #recursion
        divisor = 1 #number to divide into both numbers
        divisorList = [] #store the divisors
        
        while divisor < min (a,b): #while the divisor is less than the smollest number
            if a%divisor == 0 and b%divisor == 0: #if they divide evenly
                divisorList.append (divisor)
            divisor +=1
    return max (divisorList)

print (gcd (20,45))
            
        
        
        

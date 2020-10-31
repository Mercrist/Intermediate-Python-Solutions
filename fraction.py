class Fraction:
    '''represents fractions'''
    def __init__(self,num,denom): 
        '''Fraction(num,denom) -> Fraction
        creates the fraction object representing num/denom'''
        if denom == 0: # raise an error if the denominator is zero
            raise ZeroDivisionError
        else: #else, assign and create the variables
            self.num = num
            self.denom = denom 

    def __str__ (self):
        from math import gcd #gcd to know how to simplify fraction
        divisor = gcd (self.num, self.denom)
        self.denom = self.denom//divisor #divide top and bottom of fraction by the greatest common divisors
        self.num = self.num//divisor
            
        if self.denom < 0: #this is to get the numerator to always be negative
                self.denom = abs (self.denom)
                self.num = -self.num
        return str (self.num) + "/" + str(self.denom)

    def __float__ (self): #return decimal
        return self.num/self.denom
    
    def add (self,other):
        self.num = (self.num*other.denom)+(other.num*self.denom) 
        self.denom = (self.denom*other.denom)
        return str (self) #so that the str function simplifies it

    def sub (self, other):
        self.num = (self.num*other.denom)-(other.num*self.denom)
        self.denom = (self.denom*other.denom)
        return str (self)

    def mul (self, other):
        self.num = self.num*other.num
        self.denom = self.denom*other.denom
        return str (self)

    def div (self,other):
        (other.num, other.denom) = (other.denom, other.num) #revers the values and then multiply
        return str (self.mul (other))

    def eq (self, other):
        if str(self) == str (other): #if they have the same simplified values:
            return True
        return False #else returns false
        
# examples
p = Fraction(3,6)
print(p)  # should print 1/2
q = Fraction(10,-60)
print(q)  # should print -1/6
r = Fraction(-24,-48)
print(r)  # should also print 1/2
x = float(p)
print(x)  # should print 0.5
### if implementing "normal" arithmetic methods
print(p.add(q))       # should print 1/3, since 1/2 + (-1/6) = 1/3
p = Fraction(3,6) #reset since the functions modify self
print(p.sub(q))  # should print 2/3, since 1/2 - (-1/6) = 2/3
p = Fraction(3,6)
print(p.sub(p))  # should print 0/1, since p-p is 0
p = Fraction(3,6)
print(p.mul(q)) # should print -1/12
p = Fraction(3,6)
print(p.div(q))  # should print -3/1
p = Fraction(3,6)
q = Fraction(10,-60)
print(p.eq(r))   # should print True
print(p.eq(q))   # should print False





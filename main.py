class Currency:
    #dictionary of all accepted currencies
    currencies = {'CHF': 0.930023, #swiss franc 
        'CAD': 1.264553, #canadian dollar
        'GBP': 0.737414, #british pound
        'JPY': 111.019919, #japanese yen
        'EUR': 0.862361, #euro
        'USD': 1.0 #us dollar
    }
    def __init__(self, value, unit="USD"):
        self.value = value
        self.unit = unit
    #Purpose: changes USD currencies and updates the value appropriately 
    def changeTo (self, new_unit):
        self.value = (self.value/  Currency.currencies[self.unit]* Currency.currencies[new_unit])
        self.unit = new_unit
    #Purpose: by rewriting a magic method, make repr return the string to be printed rounded to 2 digits
    def __repr__(self):
        return f"{round(self.value,2)} {self.unit}"
    #Purpose: rewrite method to return the same as __repr__
    def __str__(self):
        return f"{round(self.value,2)} {self.unit}"
    #Purpose: defines the + operator to add values
    #Params: Options for other:
    #           Currency Object: converts unit to self then adds other.value
    #           Float or Int:    assumes its in USD, converts if needed, and adds 
    def __add__(self, other):
        if isinstance(other, Currency):
            # check if the currencies are the same 
            if self.unit == other.unit:
                sum =  self.value + other.value
            else:
                other_value_converted = (other.value/  Currency.currencies[other.unit]* Currency.currencies[self.unit])  
                sum =  self.value + other_value_converted
        elif isinstance(other, int) or isinstance(other, float):
            if self.unit == 'USD':
                sum =  self.value + other
            else:
                sum =  self.value + (other/ Currency.currencies["USD"] * Currency.currencies[self.unit])     
        else:
            raise ValueError("Other must be of type Currency or an integer or float")
        return Currency(sum, self.unit)
    # Purpose: same as calling add
    def __iadd__(self,other):
        return Currency.__add__(self, other)
    #Purpose: deals with when a int/float has a Currency object added to it
    #Note: will always assume the INT/FLOAT is USD and returns USD
    def __radd__(self, other):
        if (self.unit == 'USD'):
            sum = other + self.value
        else:
            sum = other + (self.value/  Currency.currencies[self.unit]* Currency.currencies['USD']) 
        return Currency(sum, 'USD')
    #Purpose: defines the - operator to subtract values
    #Params: Options for other:
    #           Currency Object: converts unit to self then subs other.value
    #           Float or Int:    assumes its in USD, converts if needed, and subs 
    def __sub__(self,other):
        if isinstance(other, Currency):
            # check if the currencies are the same 
            if self.unit == other.unit:
                subbed_val =  self.value - other.value
            else:
                other_value_converted = (other.value/  Currency.currencies[other.unit]* Currency.currencies[self.unit])  
                subbed_val =  self.value - other_value_converted
        elif isinstance(other, int) or isinstance(other, float):
            if self.unit == 'USD':
                subbed_val =  self.value - other
            else:
                subbed_val =  self.value - (other/ Currency.currencies["USD"] * Currency.currencies[self.unit])     
        else:
            raise ValueError("Other must be of type Currency or an integer or float")
        return Currency(subbed_val, self.unit)
    #Purpose: as far as I can tell tis the same as sub
    def __isub__(self, other):
        return (Currency.__sub__(self,other))
    #Purpose: deals with when a int/float has a Currency object subtracted from it
    #Note: will always assume the INT/FLOAT is USD and returns USD
    def __rsub__(self, other):
        if (self.unit == 'USD'):
            subbed_val = other - self.value
        else:
            subbed_val = other - (self.value/  Currency.currencies[self.unit]* Currency.currencies['USD']) 
        return Currency(subbed_val, 'USD')
    








v1 = Currency(23.43, "EUR")
v2 = Currency(19.97, "USD")
#Test1: Adding 2 Currency Objects
print(v1 + v2)
print(v2 + v1)
#Test2: adding ints or floats
print(v1 + 3) # an int or a float is considered to be a USD value
print(3 + v1)
#Test 3: subtracting 
print(v1 - 3) # an int or a float is considered to be a USD value
print(30 - v2) 
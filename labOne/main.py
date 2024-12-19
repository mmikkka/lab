class Math:
    pi = 3.141592653589793  
    @staticmethod  
    def cosine(x, terms=100): 
        if type(x) != int:
            raise TypeError
        
        if x < 0:
            x = -x

        if x == 0:
            return 1

        x = x * (Math.pi / 180)
    
        cosine_value = float(1)
        factorial = float(1)
        power = float(1)

        for n in range(1, terms):
            power *= -x * x  
            factorial *= (2 * n - 1) * (2 * n) 
            cosine_value += power / factorial

        return float("{0:.1f}".format(cosine_value))
    
    def sine(x, terms=100):
        if type(x) != int:
            raise TypeError

        is_negative = False
        if x < 0:
            is_negative = True
            x = -x

        if x == 0:
            return 0

        x = x * (Math.pi / 180)
        
        sine_value = float(0)
        factorial = float(1)
        power = float(x)

        for n in range(0, terms):
            if n > 0:
                power *= -x * x
                factorial *= (2 * n) * (2 * n + 1)
            sine_value += power / factorial

        if is_negative: 
            sine_value = -sine_value

        return float("{0:.1f}".format(sine_value))
    
    def natural_log(x, terms=100):
        if x <= 0:
            raise Exception("Число должно быть больше 0.")
        
        if type(x) != int and type(x) != float:
            raise TypeError

        if x == 1:
            return 0
        
        ln_value = float(0)
        y = (x - 1) / (x + 1)    

        for n in range(1, terms + 1):
            ln_value += (1 / (2 * n - 1)) * (y ** (2 * n - 1))

        ln_value *= 2  

        return float("{0:.1f}".format(ln_value))

    def modul(x):
        if type(x) != int and type(x) != float:
            raise TypeError
        
        if x < 0:
            return -x
        else:
            return x
      
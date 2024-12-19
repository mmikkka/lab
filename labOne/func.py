from main import Math

def Func(x: float) -> float:
    if x >= 0:
        return Math.natural_log(x) * Math.cosine(x)
    elif x < 0:
        return (Math.modul(Math.sine(x) - Math.cosine(x)))/(Math.natural_log(Math.modul(x)) + 1)
    
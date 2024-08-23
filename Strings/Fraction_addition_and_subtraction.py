from fractions import Fraction
import re

expression1 = "-1/2+1/2"
fr = re.findall(r'[+-]?\d+/\d+',expression1)
print(fr)
res = sum(Fraction(frac) for frac in fr)
print(res)

for f in fr:
    print(Fraction(f))
print(type(res)," ",res.numerator," ",res.denominator)
print(f"{res.numerator}/{res.denominator}")


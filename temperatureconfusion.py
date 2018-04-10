from fractions import Fraction
from sys import stdin
n, d = [int(x) for x in stdin.readline().split("/")]
ans = (Fraction(n, d) - 32) * Fraction(5, 9)
print("{}/{}".format(ans.numerator, ans.denominator))
import hashlib
from sympy import *

# Karmaşık sayılar için modüler işlem (mod p)
def complex_mod(a, p):
    return complex(a.real % p, a.imag % p)

# Karmaşık sayılar için modüler üs alma işlemi (a^b mod p)
def complex_pow_mod(a, b, p):
    result = 1 + 0j
    base = a
    exp = int(b.real)  # Karmaşık sayıyı tam sayıya dönüştürme
    while exp:
        if exp % 2:
            result = complex_mod(result * base, p)
        base = complex_mod(base * base, p)
        exp //= 2
    return result

# Karmaşık sayılar için modüler ters işlemi (mod p)
def complex_mod_inverse(a, p):
    t = 0
    newt = 1
    r = p
    newr = a.real + a.imag * I
    while newr != 0:
        quotient = r // newr
        t, newt = newt, t - quotient * newt
        r, newr = newr, r - quotient * newr
    if r > 1:
        raise ValueError(f"Modüler ters bulunamadı: {a}, modül: {p}")
    if t < 0:
        t = t + p
    return complex(t % p, 0)

g = 3 + 2j
a = 1 + 2j
p = 17

# Anahtar üretimi
A = complex_pow_mod(g, a, p)

# İmza oluşturma
m = "Hello, world!"
k = 1 + 4j
r = complex_pow_mod(g, k, p)
h = int(hashlib.sha256(m.encode('utf-8')).hexdigest(), 16)
s = (h - a * r) * complex_mod_inverse(k, p)
s = complex_mod(s, p)

# İmza doğrulama
u1 = h * complex_mod_inverse(s, p) % p
u2 = r * complex_mod_inverse(s, p) % p
v = (complex_pow_mod(g, u1, p) * complex_pow_mod(A, u2, p)) % p

if v == r.real:
    print("İmza doğrulandı.")
else:
    print("İmza doğrulanamadı.")


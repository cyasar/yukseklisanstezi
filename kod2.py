import hashlib
import cmath
import math
import numpy as np


# Karmaşık sayılar için modüler işlem tanımlama
def complex_mod(a, m):
    real_mod = a.real % m.real
    imag_mod = a.imag % m.real
    return complex(real_mod, imag_mod)

# Karmaşık sayılar için modüler ters işlem tanımlama
def complex_mod_inverse(a, m):
    a_real = int(a.real)
    a_imag = int(a.imag)
    m_real = int(m.real)
    
    real_inv = np.power(a_real, -1, dtype=complex)
    imag_inv = np.power(a_imag, -1, dtype=complex)
    return complex(real_inv, imag_inv)

# Anahtar üretimi
g = complex(2, 3)
p = complex(97, 0) # Örnek karmaşık sayı modülü
a = complex(5, 4) # Alice'in özel anahtarı

A = complex_mod(g**a, p) # Alice'in genel anahtarı
print(f"Alice'in genel anahtarı (A): {A}")

# İmza oluşturma
m = "Merhaba, bu bir örnek mesajdır."
k = complex(3, 2)

r = complex_mod(g**k, p)
h = int(hashlib.sha256(m.encode('utf-8')).hexdigest(), 16)

s = complex_mod((h - a * r) * complex_mod_inverse(k, p), p)

signature = (r, s)
print(f"İmza: {signature}")

# İmza doğrulama
h2 = int(hashlib.sha256(m.encode('utf-8')).hexdigest(), 16)

u1 = complex_mod(h2 * complex_mod_inverse(s, p), p)
u2 = complex_mod(r * complex_mod_inverse(s, p), p)

v = complex_mod(g**u1 * A**u2, p)
print(f"Doğrulama değeri (v): {v}")

if v == r:
    print("İmza geçerli.")
else:
    print("İmza geçersiz.")
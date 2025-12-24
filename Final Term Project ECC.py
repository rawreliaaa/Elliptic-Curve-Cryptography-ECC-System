import random
from typing import Optional, Tuple

Point = Optional[Tuple[int, int]]

class EllipticCurve:
    def __init__(self, a: int, b: int, p: int, G: Tuple[int, int]):
        self.a = a
        self.b = b
        self.p = p
        self.G = G
        discriminant = (4 * pow(a, 3, p) + 27 * pow(b, 2, p)) % p
        if discriminant == 0:
            raise ValueError("Singular curve: invalid parameters")
        if not self.is_on_curve(G):
            raise ValueError("Generator G not on curve")

    def is_on_curve(self, P: Point) -> bool:
        if P is None:
            return True
        x, y = P
        return (y*y - (x*x*x + self.a*x + self.b)) % self.p == 0

    def _mod_inv(self, x: int) -> int:
        return pow(x, -1, self.p)

    def point_add(self, P: Point, Q: Point) -> Point:
        if P is None: return Q
        if Q is None: return P
        x1, y1 = P
        x2, y2 = Q
        if x1 == x2 and (y1 + y2) % self.p == 0:
            return None
        if P == Q:
            m = ((3*x1*x1 + self.a) * self._mod_inv(2*y1 % self.p)) % self.p
        else:
            m = ((y2 - y1) * self._mod_inv((x2 - x1) % self.p)) % self.p
        x3 = (m*m - x1 - x2) % self.p
        y3 = (m*(x1 - x3) - y1) % self.p
        return (x3, y3)

    def scalar_mult(self, k: int, P: Point) -> Point:
        if k % self.p == 0 or P is None:
            return None
        result = None
        addend = P
        while k > 0:
            if k & 1:
                result = self.point_add(result, addend)
            addend = self.point_add(addend, addend)
            k >>= 1
        return result

def generate_keypair(curve: EllipticCurve) -> Tuple[int, Point]:
    priv = random.randint(1, curve.p - 1)
    pub = curve.scalar_mult(priv, curve.G)
    return priv, pub

def encrypt(curve: EllipticCurve, pub: Point, M: Point) -> Tuple[Point, Point]:
    k = random.randint(1, curve.p - 1)
    C1 = curve.scalar_mult(k, curve.G)
    k_pub = curve.scalar_mult(k, pub)
    C2 = curve.point_add(M, k_pub)
    return C1, C2

def decrypt(curve: EllipticCurve, priv: int, C1: Point, C2: Point) -> Point:
    S = curve.scalar_mult(priv, C1)
    if S is None: 
        raise ValueError("Shared secret is point at infinity; decryption failed.")
    S_inv = (S[0], (-S[1]) % curve.p)
    return curve.point_add(C2, S_inv)

if __name__ == "__main__":
    p, a, b, G = 97, 2, 3, (3, 6)
    curve = EllipticCurve(a, b, p, G)
    priv, pub = generate_keypair(curve)
    M = curve.scalar_mult(7, curve.G)
    C1, C2 = encrypt(curve, pub, M)
    M_dec = decrypt(curve, priv, C1, C2)
    print("Private key:", priv)
    print("Public key:", pub)
    print("Plaintext point:", M)
    print("Ciphertext:", (C1, C2))
    print("Decrypted point:", M_dec)
    print("Decryption correct:", M_dec == M)

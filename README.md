"""
# Elliptic Curve Cryptography (ECC) System

This file contains a simple, educational implementation of an **Elliptic Curve Cryptography (ECC)** system in Python.  
It demonstrates the technical principles of ECC, how to use the program, its architecture, the development process, and the references and enhancements that guided its creation.

## Functions, Technical Principles, and Usage

The program defines an elliptic curve over a finite prime field using the equation:

    y² = x³ + ax + b (mod p)

It implements the following functions:
- **Point operations**: addition, doubling, and scalar multiplication of points on the curve.
- **Key generation**: produces a private key (random integer) and a public key (scalar multiple of the generator point).
- **Encryption (ElGamal-style)**: generates ciphertext as a pair (C1, C2), where C1 = k·G and C2 = M + k·Pub.
- **Decryption**: recovers the plaintext point using M = C2 - d·C1.

All operations are performed modulo a prime p, and the security principle relies on the hardness of the **Elliptic Curve Discrete Logarithm Problem (ECDLP)**.

### How to Use
Clone or download this file, then run:

    python ecc_system.py

Example output:
    Private key: 42
    Public key: (x, y)
    Plaintext point: (x, y)
    Ciphertext: ((x1, y1), (x2, y2))
    Decrypted point: (x, y)
    Decryption correct: True

---

## Architecture, Development Process, and References

### Architecture
The program is structured as follows:
- **EllipticCurve class**: encapsulates curve parameters and point operations.
- **Key management functions**: generate private/public key pairs.
- **Crypto functions**: perform encryption and decryption.
- **Demo script**: shows example usage with toy parameters.

### Development Process
1. **Research**: Reviewed ECC fundamentals such as modular arithmetic, group law, and curve equations.
2. **Implementation**: Built modular inverse, point addition, scalar multiplication, and ElGamal-style encryption/decryption.
3. **Testing**: Verified that generated keys lie on the curve and confirmed encryption/decryption correctness.
4. **Documentation**: Embedded README into this file.

### References and Enhancements
- **Sources**:
  - *Handbook of Applied Cryptography* by Menezes, van Oorschot, and Vanstone.
  - Elliptic Curve Cryptography (Wikipedia).
  - Practical ECC Guide (cryptobook.nakov.com).
- **Enhancements made**:
  - Added sanity checks (curve discriminant, generator validity).
  - Modularized point operations for clarity.
  - Extended with encryption/decryption functions beyond scalar multiplication.
- **Future possible improvement**:
  - Implement ECDSA signatures.
  - Add message-to-point encoding.
  - Integrate with secure libraries for real-world curves.



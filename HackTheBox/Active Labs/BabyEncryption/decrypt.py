def modular_inverse(a, m):
    # Extended Euclidean Algorithm to find the modular inverse
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        # q is quotient
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def decryption(ct):
    # Find the modular inverse of 123 mod 256
    inv_123 = modular_inverse(123, 256)
    
    pt = []
    for c in ct:
        # Reverse the encryption formula
        original_char = (inv_123 * (c - 18)) % 256
        pt.append(original_char)
    
    return bytes(pt)

with open('./msg.enc', 'r') as f:
    hex_data = f.read().strip()

ct = bytes.fromhex(hex_data)

decrypted_msg = decryption(ct)

print("Decrypted Message:", decrypted_msg.decode('latin-1'))  
# Use 'latin-1' to handle byte values correctly

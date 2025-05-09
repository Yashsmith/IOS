def correct_hamming(received):
    # Convert string to list of integers
    bits = [int(bit) for bit in received]

    # We use 1-based positions: [p1, p2, d1, p3, d2, d3, d4]
    # Indexes (0-based):       [ 0,  1,  2,  3,  4,  5,  6]

    # Calculate syndrome bits (s1, s2, s3)
    s1 = bits[0] ^ bits[2] ^ bits[4] ^ bits[6]  # parity bit p1
    s2 = bits[1] ^ bits[2] ^ bits[5] ^ bits[6]  # parity bit p2
    s3 = bits[3] ^ bits[4] ^ bits[5] ^ bits[6]  # parity bit p3

    # Calculate error position in decimal
    error_pos = s3 * 4 + s2 * 2 + s1 * 1

    if error_pos == 0:
        print("✅ No error detected.")
    else:
        print(f"❌ Error at position {error_pos}")
        # Fix the error (flip the bit)
        bits[error_pos - 1] ^= 1
        print("✅ Error corrected.")

    # Print corrected code
    print("Corrected 7-bit Hamming code:", ''.join(str(bit) for bit in bits))
    print("Original 4-bit data:", bits[2], bits[4], bits[5], bits[6])


# --- Main Program ---
code = input("Enter 7-bit Hamming code (e.g. 0110011): ")

# Input check
while len(code) != 7 or not all(c in '01' for c in code):
    code = input("Please enter exactly 7 bits (0 and 1 only): ")

correct_hamming(code)
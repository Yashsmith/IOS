def encode(data):
    # data = 4 bits: d1 d2 d3 d4
    d1 = int(data[0])
    d2 = int(data[1])
    d3 = int(data[2])
    d4 = int(data[3])

    # parity bits
    p1 = d1 ^ d2 ^ d4
    p2 = d1 ^ d3 ^ d4
    p3 = d2 ^ d3 ^ d4

    # final 7-bit code: p1 p2 d1 p3 d2 d3 d4
    return [p1, p2, d1, p3, d2, d3, d4]

def detect_and_correct(code):
    # code = 7 bits: p1 p2 d1 p3 d2 d3 d4
    p1 = code[0]
    p2 = code[1]
    d1 = code[2]
    p3 = code[3]
    d2 = code[4]
    d3 = code[5]
    d4 = code[6]

    # syndrome bits
    s1 = p1 ^ d1 ^ d2 ^ d4
    s2 = p2 ^ d1 ^ d3 ^ d4
    s3 = p3 ^ d2 ^ d3 ^ d4

    error_pos = s3 * 4 + s2 * 2 + s1 * 1  # binary to decimal

    if error_pos == 0:
        print("✅ No error detected.")
    else:
        print(f"❌ Error at position {error_pos} (1-based). Correcting...")
        code[error_pos - 1] ^= 1  # flip the bit

    print("✅ Corrected code:", ''.join(str(bit) for bit in code))
    print("📥 Original data bits:", code[2], code[4], code[5], code[6])

# -----------------------------
# Main Program
# -----------------------------
data = input("Enter 4-bit binary data (e.g. 1011): ")
while len(data) != 4 or not all(c in '01' for c in data):
    data = input("❗ Please enter exactly 4 bits (only 0 and 1): ")

code = encode(data)
print("📤 Encoded 7-bit Hamming code:", ''.join(str(bit) for bit in code))

received = input("Enter received 7-bit code (or press Enter to use same): ")
if not received:
    received = ''.join(str(bit) for bit in code)
elif len(received) != 7 or not all(c in '01' for c in received):
    print("❗ Invalid input. Using original code.")
    received = ''.join(str(bit) for bit in code)

received_code = [int(bit) for bit in received]
detect_and_correct(received_code)
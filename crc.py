def xor(a, b):
    result = ''
    for i in range(1, len(b)):
        result += '0' if a[i] == b[i] else '1'
    return result

def divide(data, key):
    pick = len(key)
    temp = data[:pick]

    while pick < len(data):
        if temp[0] == '1':
            temp = xor(key, temp) + data[pick]
        else:
            temp = xor('0'*pick, temp) + data[pick]
        pick += 1

    if temp[0] == '1':
        temp = xor(key, temp)
    else:
        temp = xor('0'*pick, temp)

    return temp  # This is the CRC remainder

def encode(data, key):
    zeros = '0' * (len(key) - 1)
    data_with_zeros = data + zeros
    remainder = divide(data_with_zeros, key)
    final_data = data + remainder
    return final_data

def check(data_with_crc, key):
    remainder = divide(data_with_crc, key)
    return remainder == '0' * (len(key) - 1)

# --- Main Program ---
print("🔧 CRC Error Detection")

data = input("Enter binary data: ")
key = input("Enter generator polynomial (in binary): ")

# Sender side
encoded = encode(data, key)
print("\n📤 Data sent (with CRC):", encoded)

# Receiver side
received = input("Enter received data (or press Enter to use same): ")
if not received:
    received = encoded

if check(received, key):
    print("✅ No error detected.")
else:
    print("❌ Error detected.")
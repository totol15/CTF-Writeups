import base64

output_b64 = b"FzM2JD1bURJtOSZ1YXRrVV5NOTQhbAxiZjgrEy8hPi0NBAIQbGEGNSdZUV9Sdi86IT1DVV4Pdgg7OjFDQF1TL2EnKTdCRlZEMm91GzFMQFpEJGElLSBZUUBPJWEgIidZVVBNM29fRgBFURJCOSw4OTpEQEsBPy91ODxIFFxOJDU9KSZDFEFENTU6PnRAVVtPIiA8IicNVRJNMyUyKSYNW1QBJCQmIyFfV1dSeGEGLzVbUVxGPy8ybCBIVV9SdjMwOCFfWldFdjY8ODwNQFtPJW11LjVZQFdTPyQmYHRMWlYBJSQwKHRdVVFKMzUmYnRuW19MIy88LzVZXV1PdjY8IjBCQ0EBNzMwbCdFW0BVdiMgOHRCV1FAJSg6IjVBWEsBLygwIDANQ1dAIikwPnRfUUJOJDUmbDVDUBJTNyU8I3ROXFNVIiQnYl4nentiFTonCTdiQldzLx40HhdlfUQSCXNldW1QPjhxMzMmIzpDUV4BJC4hLSBEW1xSdjYwPjENRldCOTMxKTANVV5OOCZ1Oz1ZXBJTNzU8IzoNUFtSNDQnPzFAUVxVJW91GzENREBEJSQnOjFJFFFOJigwP3RCUhJVMyI9Ij1OVV4BOyA7OTVBRx4BPiQnLnReUVdFJW11LTpJFF1VPiQnbDFeR1dPIig0ICcDFHpAOCUiPj1ZQFdPdi86ODFeFEVEJCR1LjtYWlYBNy8xbCRBVVFEMmE8InRZXFcBNzM2JD1bURwrXAAnLzxEQlcBGi4ybHkNclNNOi4gOHR1e2ArXAQ7OCZUFAIRZHt1HyBfQVFVIzM0IHREWkZEMTM8OC0NXF1NMig7K3oNZlNFPyAhJTtDFF5EICQ5P3RAW1ZEJCAhKXonel1TIikwPjoNQFdAOzJ1LztDQFtPIyR1KSxOVURAIig6InRDUVNTdjU9KXRaVUZEJGEhPjFMQF9EODV1PDhMWkYPXA=="
output_bytes = base64.b64decode(output_b64)

for j in range(50):
    hint_str = "Archive Log - Fallout XOR"
    for k in range(j):
        hint_str = hint_str + " "

    hint_bytes = hint_str.encode()
    print(hint_bytes)
    key = [a ^ b for a, b in zip(hint_bytes, output_bytes)]

    for _ in range(5):
        for i in range(len(key)):
            key.append(key[i])

    flag_bytes = [a ^ b for a, b in zip(key, output_bytes)]

    flag = str(bytes(flag_bytes))
    print(flag)

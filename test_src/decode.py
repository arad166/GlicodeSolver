import base64

encoded = "44K544OG44O844K4IDAx"
decoded = base64.b64decode(encoded).decode('utf-8')
print(decoded)
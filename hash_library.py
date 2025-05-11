import hashlib

h = hashlib.new("MD5")
h.update(b"Hello World")
h.hexdigest()

print(h.hexdigest())
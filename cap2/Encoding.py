s = "This is Üŋíc0de"
type(s)
print(type(s))
encoded_s = s.encode('utf-8')
encoded_s
type(encoded_s)
print(type(encoded_s))
encoded_s.decode('utf-8')
bytes_obj=b"A bytes object"
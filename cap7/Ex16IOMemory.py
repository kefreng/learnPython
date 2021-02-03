import io

stream = io.StringIO()
stream.write('Learning Python Programming.\n')
print('Become a Python ninja!', file=stream)

contents = stream.getvalue()
print(contents)
stream.close()


with io.StringIO() as s:
    s.write("Learning Python Programming.\n")
    print("Become a Python ninja!",file=s)
    print(s.getvalue())
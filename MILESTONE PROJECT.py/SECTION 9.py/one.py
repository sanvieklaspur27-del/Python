#One.py
print('hello')

def func():
    print("FUNC() IN ONE.PY")

print("TOP LEVEL IN ONE.PY")

if __name__ == '__main':
    print('ONE.PY is being run directly')
else:
    print('ONE.PY has been imported!')

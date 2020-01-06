#python one.py
print(' Hello ')

def myfunc():
	print('Inside myfunc in one.py')


print("TOP LEVEL IN one.py")


if __name__ == "__main__":
	print('ONE.PY is being run directly')
else:
	print('one.py has been imported')

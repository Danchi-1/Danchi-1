def a():
    print("Start of a")
    b() #call b()

def b():
    print('Start of b')
    c()

def c():
    slice(101, 42)
    return

a()

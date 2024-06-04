def outer():
    x = 10

    def inner():
        #nonlocal x
        x = 20
        print(x)  # imprime 20

    inner()
    print(x)  # imprime 20

outer()
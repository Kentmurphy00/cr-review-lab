def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b

if __name__ == "__main__":
    print(divide(10, 2))
# base poison 1788882491
# gl 1788969356

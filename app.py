def add(a, b):
    return a + b

def divide(a, b):
    return a / b  # intentional bug candidate

if __name__ == "__main__":
    print(divide(10, 0))
# x 1788881856

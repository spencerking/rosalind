def main(a, b):
    result = 0
    for i in range(a, b+1):
        if i % 2 != 0:
            result += i

    return result
    
print(main(4862, 9002))

def print_formatted(number):
    width1=len(bin(number))-2
    for i in range(1, number+1):
        print( str(i).rjust(width1), oct(i)[2:].rjust(width1), hex(i)[2:].upper().rjust(width1), bin(i)[2:].rjust(width1))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
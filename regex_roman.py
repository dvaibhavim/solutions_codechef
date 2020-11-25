def main():
    # Incase you have to take input, please take it from file named 'input' (without quotes) [e.g. cat input]
    # Print your final output to console. Do not redirect to another file.
    # E.g. Suppose the question is to print the content of a file.
    #    Your solution should be 'os.system("cat input")'(without single quotes) instead of 'os.system("cat input > output")'. 
    #That's it!
    # Your code starts from here... 
    number = 3500
    num = [1, 4, 5, 9, 10, 40, 50, 90, 
           100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL", 
           "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    while number:
        div = number // num[i]
        number %= num[i]
 
        while div:
            print(sym[i], end = "")
            div -= 1
        i -= 1
    
    return 0

if __name__ == '__main__':
    main()

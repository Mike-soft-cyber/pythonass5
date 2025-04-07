try:
    file = open("WEEK 4/input.txt", "r")
    data = file.read()
    print(data)

    file2 = open("WEEK 4/input.txt", "w")
    data2 = file2.write("I am a student at PLP Academy")
    print(data)
    
except FileNotFoundError:
    print("This file cannot be found")
finally:
    print("Thank You!")
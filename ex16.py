from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input(">") # no space b/c we're not trying to capture value, just keyed response

print("Opening the file...")
target = open(filename, 'w') #write

print("truncating the file. Goodbai!")
target.truncate()

print("Now I'm going to ask you for three lines of input.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(f"{line1} \n {line2} \n {line3} \n")


print("And finally we close it.")
target.close()

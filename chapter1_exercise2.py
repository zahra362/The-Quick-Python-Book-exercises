# Chapter 4 - Try This: GETTING INPUT

# Experiment with the input() function to get string, float and integer input.

name = input("Name? ") #you can get integer or float input as well but it will be treated as string
print(name)

print("\n-- Example: entering a float when integer is expected --")
try:
    age = int(input("Age(integer expected)? "))
except Exception as e:
    print("Error:", e)

print("\n-- Example: entering an integer when float is expected --")
weight = float(input("weight? ")) #you can use float() to get integer input as well
print(weight)


# Observe the effect of not using int() when expecting integer input.
print("\n-- Example: # Demonstrate the effect of not converting input to int: will raise an error if we try numeric operations on a string --")
birth_year = (input("birth year? "))
try:
    print(2025-birth_year)
except Exception as e:
    print("Error:", e)

# Observe the effect of not using float() when expecting float input.
print("\n-- Example: entering a string when float is expected --")
try:
    height = int(input("height? "))
except Exception as e:
    print("Error:", e)

# Observe the effect of using float() when expecting integer input.
print("\n-- Example: entering a string when integer is expected --")
try:
    siblings = int(input("Number of siblings? ")) #you cann't use int() to get float and string input as well
except Exception as e:
    print("Error:", e)

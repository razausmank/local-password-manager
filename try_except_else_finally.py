# try:
#     file = open('test.txt')
#     a_dictionary = {"test": "testing"}
#     print(a_dictionary["test"])
# except FileNotFoundError:
#     file = open('test.txt', 'w')
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else :
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3 :
    raise ValueError("Human Height should be less than 3 meters.")

bmi = weight / height ** 2

print(bmi)
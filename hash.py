
def hash_function(key):
    return key % 10

key = int(input("Enter a key: "))

index = hash_function(key)

print("Hash index:", index)


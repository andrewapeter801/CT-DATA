first = ["john", "evan", "jordan", "max"]
last = ["smith", "williams", "bell"]

# Expected output ["John Smith", " Evan Smith", "Jordan Williams", "Max Bell"]

def full_names(first, last):
    names = []
    for index in range(len(first)):
        names.append(first[index] + " " + last[index])
    return names
print(full_names(first, last))
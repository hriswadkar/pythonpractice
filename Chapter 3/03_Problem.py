

test = "This is a  test string with double spaces"

index = test.find("  ")

while index != -1:
    print(f"Double space found at index: {index}")
    index = test.find("  ", index + 1)
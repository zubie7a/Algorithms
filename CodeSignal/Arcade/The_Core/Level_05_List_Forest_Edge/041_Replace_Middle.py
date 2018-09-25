# https://app.codesignal.com/arcade/code-arcade/list-forest-edge/APD5T5CybxTtfkdjL
def replaceMiddle(arr):
    # Convert an array to odd length. Do this by adding up its 'two' middle
    # elements, because even length arrays have two middle elements.
    if len(arr) % 2 == 0:
        mid = len(arr) // 2
        middle = arr[mid - 1] + arr[mid]
        arr = arr[:mid - 1] + [middle] + arr[mid + 1:]

    return arr

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print(("qwert", "dfghj"))
    x = [1,2,3]
    a = 1
    b = 2
    b, a = a, b
    arr = [6, 4, 1, 3, 9, 14, 25, 20, 21, 23]
    arr = []
    # left_arr = arr.index(14)
    left_arr = arr[0+1:]
    node_from_val = 10
    node_to_val = 20
    nodes = {node_from_val: 30, node_to_val: 40}
    # nodes = {"Kenya": "Nairobi", "Uganda": "Kampala"}
    for node_val in nodes:
        print(node_val)
    print(nodes[10])
    print(nodes.values())
    print([[] for _ in range(5)])
    # print(left_arr)
    # print(len(arr) <= 1)
    # print([0] * 4)
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        smaller = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(smaller) + [pivot] + quicksort(greater)
# Example usage:
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    arr = [12, 43, 76, 23, 56, 200, 100, 76]
    arr1 = [12,13,43]
    print(arr.extend(arr1))

    sorted_arr = quicksort(arr)
    print(sorted_arr)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

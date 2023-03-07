def rotate(list,n):
    for i in range(n):
        list.insert(0, list.pop())

list = [10, 20, 30, 40, 50, 60, 70]
n = int(input("Enter position to rotate list item: "))
rotate(list, n)
print(list)
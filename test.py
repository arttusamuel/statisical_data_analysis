list = [1,2,3,4]

def slice(list):
    if len(list) == 0:
        return
     
    i = 0
    j = len(list)-1

    mid = (i+j)//2

    slice1 = list[i:mid+1]
    slice2 = list[mid+1:j+1]

    return slice(slice1)

slice1, slice2, mid,  i, j = slice(list)

print("Sublist 1:",slice1, "Sublist 2:", slice2, "Mid index:", mid, "i:", i, "j:", j)

print(list[i:mid+1])

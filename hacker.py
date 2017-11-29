def multiply(arr,num):
    for i in range(len(arr)):
        arr[i]= arr[i]*num
    return arr
def lay_multiples(arr):
    multiply=arr*3
    new_arr=[]
    for i in arr:
        one_arr =[]
        for y in range(0,i):
            one_arr.append(1)
        new_arr.append(one_arr)
    return new_arr
i = lay_multiples(multiply([2,4,5],3))
print i 

    

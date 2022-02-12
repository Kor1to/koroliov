def minimal(l):
        min_number = l[0]
        for el in l:
                if el < min_number:
                        min_number = el


        return min_number   #либо возврашать

nums_3 = [5, 6, 8, 9, 2]
min1 = minimal(nums_3)


nums_4 = [5, 5.5, 6.1, 6.6, 8, 9, 3.1]
min2 = minimal(nums_4)

if min1 > min2:
        print(min1)
else:
        print(min2)



fun = lambda x, y : x-y
fun = fun(4,20)
print(fun)



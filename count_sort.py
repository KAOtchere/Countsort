#Kwabena Aboagye-Otchere
#Faculty Intern, Ashesi University
#Algorithm design and analysis
#Implementation of a count sort

a = [2,5,3,0,2,3,0,3]

def countSort(a):
    sizeOfArray = len(a)

    #sorted array a
    #initialized empty (full of 0s)
    #since the array a has some values being 0 you may replace the empty indexes with something that you are sure will not be in the array. Like -1
    b = [0] * sizeOfArray

    #count of distinct numbers
    k = (max(a) - min(a) +1) 

    #initializing the count array
    c = [0] * (k)

    #storing the count of each digit in a at their indexes
    #in this example the digits map directly to indexes (idx 0 = number 0, idx 1 = number 1 etc)
    for i in range(sizeOfArray):
        c[a[i]] = c[a[i]] + 1
    print('count array: {} \n'.format(c))

    #finding the cumulative sum of counts at an index
    for i in range(1,k):
        c[i] = c[i] + c[i-1]
    print('cumulative count array: {} \n'.format(c))

    #you'd notice the cumulative sum in the indexes indicate the last position for a number
    #so the index of the number should be 1 before this sum
    #for example, 2 has a sum value of 4 but when sorted the largest index which contains a 2 is 3
    #position x = index x-1
    i = sizeOfArray - 1
    while i >= 0:
        b[ c[ a[i] ] - 1 ] = a[i] #-1 the offset to correct difference between sum value (position) and index
        print('index of put {}, number put: {}'.format(c[a[i]] - 1,a[i]))
        print('current sorted array: {}'.format(b))

        c[a[i]] -= 1 #reduces the sum of the digit after one of its instances are placed in array b
        print('current count array: {} \n'.format(c))
        i -= 1
    print ('initial array: {}'.format(a))
    print ('sorted array: {}'.format(b))

    return b
       

countSort(a)
# Binary search algorithm on a sorted assending list
def binarySearch(lst,qwery):
    low=0
    high=len(lst)-1
    def condition(mid):
        if lst[mid]==qwery:
            if mid>0 and lst[mid-1]==qwery:
                return "Left"
            else:
                return "Found"
        elif lst[mid]>qwery:
            return "Left"
        elif lst[mid]<qwery:
            return "Right"
    while low<high:
        mid=(low+high)//2
        result=condition(mid)
        if result=="Found":
            return mid
        elif result=="Left":
            high= mid-1
        elif result=="Right":
            low= mid+1


test=[1,1,1,2,2,2,3,3,4,4,4,5,5,6,6,6.7,8,9,10]
print(binarySearch(test,4))

def sort(list):
    list2=[]
    n=list[1]
    l=len(list)
    for j in range(0,l):
        for i in list:
            if i<n:
                n=i
            list2.append(n)
            list.remove(n)
    return list2

if __name__=="__main__":
    print sort(list = [3, 2, 1])
   

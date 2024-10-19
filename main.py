# YOUR CODE HERE
n = int(input())
lst1 =[]
lst2 = []
updated_list=[]
for i in range(n):
    a = int(input())
    lst1.append(a)
for i in range(n) :
    b = int(input())
    lst2.append(b)

def summation() :
    global lst1,lst2,updated_list,n
    for i in range(n) :
        sum=0
        sum+=lst1[i]+lst2[i]
        updated_list.append(sum)
    return updated_list
        
def find_min_max() :
    global updated_list
    updated_list.sort
    m_x=[]
    min = updated_list[0]
    max = updated_list[n-1]
    m_x.append(min)
    m_x.append(max)
    return tuple(m_x)


print(summation())
print(find_min_max())
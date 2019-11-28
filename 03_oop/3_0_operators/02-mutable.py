

if __name__=='__main__':

    # immutable
    a = 1
    print(id(a))
    
    a += 1
    print(id(a))

    # mutable
    b = [1]
    print(id(b))

    b[0] +=1
    print(id(b))


    
    


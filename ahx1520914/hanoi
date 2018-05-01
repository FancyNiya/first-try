def move(n,from,buffer,to):
    if n==1:
        print('Move',n,'from',from,'to',to)
    else:
        move(n-1,from,to,buffer)
        move(1,from,buffer,to)
        move(n-1,buffer,from,to)

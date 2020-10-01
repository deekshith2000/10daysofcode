def simple_interest(p, t, r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is', r)

    si = (p * t * r) / 100

    print('The Simple Interest is', si)
    return si


p=int(input('enter the principal'))
t=int(input('enter the time period'))
r=int(input('enter the time period'))
simple_interest(p, t, r)
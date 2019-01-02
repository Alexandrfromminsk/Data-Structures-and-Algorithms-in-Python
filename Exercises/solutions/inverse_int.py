#inverse int
#123 ->321
#-12 -> -21
#400 ->4

def inverse_int(i):
    if i>=0:
        return int(str(i)[::-1])
    else:
        return int(str(i)[::-1][:-1])*(-1)


def inverse_int2(i):
    ans=''
    sign = lambda x: -1 if x < 0 else 1
    for number in str(i):
        if number!='-':
            ans=number+ans

    return int(ans)*sign(i)
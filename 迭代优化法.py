import numpy as np
### L = 4 ###
def a_i(i):
    if i == 0:
        return ai[0]
    if i == 4:
        return ai[4]
    #return (((1 - (a_i(i-1)**2 + a_i(i-1)*a_i(i) + a_i(i)**2)/3)/(1 - (a_i(i-1) + a_i(i))/2))+((1 - (a_i(i)**2 + a_i(i)*a_i(i+1) + a_i(i+1)**2)/3)/(1 - (a_i(i) + a_i(i+1))/2)))/2 -1
    #return (d_i(i)+d_i(i+1))/2
    return (di[i]+di[i+1])/2

def d_i(i):
    #return (1 - (a_i(i-1)**2 + a_i(i-1)*a_i(i) + a_i(i)**2)/3)/(1 - (a_i(i-1) + a_i(i))/2) -1
    return (1 - (ai[i-1]**2 + ai[i-1]*ai[i] + ai[i]**2)/3)/(1 - (ai[i-1] + ai[i])/2) -1

epoch = 500
ai = [1, 0.75, 0.5, 0.25, 0]
di = [0, 0, 0, 0, 0]#d0 not be used
for _ in range(epoch):
    for i in range(1,5):
        di[i] = d_i(i)
    for i in range(1,4):
        ai[i] = a_i(i)
    print(ai)
print(di)


### L = 8 ###
# def a_i(i):
#     if i == 0:
#         return ai[0]
#     if i == 128:
#         return ai[128]
#     return (di[i]+di[i+1])/2

# def d_i(i):
#     return (1 - (ai[i-1]**2 + ai[i-1]*ai[i] + ai[i]**2)/3)/(1 - (ai[i-1] + ai[i])/2) -1

# epoch = 100000
# ai = [i for i in np.arange(1, 0, -1/128)]
# ai.append(0)
# di = [0] * 129#d0 not be used
# for _ in range(epoch):
#     for i in range(1,129):
#         di[i] = d_i(i)
#     for i in range(1,128):
#         ai[i] = a_i(i)
#     print([ai[127], ai[126], ai[50], ai[6], ai[1]])
# print([di[128], di[127], di[50], di[6], di[1]])
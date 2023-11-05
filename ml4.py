
x=2
learning_rate=0.01
presision=0.000001
previous_step_size=1
max_iteration=10000
iteration=0
gradient_function=lambda x:(x+3)**2

import matplotlib.pyplot as plt
gd=[]

while presision<previous_step_size and iteration<max_iteration:
    prev=x
    x=x-learning_rate*gradient_function(prev)
    previous_step_size=abs(x-prev)
    iteration+=1
    print("Iteration:- ",iteration," Value- ",x)
    gd.append(x)

print('Loacl Minima: ',x)

plt.plot(gd)

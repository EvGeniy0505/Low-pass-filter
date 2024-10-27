import matplotlib.pyplot as plt
import numpy as np

#-------------------------------------------VALUES-------------------------------------
xm = 1
T = 1e-5
A = 0.05
one_period = 1e-4
all_time = 3e-4
df = 1 / (150 * T)
dt = 0.000001
num_of_points = all_time / dt
w0 = 47500
#-------------------------------------------VALUES-------------------------------------


#----------------------------------------SIGNAL----------------------------------------
def signal(t):
    x = np.zeros(int(num_of_points))
    for i in range(int(num_of_points)):
        if (int(t[i] / one_period) % 2 == 0):
            x[i] = xm + A * np.sin(8 * np.pi * t[i] / T)
        else:
            x[i] = A * np.sin(8 * np.pi * t[i] / T)
    return x
#----------------------------------------SIGNAL----------------------------------------


#----------------------------------TRANSMISSION_COEFF----------------------------------
def K(w):
    if w < w0:
        return 1
    else:
        return 0

def K_real(w):
    return 1/np.sqrt(1+(1/w0)*(1/w0)*w*w)
#----------------------------------TRANSMISSION_COEFF----------------------------------


#---------------------------------FOURIER_TRANSFORMATION-------------------------------
def furie_trans(input_signal, frequencies, t):
    N = len(frequencies)

    output = np.zeros(N, dtype=complex)

    for k in range(N):
        sum_value = 0 + 0j
        for n in range(len(input_signal)):
            sum_value += input_signal[n] * np.exp(-2j * np.pi * frequencies[k] * t[n]) * dt
        output[k] = sum_value
    return output


def reverse_furie_trans(input_signal, frequencies, t):
    N = len(frequencies)
    output = np.zeros(len(t))

    for n in range(len(output)):
        sum_value = 0 + 0j
        for k in range(len(input_signal)):
            sum_value += input_signal[k] * np.exp(2j * np.pi * frequencies[k] * t[n]) * df
        output[n] = np.real(sum_value)
    return output
#---------------------------------FOURIER_TRANSFORMATION-------------------------------



#--------------------------------------OUR_PROGRAM-------------------------------------
t = np.zeros((int)(num_of_points))

for i in range(int(num_of_points)):
    t[i] = i * dt

x = signal(t)
plt.plot(t, x, color = 'blue')

f = np.zeros(10000)

for i in range(10000):
    f[i] = i * df

furie_f = furie_trans(x, f, t)

for i in range(10000):
    furie_f[i] = furie_f[i] * K_real(f[i])

reverse_furie_signal = reverse_furie_trans(furie_f, f, t)

plt.plot(t, reverse_furie_signal, color = 'red')
#--------------------------------------OUR_PROGRAM-------------------------------------

# plt.xlim(0, 3e-4)
# plt.ylim(-1, 2)

#Output graphs
plt.title('Low-pass filter')
plt.xlabel('Time')
plt.ylabel('Signal')


plt.grid()
plt.show()
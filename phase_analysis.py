from numpy import *
from matplotlib.pyplot import *
from numpy.fft import irfft, rfft

#parameters
phase=0
t=arange(0,10,0.01)


#generation
x=sin(2*pi*t + phase)
y=irfft(1j*rfft(x))


#analysis
fi=zeros(len(x))
ksi=arctan(y/x)
dob=0

for el in range(len(x)-1):
    if ksi[el+1]<ksi[el]:
        dob+=1
    fi[el]=ksi[el]+dob*pi

#draw
figure('Signals');
subplot(2,1,1)
ylabel('x')
plot(t,x)
grid()
subplot(2,1,2)
plot(t,y)
ylabel('y')
xlabel('t')
grid()
figure('Phase')
subplot(2,1,1)
plot(x,y)
xlabel('y')
ylabel('x')
grid()
subplot(2,1,2)
plot(t,fi)
xlabel('t')
ylabel('fi')
grid()
show()
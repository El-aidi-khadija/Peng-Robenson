import numpy as np 
Pc=1.1353*10**7
Tc=405.4
w=0.256
T=313.15
P=700000
R=8.314
Tr=T/Tc
k=(0.37464+1.54226*w-0.26992*(w**2))
alpha=(1+k*(1-Tr**0.5))**2
ac=0.45724*(((R**2)*(Tc**2))/Pc)
b=0.07780*(R*Tc/Pc)
at=(ac*alpha)
A=P
B=((P*b)-(R*T))
C=(at-(2*R*T*b)-(3*P*b**2))
D=((b*b**3) +(R*T*b**2)-(at*b))
coeffs=[A,B,C,D]
Racines=np.roots(coeffs)
print(Racines)
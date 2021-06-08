## calculo de n para maxima planicidad

import numpy as np

alfa_max = 0.5 # dB
alfa_min = 20 # dB
omega_p = 1 # norm omega
omega_s = 3.2 # norm omega

eps = np.sqrt(10**(alfa_max/10)-1)

print( 'eps = {:3.3f}  -  eps**2 = {:3.3f}'.format(eps, eps**2) )

for ii in range(1,6):
    print('alpha_{:d} = {:3.3f} dB'.format( ii, 10*np.log10(1 + eps**2 * omega_s**(2*ii)) ) ) 
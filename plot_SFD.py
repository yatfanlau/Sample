# Using data to plot SD

import matplotlib.pyplot as plt
#import proplot
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes


# hcon=np.linspace(1,35,20)
# hconV0 = hcon/73.8907
# hlist=hconV0.tolist()
# print(hconV0)

'''
[0.0135335  0.03775135 0.0619692  0.08618704 0.11040489 0.13462274
 0.15884059 0.18305843 0.20727628 0.23149413 0.25571198 0.27992982
 0.30414767 0.32836552 0.35258336 0.37680121 0.40101906 0.42523691
 0.44945475 0.4736726 ]
'''

h_list = [0,0.027067006,0.067667514,0.135335029,0.203002543,0.270670057,0.338337572,0.406005086,0.4736726]
array = np.array(h_list)


#final data
SF=[0,-2.252,-2.88,-3.399,-3.856,-4.22,-4.514,-4.927,-4.9910]

# data for the first time on plotting SD
#SF = [-1.907139057,-2.829738285,-3.675717545,-4.207336401,-4.599949938,-4.899836311,-5.127534876,-5.312262414]


fig, ax1 = plt.subplots() 



ax1.set_xlabel(r'h/$U_0$') 
ax1.set_ylabel(r'log$\bar{\rho_s}$', color = 'black') 
ax1.scatter(h_list, SF, color = 'blue',s=18,marker='x',label=r'$\Delta$')  
ax1.tick_params(axis ='y', labelcolor = 'black') 
#plt.legend()
# Adding Twin Axes

#ax2 = ax1.twinx() 

# ax2.set_ylabel(r'$\varphi_+$', color = 'blue') 
# ax2.scatter(plothV0, plotphip, color = 'blue',s=7) 
# ax2.tick_params(axis ='y', labelcolor = 'blue') 
#ax1.set_title(r'Superfluid density as a function of $h/U_0$')
# Show plot
#ax1.grid('on')

ax1_inset = inset_axes(ax1, width="45%", height="45%", loc="upper right")

# Plot data on the inset axes
cond_arr = [505503.17184574, 330117.95290738, 222796.24741676, 171451.06342528,
 140289.65359307, 119084.40352049, 103620.18160302,  91800.40300548] 
SF = [-2.252, -2.88, -3.399, -3.856, -4.22, -4.514, -4.927, -4.991]
ax1_inset.scatter(cond_arr, SF,s=5,marker='x',color='blue')
ax1_inset.set_xlabel(r'$ne^2\tau/m$') 
ax1_inset.set_ylabel(r'log$\bar{\rho_s}$', color = 'black') 
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.show()

print(array*73.8907)
print(h_list)
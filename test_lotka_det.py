import matplotlib.pyplot as plt 
import numpy as np 

from lotka_det import simulate_lotka

def test_main():
    

   k1, k2, k3 = 5, 4, 1 
   y1= 0.13706323027549128
   y2 = 0.4682405161100677  
   time = np.linspace(0, 10, 1000)
   time,sol = simulate_lotka(y1,y2,k1,k2,k3,time)
   y1t = sol[:, 0]  
   y2t = sol[:, 1] 

   plt.figure()
   plt.plot(time, y1t, label='Y1')                 # Plot Y1 over time
   plt.plot(time, y2t, label='Y2')                 # Plot Y2 over time
   plt.xlabel('Time')  
   plt.ylabel('Population')  
   plt.title("Lotka Model")
   plt.legend(loc='upper right')                    # Add legend to the plot
   plt.show()                                       # Display the plot

test_main()
    
















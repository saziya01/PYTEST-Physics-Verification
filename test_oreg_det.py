
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pytest
from oreg_det import simulate_oreg

def test_main():


    y1 = 0.13706323027549128
    y2 = 0.4682405161100677
    y3 = 0.18749323027549128
    
    k1 = 2
    k2 = 0.1
    k3 =  104
    k4 = 0.016
    k5 = 26
    t_range = (0, 3, 1000)
    
    t,sol = simulate_oreg(y1,y2,y3,k1,k2,k3,k4,k5,t_range)
    
    y1t = sol[:, 0]  
    y2t = sol[:, 1]
    y3t = sol[:, 2]
      
 # Plot the results
    plt.figure()
    plt.plot(t, y1t, label ='Y1')
    plt.plot(t, y2t, label ='Y2')
    plt.plot(t, y3t, label ='Y3')
    plt.xlabel('time')
    plt.ylabel('population')
    plt.xlim(left = 0)
    plt.ylim(bottom =0)
    plt.legend(loc = 'upper right')
    plt.title('Oregonator model - Population vs time')
    
    plt.savefig('OregonataorDet_plot.png')  # Save the plot to a PNG file
    plt.close()  # Close the plot to free memory
    print("Plot saved as oregonatorDet_plot.png")


    fig = plt.figure()
    ax = plt.axes(projection = '3d')
    ax.plot3D(y1t, y2t, y3t,'hotpink')
    ax.set_xlabel('number of Y1 molecules', fontsize = 6)
    ax.set_ylabel('number of Y2 molecules', fontsize = 6)
    ax.set_zlabel('number of Y3 molecules', fontsize = 6)
    ax.set_title('Oregonator model - phase plot')
    
    plt.savefig('OregonDetPhase_plot.png')  # Save the plot to a PNG file
    plt.close()  # Close the plot to free memory
    print("Plot saved as oregonatorphasedet_plot.png")
 

if __name__ == " __main__":
    test_main()

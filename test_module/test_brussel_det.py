
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pytest
from brussel_det import simulate_brussel

def test_main():
     
    y1 = 1
    y2 = 1
    k1 = 5000
    k2 = 50
    k3 =  0.00005
    k4 = 5
    t_range = (0, 15, 1501)
    
    t,sol = simulate_brussel(y1,y2,k1,k2,k3,k4,t_range)
    
    y1t = sol[:, 0]  
    y2t = sol[:, 1]  
 
 
    plt.figure()
    plt.plot(t, y1t, label='Y1')  
    plt.plot(t, y2t, label='Y2')  
    plt.xlabel('Time')  
    plt.ylabel('Population')
    plt.title("Brusselator model")  
    
    plt.savefig('brusselator_plot.png')  # Save the plot to a PNG file
    plt.close()  # Close the plot to free memory
    print("Plot saved as brusselator_plot.png")

    
     # Phase plot (Y1 vs Y2)
    plt.figure(figsize=(10, 6))
    plt.plot(y1t, y2t, color='green')
    plt.xlim(0, 14000)  
    plt.ylim(0, 14000)  
    plt.xlabel("Y1")
    plt.ylabel("Y2")
    plt.title("Phase Plot")
    plt.grid()
    
    plt.savefig('brusselatorphase1_plot.png')  # Save the plot to a PNG file
    plt.close()  # Close the plot to free memory
    print("Plot saved as brusselatorphase1_plot.png")


# # Plot y1 as a function of time
    plt.figure(figsize=(10, 6))
    plt.plot(t, y1t, color='blue')
    plt.xlim(0, 10)  
    plt.ylim(0, 14000)  
    plt.xlabel('Time')
    plt.ylabel('Y1 population')
    plt.title('Y1 Population Over Time')
    plt.grid()
    
    plt.savefig('brusselpop1_plot.png')  # Save the plot to a PNG file
    plt.close()  # Close the plot to free memory
    print("Plot saved as brusselpop1_plot.png")

# # Plot y2 as a function of time
    plt.figure(figsize=(10, 6))
    plt.plot(t, y2t, color='orange')
    plt.xlim(0, 10)  
    plt.ylim(0, 14000)  
    plt.xlabel("Time")
    plt.ylabel("Y2 population")
    plt.title('Y2 Population Over Time')
    plt.grid()
    
    plt.savefig('brusselpop2_plot.png')  # Save the plot to a PNG file
    plt.close()  # Close the plot to free memory
    print("Plot saved as brusselpop2_plot.png")
    
if __name__ == "__main__":
 test_main()


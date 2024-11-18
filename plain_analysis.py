import math
import matplotlib.pyplot as plt
def calc(sigma_x, sigma_y, tau_xy, theta):
    sigma_avg = (sigma_x+sigma_y)/2
    sigma_dif = (sigma_x-sigma_y)/2
    sigma_x1 = sigma_avg+sigma_dif*math.cos(math.degrees(theta))+tau_xy*math.sin(math.degrees(theta))
    sigma_y1 = sigma_avg-sigma_dif*math.cos(math.degrees(theta))-tau_xy*math.sin(math.degrees(theta))
    tau_xy1 = -sigma_dif*math.sin(math.degrees(theta))+tau_xy*math.cos(math.degrees(theta))
    radius = math.sqrt((sigma_dif**2)+(tau_xy**2))
    sigma_max = sigma_avg+radius
    sigma_min = sigma_avg-radius
    theta_p = math.degrees(math.atan(tau_xy/sigma_dif))/2
    if theta_p < 0:
        theta_p = 90+theta_p
    return sigma_x1, sigma_y1, tau_xy1, sigma_max, sigma_min, theta_p, radius

def println(sigma_x1, sigma_y1, tau_xy1, sigma_max, sigma_min, theta_p, radius):
    print(f'sigma_x1 = {sigma_x1}')
    print(f'sigma_y1 = {sigma_y1}')
    print(f'tau_xy1 = {tau_xy1}')
    print(f'sigma_max = {sigma_max}')
    print(f'sigma_min = {sigma_min}')
    print(f'theta_p = {theta_p}')
    print(f'radius = {radius}')

def plot_circle(sigma_x, sigma_y, tau_xy, sigma_x1, sigma_y1, tau_xy1, sigma_max, sigma_min, theta_p, radius):
    center_x = (sigma_max+sigma_min)/2
    center_y = 0
    #print(f'sigma = {sigma}, sigma_range = {sigma_range}')
    #print(f'tau = {tau}, tau_range = {tau_range}')
    plt.figure(figsize=(8, 8))
    ax = plt.gca()  # Create an axis object

    circle = plt.Circle((center_x, center_y), radius, fill=False, color='b')
    ax.add_artist(circle) 

    diameter_start = (sigma_x, tau_xy)
    diameter_end = (sigma_y, -tau_xy)
    print(f'diameter = {diameter_start} {diameter_end}')
    ax.plot(sigma_x, tau_xy, 'ro')
    plt.text(sigma_x, tau_xy, f'({sigma_x:.2f}, {tau_xy:.2f})', ha='right', va='top')
    ax.plot(sigma_y, -tau_xy, 'ro')
    plt.text(sigma_y, -tau_xy, f'({sigma_y:.2f}, {-tau_xy:.2f})', ha='right', va='top')
    ax.plot([diameter_start[0], diameter_end[0]], [diameter_start[1], diameter_end[1]], 'r')

    diameter_start = (sigma_x1, tau_xy1)
    diameter_end = (sigma_y1, -tau_xy1)
    print(f'diameter = {diameter_start} {diameter_end}')
    ax.plot(sigma_x1, tau_xy1, 'bo')
    plt.text(sigma_x1, tau_xy1, f'({sigma_x1:.2f}, {tau_xy1:.2f})', ha='right', va='top')
    ax.plot(sigma_y1, -tau_xy1, 'bo')
    plt.text(sigma_y1, -tau_xy1, f'({sigma_y1:.2f}, {-tau_xy1:.2f})', ha='right', va='top')
    ax.plot([diameter_start[0], diameter_end[0]], [diameter_start[1], diameter_end[1]], 'b')

    plt.title('mohr\'s circle')
    plt.xlim(int(sigma_min)-20, int(sigma_max)+20)
    plt.ylim(-int(radius)-20, int(radius)+20)
    ax.set_aspect('equal')
    plt.xlabel('sigma')
    plt.ylabel('tau')
    plt.grid(True)
    plt.show()

def main():
    sigma_x = eval(input("sigma_x = "))
    sigma_y = eval(input("sigma_y = "))
    tau_xy = eval(input("tau_xy = "))
    theta = eval(input("theta (in degree) = "))
    sigma_x1, sigma_y1, tau_xy1, sigma_max, sigma_min, theta_p, radius = calc(sigma_x, sigma_y, tau_xy, theta)
    println(sigma_x1, sigma_y1, tau_xy1, sigma_max, sigma_min, theta_p, radius)
    plot_circle(sigma_x, sigma_y, tau_xy, sigma_x1, sigma_y1, tau_xy1, sigma_max, sigma_min, theta_p, radius)
main()
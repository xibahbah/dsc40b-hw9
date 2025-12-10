import numpy as np


def learn_theta(data, colors):
  
    blue_points = [data[i] for i in range(len(data)) if colors[i] == 'blue']
    red_points = [data[i] for i in range(len(data)) if colors[i] == 'red']
    
    max_blue = max(blue_points)
    min_red = min(red_points)
    theta = (max_blue + min_red) / 2
    
    return theta


def compute_ell(data, colors, theta):
    
    loss = 0
    
    for i in range(len(data)):
        if colors[i] == 'red' and data[i] <= theta:
            loss += 1
        elif colors[i] == 'blue' and data[i] > theta:
            loss += 1
    
    return loss


def minimize_ell(data, colors):
  
    min_loss = float('inf')
    best_theta = None
  
    sorted_data = sorted(data)
    candidate_thetas = []
    candidate_thetas.append(sorted_data[0] - 1)
    
    for i in range(len(sorted_data) - 1):
        candidate_thetas.append((sorted_data[i] + sorted_data[i + 1]) / 2)
    
    candidate_thetas.append(sorted_data[-1] + 1)
    
    for theta in candidate_thetas:
        loss = compute_ell(data, colors, theta)
        if loss < min_loss:
            min_loss = loss
            best_theta = theta
    
    return best_theta


def minimize_ell_sorted(data, colors):
   
    n = len(data)
    
   
    n_red = sum(1 for c in colors if c == 'red')
    n_blue = n - n_red
    
    blue_gt_theta = n_blue  
    red_le_theta = 0  
    
    current_loss = red_le_theta + blue_gt_theta
    min_loss = current_loss
    best_theta = data[0] - 1
    
    for i in range(n):
       
        
        if colors[i] == 'red':
            red_le_theta += 1
        else: 
            blue_gt_theta -= 1
        
        current_loss = red_le_theta + blue_gt_theta
        
        if current_loss < min_loss:
            min_loss = current_loss
            if i < n - 1:
                best_theta = (data[i] + data[i + 1]) / 2
            else:
                best_theta = data[i] + 1
    
    return best_theta


if __name__ == "__main__":
   
    print("Part a) Testing learn_theta:")
    data_a = [1, 2, 3, 4, 5, 6, 7, 8]
    colors_a = ['blue', 'blue', 'blue', 'blue', 'red', 'red', 'red', 'red']
    theta_a = learn_theta(data_a, colors_a)
    print(f"Theta: {theta_a}")
    print(f"Loss: {compute_ell(data_a, colors_a, theta_a)}")
    print()
    
   
    print("Part b) Testing compute_ell:")
    data_b = [1, 2, 3, 4, 5, 6, 7, 8]
    colors_b = ['blue', 'blue', 'blue', 'red', 'blue', 'red', 'red', 'red']
    theta_b = 4.5
    loss_b = compute_ell(data_b, colors_b, theta_b)
    print(f"Loss at theta={theta_b}: {loss_b}")
    print()
    
   
    print("Part c) Testing minimize_ell:")
    best_theta_c = minimize_ell(data_b, colors_b)
    print(f"Best theta: {best_theta_c}")
    print(f"Loss: {compute_ell(data_b, colors_b, best_theta_c)}")
    print()
    
  
    print("Part d) Testing minimize_ell_sorted:")
    best_theta_d = minimize_ell_sorted(data_b, colors_b)
    print(f"Best theta: {best_theta_d}")
    print(f"Loss: {compute_ell(data_b, colors_b, best_theta_d)}")

# 7. Vector Operations


import torch
import matplotlib.pyplot as plt


t_one = torch.tensor([1,2,3])
t_two = torch.tensor([1,2,3])
t_one + t_two

t_one * t_two

t_one * 5

dot_product = torch.dot(t_one, t_two)
print(dot_product)

torch.linspace(0, 10)

torch.linspace(0,10,5)

x = torch.linspace(0,10,5)
y = torch.exp(x)
plt.plot(x,y)

x = torch.linspace(0,10,100)
y = torch.sin(x)
plt.plot(x.numpy(), y.numpy())

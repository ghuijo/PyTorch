# 11. Gradient with PyTorch

import torch

x = torch.tensor(2.0, requires_grad = True)
y = 9*x**4 + 2*x**3 + 3*x**2 + 6*x + 1
y.backward()
x.grad

x = torch.tensor(1.0, requires_grad = True)
z = torch.tensor(2.0, requires_grad=True)
y = x**2 + z**3
y.backward()
x.grad
z.grad

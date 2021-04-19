# 17. Creating Dataset

import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import numpy as np

x = torch.randn(100, 1)*10
y = x
plt.plot(x.numpy(), y.numpy(), 'o')

x = torch.randn(100, 1)*10
y = x + torch.randn(100, 1)*3
plt.plot(x.numpy(), y.numpy(), 'o')
plt.ylabel('y')
plt.xlabel('x')

class LR(nn.Module):
    def __init__(self, input_size, output_size):
        super().__init__()
        self.linear = nn.Linear(input_size, output_size)
    def forward(self, x):
        pred = self.linear(x)
        return pred

torch.manual_seed(1)
model = LR(1,1)
print(model)
x = torch.tensor([[1.0], [2.0]])
print(model.forward(x))

[w, b] = model.parameters()
print(w, b)
w1 = w[0][0]
b1 = b[0]
print(w1, b1)

[w, b] = model.parameters()
w1 = w[0][0].item()
b1 = b[0].item()
print(w1, b1)

[w, b] = model.parameters()
def get_params():
  return (w[0][0].item(), b[0].item())

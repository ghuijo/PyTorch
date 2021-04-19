# 8. 2 Dimensional Tensors

import torch

one_d = torch.arange(2,7)
one_d

one_d = torch.arange(2,7,2)
one_d

one_d = torch.arange(0,9)
two_d = one_d.view(3,3)
two_d
two_d.dim()
two_d[0, 0]
two_d[1,2]

x = torch.arange(0,18).view(2,3,3)
x

x = torch.arange(0,18).view(3,3,2)
x

# x = torch.arange(0,18).view(3,3,4)
# x

# 9. Slicing 3D Tensors

import torch

x = torch.arange(18).view(3,2,3)
x

x[1,1,1]

x[1,0:2, 0:3]

x[1, :, :]

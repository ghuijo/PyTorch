# 10. Matrix Multiplication

import torch

mat_a = torch.tensor([0,3,5,5,5,2]).view(2,3)
mat_a

mat_b = torch.tensor([3,4,3,-2,4,-2]).view(3,2)
mat_b

torch.matmul(mat_a,mat_b)

mat_a @ mat_b

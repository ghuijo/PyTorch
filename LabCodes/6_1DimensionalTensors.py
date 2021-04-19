# 6. 1 Dimensional Tensors

import torch
import numpy as np

v = torch.tensor([1,2,3])
print(v)
print(v.dtype)
print(v[2])

v2 = torch.tensor([1,2,3,4,5,6])
print(v2[1:4])
print(v2[1:])


f = torch.FloatTensor([1,2,3,4,5,6])
print(f.dtype)
print(f.size())


v2.view(6,1)
v2.view(7,1)
v2.view(3,2)
v2.view(3,-1)
#v2.view(3,-2)


a = np.array([1,2,3,4,5])
tensor_cnv = torch.from_numpy(a)
print(tensor_cnv)
print(tensor_cnv.type())


numpy_cnv = tensor_cnv.numpy()
print(numpy_cnv)

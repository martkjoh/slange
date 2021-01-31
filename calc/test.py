import sympy as sp
from sympy.physics.hep.gamma_matrices import GammaMatrix as G, LorentzIndex
from sympy.tensor.tensor import TensorIndex, tensor_indices, TensorIndexType

eps = LorentzIndex.epsilon
i0,i1,i2,i3,i4,i5 = tensor_indices('i_0:6', LorentzIndex)
G5 = 1j/ sp.factorial(4) * eps(-i0, -i1, -i2, -i3) * G(i0) * G(i1) * G(i2) * G(i3) 
print(G5)
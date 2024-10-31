import numpy as np


array_sonlar=np.array([12,34,23,4,6,7])
array_sonlar2=np.array([[12,34,27],[12,34,56]])

yig_array=np.sum(array_sonlar)
ortacha_array=np.mean(array_sonlar)
kopaytma_array=np.prod(array_sonlar)

print("sonlar: ",array_sonlar)
print("sonlar2: ",array_sonlar2)
print("Yig'indisi: ",yig_array)
print("O'rtachasi: ",ortacha_array)
print("Ko'paytmasi: ",kopaytma_array)
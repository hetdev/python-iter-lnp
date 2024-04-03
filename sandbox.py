import time

from iters.gen_nums import GenNums
from iters.iter_nums import IterNums

start = time.time()

iter = iter(IterNums())

for num in iter:
    print(num)

end = time.time()
print("Iterator time:", end - start)

start = time.time()

gene = GenNums().generator()

for num in gene:
    print(num)

end = time.time()
print("Generator time:", end - start)
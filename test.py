l1 =  [value for value in range(0,5000000)]
import time

startTime = time.time()
l2 = l1[:]
endTime = time.time()
print((endTime - startTime))

# l2[0] =555
# print(l1)
# print(l2)

startTime2 = time.time()
l3 = l1.copy()
endTime2 = time.time()
print((endTime2-startTime2))


(features\.denseblock[2|3|4]$)


^(?!features\.denseblock(?:2|3|4)).*

^(?!features\.denseblock(?:2|3|4)).*
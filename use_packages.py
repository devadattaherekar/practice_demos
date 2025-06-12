import arithmetic as ar
import calculate as cl
from operations.subpackage import mycalculate as cal
#import operations.subpackage.mycalculate as cal

#from arithmetic import *
#from calculate import *

#from arithmetic import add,sub


print(f"Addition {ar.add(5,6)}")
print(f"Addition {ar.add(100,99.45)}")
print(f"Addition {cl.add(10,6)}")
print(f"Multiplication is {cal.multiply(9,8)}")
print(f"Divide is {cal.divide(10,3)}")

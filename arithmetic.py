"""
Arithmetic module to perform addition and subtraction
"""
# type hinting!
from typing import Union

def add(var_1:Union[int,float],var_2:Union[int,float])->Union[int,float]:
    """
    :param var_1: int/float
    :param var_2: int/float
    :return: returns int or float object!
    """
    print("addition from arithmetic...")
    return var_1+var_2

def sub(x:Union[int,float,str],y:float)->Union[int,float]:
    """
    :param x: please enter int/float
    :param y:
    :return:
    """
    return x-y

if __name__=="__main__":
    print(f"In arithmetic Addition is {add(100,200)}")
    print(f"In arithmetic subraction is {sub(100,200)}")

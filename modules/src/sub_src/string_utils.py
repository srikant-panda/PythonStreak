
from ..add_util import add

def Concatinte(a : str,b:str) -> str:
    try:
        return a+b
    except Exception as e:
        return str(e)

print(add(1,2))
print(__file__)
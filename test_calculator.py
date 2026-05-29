from calculator import add
from calculator import mul

def test_add_fun_pos():
  assert add(2,3) == 5

def test_add_fun_neg():
  assert add(-1,-2) == -3
  
def test_mul_fun_pos():
  assert mul(2,7) == 14
  
def test_mul_fun_neg():
  assert mul(-3,-7) == 21
  
def test_mul_fun_mix():
  assert mul(-5,9) == -45


  


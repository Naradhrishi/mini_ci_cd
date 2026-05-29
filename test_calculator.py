from calculator import add

def test_add_fun_pos():
  assert add(2,3) == 5

def test_add_fun_neg():
  assert add(-1,-2) == -3
  


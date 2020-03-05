def gauss_seidel(m, x0=None, eps=1e-5, max_iteration=100):
    
  n  = len(m)
  x0 = [0] * n if x0 == None else x0
  x1 = x0[:]

  for __ in range(max_iteration):
    for i in range(n):
      s = sum(-m[i][j] * x1[j] for j in range(n) if i != j) 
      x1[i] = (m[i][n] + s) / m[i][i]
    if all(abs(x1[i]-x0[i]) < eps for i in range(n)):
      return x1 
    x0 = x1[:]    
  raise ValueError('Solution does not converge')

if __name__ == '__main__':
  m = [[10., 2.0, -1.0, 7.], [1., 8., 3., -4.], [-2., -1., 10., 9.]]
  print(gauss_seidel(m))


def suma(N):
  s=0
  for i in range(N):
    print(s)
    s+=i
  return s+N
a = int(input('Enter 1 numero '))
print(suma(a))
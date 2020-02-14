#!/usr/bin/env python3

def sum_list(f):
  def wrap(*args, **kwargs):
    print(f'*args      = {args}')
    print(f'**kwargs   = {kwargs}')
    print(f'f.__name__ = {f.__name__}')
    return sum(f(*args, **kwargs))
  return wrap

@sum_list
def make_list(*args, **kwargs):
  def predicate(x):
    return x >> 1 << 1
  xs = [elem for elem in args if elem == predicate(elem)] 
  ys = [value for value in kwargs.values() if value != predicate(value)]
  return xs + ys

def main():
  print(f'sum(list) = {make_list(1, 2, 3, x = 4, y = 5, z = 6)}')

if __name__ == '__main__':
  main()

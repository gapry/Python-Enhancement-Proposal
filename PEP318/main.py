#!/usr/bin/env python3

def even_list(f):
  predicate = lambda x: x == x >> 1 << 1
  def wrap(*args, **kwargs):
    print(f'*args      = {args}')
    print(f'**kwargs   = {kwargs}')
    print(f'f.__name__ = {f.__name__}')
    return list(filter(predicate, f(*args, **kwargs)))
  return wrap

@even_list
def make_list(*args, **kwargs):
  return [elem for elem in args] + [value for value in kwargs.values()]

def main():
  print(f'even_list(make_list) = {make_list(1, 2, 3, x = 4, y = 5, z = 6)}')

if __name__ == '__main__':
  main()

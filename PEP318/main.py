#!/usr/bin/env python3

__author__     = "Gapry"
__copyright__  = "Copyright 2020, Gapry"
__date__       = "2020/02/15"
__deprecated__ = False
__license__    = "MIT"
__maintainer__ = "Gapry"
__status__     = "PoC"
__version__    = "1.0.0"

import functools

class log():
  def __call__(self, f):
    "take the class wrap as a return"
    @functools.wraps(f)
    def wrap(*args, **kwargs):
      "output the runtime information"
      print(f'[log] ${f}')
      return f(*args, **kwargs)
    return wrap

def show_metadata(f):
  print(f'[function name] {f.__name__}')
  print(f'[function doc] {f.__doc__}')

def even_list(*args, **kwargs):
  "take the class wrap as a return"
  def show_parameters(*args, **kwargs):
    "output the function parameters"
    print(f'*args      = {args}')
    print(f'**kwargs   = {kwargs}')
  show_parameters(*args, **kwargs)
  xs = list(args) + list(kwargs.values())
  def decorator(f):
    "take the class wrap as a decorator"
    predicate = lambda x: x == x >> 1 << 1
    @functools.wraps(f)
    def wrap(*args, **kwargs):
      "only accept even numbers to generate a new list"
      show_parameters(*args, **kwargs)
      show_metadata(f)
      nonlocal xs
      xs += f(*args, **kwargs)
      return list(filter(predicate, xs)) 
    return wrap
  return decorator

@log()
@even_list(-6, -5, -4, x = -3, y = -2, z = -1)
def make_list(*args, **kwargs):
  "utilize the function parameters to generate a new list"
  print('[even_list closure] {}'.format(even_list(*args, **kwargs)(make_list).__closure__))
  show_metadata(make_list)
  return list(args) + list(kwargs.values())

def main():
  "execute the test case"
  print(f'even_list(make_list) = {make_list(1, 2, 3, x = 4, y = 5, z = 6)}')

if __name__ == '__main__':
  main()

import random

def get_pair(threshold, upper, best_value, alpha, beta) -> (int, int):
  for target in range(upper):
    if (((alpha := best_value << 2) if (threshold == target) else (beta := best_value >> 1) >= beta)): break
  return (alpha, beta)

def show_pair(*pair: (int, int)):
  print(("(alpha, beta) = ({0}, {1})").format(str(pair[0]), str(pair[1])))

if __name__ == '__main__':
  alpha = random.randint(1, 2 << 1)
  beta  = random.randint(alpha << 1, alpha << 2)
  show_pair(alpha, beta)
  show_pair(*get_pair(random.randint(1, 10), 16, random.randint(2, 8), alpha, beta))

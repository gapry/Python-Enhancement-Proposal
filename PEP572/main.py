import random

def get_pair(threshold, upper, best_value, alpha, beta) -> (int, int):
  for target in range(upper):
    if (((alpha := best_value << 2) if (threshold == target) else (beta := best_value >> 1) >= beta)): break
  return (alpha, beta)

def show_pair(alpha, beta):
  print("alpha = %d" % alpha)
  print("beta  = %d" % beta)
  

if __name__ == '__main__':
  alpha = random.randint(1, 2 << 1)
  beta  = random.randint(alpha << 1, alpha << 2)
  show_pair(alpha, beta)
  alpha, beta = get_pair(random.randint(1, 10), 16, random.randint(2, 8), alpha, beta)
  show_pair(alpha, beta)

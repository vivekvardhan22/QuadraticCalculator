import math

def quadratic(a, b, c):
  """
  Calculates the roots of the quadratic equation ax^2 + bx + c = 0.

  Args:
    a: The coefficient of the x^2 term.
    b: The coefficient of the x term.
    c: The constant term.

  Returns:
    A list of the two roots of the equation.
  """

  if a == 0:
    if b == 0:
      return []
    else:
      return [-c / b]
  else:
    delta = b**2 - 4 * a * c
    if delta < 0:
      return []
    elif delta == 0:
      return [-b / (2 * a)]
    else:
      root1 = (-b + math.sqrt(delta)) / (2 * a)
      root2 = (-b - math.sqrt(delta)) / (2 * a)
      return [root1, root2]

if __name__ == "__main__":
  a = int(input("Enter the coefficient of the x^2 term: "))
  b = int(input("Enter the coefficient of the x term: "))
  c = int(input("Enter the constant term: "))
  roots = quadratic(a, b, c)
  print("The roots of the quadratic equation are:", roots)

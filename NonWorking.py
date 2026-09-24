import sys
import math
import random
import functools

#---Algebra---
def solve_linear():
    print("\nSolve a linear equation (ax + b = c)")
    try:
        a = get_float("a: ")
        b = get_float("b: ")
        c = get_float("c: ")
        
def solve_quadratic():
#---Calculus 1---
def derivative():
def derivative_numeric():
def estimate_limit():
def integral_exact():
def integral_trapezoid():

#---input helper---

def get_float(prompt):
    while True:
        try:
            print(prompt, end="", flush=True)
            sys.stdout.flush()
            return float(input())
        except ValueError:
            print(" >> Invalid input. Please type a number (e.g. 3, 3.5, -2). ")
        except EOFError:
            print("\n >> No input received. Exiting program.")
            raise SystemExit


def Main():
    print("ALGEBRA & CALCULUS")
    print("FIND THE VALUE OF (X) = FORMULA: f(x)=ax^2+bx+c) ")

    while True:
    print("\n1. Solve a linear equation (ax + b = c)")
    print("\n2. Solve a quadratic equation (ax^2 + bx + c = 0)")
    print("\n3. Evaluate f(x) = ax^2 + bx + c")
    print("\n4. Find the derivative f'(x) at a point")
    print("\n5. Estimate a limit as a x approaches a value")
    print("\n6. Compute a definite integral of f(x)")
    print("\n7. Quit")

    choice = input("Choose an option: ").strip()

if choice =="1":
    a,b,c = get_float("a: "), get_float("b: "), get_float("c: ")
    print(solve_linear(a,b,c))

elif choice == "2":
    a,b,c = get_float("a: "), get_float("b: "), get_float("c: ")
    print(solve_quadratic(a,b,c))

elif choice == "3":
    a,b,c = get_float("a: "), get_float("b: "), get_float("c: ") 
    x = get_float("x: ")
    print(f"f({x}) = {f(a,b,c)}")

elif choice == "4":
    a,b,c = get_float("a: "), get_float("b: "), get_float("c: ") 
    x = get_float("x: ")
    exact = derivative_exact(a, b, x)
    numeric = derivative_numeric(a, b, c, x)
    print(f"Exact f'({x}) ={exact} ")
    print(f" Numeric f'({x}) = {numeric:.6f} (via central difference)")

elif choice == "5":
    a,b,c = get_float("a: "), get_float("b: "), get_float("c: ") 
    x0 = get_float("x0(the value of x approaches): ")
    print(estimate_limit(a,b,c,x0))

elif choice == "6":
    a,b,c = get_float("a: "), get_float("b: "), get_float("c: ") 
    x1 = get_float("Lower bound x1: ")
    x2 = get_float("Lower bound x2: ")
    exact = integral_exact(a, b, c, x1, x2)
    numeric = integral_trapezoid(a, b, c, x1, x2)
    print(f"Exact integral = {exact:. 6f}")
    print(f"Numeric integral ={numeric:.6f}(via trapezoidal rule, n= 1000)")

elif choice == "7":
    print("Goodbye!!")
    break
else:
    print("Invalid choice: Please choose 1-7")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Goodbye!")
    except SystemExit:
        pass

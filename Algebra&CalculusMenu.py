import sys
import math

#---Algebra---

def solve_linear(a, b, c):
    """Solves ax + b = c -> ax = c - b -> x = (c - b) / a"""
    if a == 0:
        if b == c:
            return "Infinite solutions."
        else:
            return "No solution."
    x = (c - b) / a
    return f"x = {x}"

def solve_quadratic(a, b, c):
    """Solves ax^2 + bx + c = 0"""
    if a == 0:
        return f"Linear case: {solve_linear(b, c, 0)}"
    
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Two real roots: x1 = {root1}, x2 = {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"One real double root: x = {root}"
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-discriminant) / (2 * a)
        return f"Two complex roots: x1 = {real_part} + {imag_part}i, x2 = {real_part} - {imag_part}i"

def evaluate_f(a, b, c, x):
    """Evaluates f(x) = ax^2 + bx + c"""
    return a * (x**2) + b * x + c

#---Calculus 1---

def derivative_exact(a, b, x):
    """Exact derivative of f(x) = ax^2 + bx + c is f'(x) = 2ax + b"""
    return 2 * a * x + b

def derivative_numeric(a, b, c, x, h=1e-5):
    """Approximates f'(x) using the central difference formula"""
    f_plus = evaluate_f(a, b, c, x + h)
    f_minus = evaluate_f(a, b, c, x - h)
    return (f_plus - f_minus) / (2 * h)

def estimate_limit(a, b, c, x0, h=1e-5):
    """Estimates limit as x approaches x0 from both sides"""
    left_limit = evaluate_f(a, b, c, x0 - h)
    right_limit = evaluate_f(a, b, c, x0 + h)
    avg_limit = (left_limit + right_limit) / 2
    return f"Estimated limit as x -> {x0} is {avg_limit:.6f}"

def integral_exact(a, b, c, x1, x2):
    """Exact definite integral of ax^2 + bx + c from x1 to x2 using antiderivative F(x) = (a/3)x^3 + (b/2)x^2 + cx"""
    def F(x):
        return (a / 3) * (x**3) + (b / 2) * (x**2) + c * x
    return F(x2) - F(x1)

def integral_trapezoid(a, b, c, x1, x2, n=1000):
    """Approximates the definite integral using the Trapezoidal Rule"""
    h = (x2 - x1) / n
    total_sum = 0.5 * (evaluate_f(a, b, c, x1) + evaluate_f(a, b, c, x2))
    
    for i in range(1, n):
        x = x1 + i * h
        total_sum += evaluate_f(a, b, c, x)
        
    return total_sum * h

#---Input Helper---

def get_float(prompt):
    while True:
        try:
            print(prompt, end="", flush=True)
            sys.stdout.flush()
            user_input = input()
            return float(user_input)
        except ValueError:
            print(" >> Invalid input. Please type a number (e.g. 3, 3.5, -2). ")
        except EOFError:
            print("\n >> No input received. Exiting program.")
            raise SystemExit

#---Main Application Routine---

def main():
    print("ALGEBRA & CALCULUS TOOL")
    print("Base Formula: f(x) = ax^2 + bx + c")

    while True:
        print("\n1. Solve a linear equation (ax + b = c)")
        print("2. Solve a quadratic equation (ax^2 + bx + c = 0)")
        print("3. Evaluate f(x) = ax^2 + bx + c")
        print("4. Find the derivative f'(x) at a point")
        print("5. Estimate a limit as x approaches a value")
        print("6. Compute a definite integral of f(x)")
        print("7. Quit")

        choice = input("\nChoose an option (1-7): ").strip()

        if choice == "1":
            a = get_float("a: ")
            b = get_float("b: ")
            c = get_float("c: ")
            print(solve_linear(a, b, c))

        elif choice == "2":
            a = get_float("a: ")
            b = get_float("b: ")
            c = get_float("c: ")
            print(solve_quadratic(a, b, c))

        elif choice == "3":
            a = get_float("a: ")
            b = get_float("b: ")
            c = get_float("c: ") 
            x = get_float("x: ")
            res = evaluate_f(a, b, c, x)
            print(f"f({x}) = {res}")

        elif choice == "4":
            a = get_float("a: ")
            b = get_float("b: ")
            c = get_float("c: ") 
            x = get_float("x: ")
            exact = derivative_exact(a, b, x)
            numeric = derivative_numeric(a, b, c, x)
            print(f"Exact f'({x}) = {exact}")
            print(f"Numeric f'({x}) = {numeric:.6f} (via central difference)")

        elif choice == "5":
            a = get_float("a: ")
            b = get_float("b: ")
            c = get_float("c: ") 
            x0 = get_float("x0 (the value x approaches): ")
            print(estimate_limit(a, b, c, x0))

        elif choice == "6":
            a = get_float("a: ")
            b = get_float("b: ")
            c = get_float("c: ") 
            x1 = get_float("Lower bound x1: ")
            x2 = get_float("Upper bound x2: ")
            exact = integral_exact(a, b, c, x1, x2)
            numeric = integral_trapezoid(a, b, c, x1, x2)
            print(f"Exact integral = {exact:.6f}")
            print(f"Numeric integral = {numeric:.6f} (via trapezoidal rule, n=1000)")

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

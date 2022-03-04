# Solution for the problem "Euler's Method"
import sys

# y'(x) = x^2 - 6y^2, y(5) = 2

def f(xx,yy):
    return (xx ** 2) - 6 * (yy ** 2)

def main():
    res = [] # Result
    
    linecount = 0
    num_input = 0
    
    # stdin loop
    for line in sys.stdin:
        if linecount == 0 and num_input == 0:
            # Number of inputs in the first line
            num_input = int(line)
            if num_input == 0:
                break # If zero input - end program
        elif line == "":
            break
        else:
            i1, i2 = line.strip().split(" ") # Final. X
            stepSize = float(i1)
            dx = float(i2)
            x = 5.0 # Init. x
            y = 2.0 # Init. y

            if dx < x and stepSize > 0:
                stepSize *= -1

            while abs(dx - x) > 0:
                if abs(stepSize) > abs(dx - x):
                    stepSize = dx - x
                new_x = x + stepSize
                new_y = y + f(x, y) * (new_x - x)
                y = new_y
                x = new_x
                

            res.append(round(float(y),1))
            linecount += 1
        if linecount >= num_input:
            break

    for r in res:
        print("{:.1f}".format(r))

main()
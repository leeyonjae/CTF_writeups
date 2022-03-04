# Solution for the Problem "Jet's Pizza"
import sys

def main():
    price = []

    for topping in sys.stdin:
        if topping == "":
            break
        else:
            p = 15
            if "T" in topping:
                p += 1.5
            if "O" in topping:
                p += 1.25
            if "P" in topping:
                p += 3.5
            if "M" in topping:
                p += 3.75
            if "A" in topping:
                p += 0.4
            
            if p > 20:
                p *= 0.95
            
            price.append(p)
    
    for pr in price:
        print("{:.2f}".format(pr))


main()
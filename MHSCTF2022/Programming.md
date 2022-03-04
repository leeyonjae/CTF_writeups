# Programming

This category was more of a programming practice than capturing the flag.

## Hello CTF (5 pts)

> Submit a program using Python 3.8 that will output the following:
>
> flag{Hello_mhsCTF2022}

It's clearly a warmup.

**Solution:**

```python
def main():
    print("flag{Hello_mhsCTF2022}")

main()
```

## Jet's Pizza (20 pts)

> Jet's Pizza is opening up for business and they're tring to figure out an easy way to calculate the price of a pizza.
>
> Pizzas can have any combination of the following toppings (at least one topping is required per pizza): tomatoes (+$1.50), onions (+$1.25), pineapple (+$3.50), mushrooms (+$3.75), and avocado (+$0.40).
>  
> The base price of a pizza is $15 but if the total ends up being over $20, a 5% discount is applied (with the final price rounded to the nearest cent).
>
> Your job is to create a program (Python 3.8) that takes in a user's topping preference and return the pizza's price.

```text
Sample Input 1:
**TPM**
Sample Output 1:
**22.56**
Explanation 1:
The toppings of tomatoes (T), pineapple (P), and mushrooms (M) add $8.75 to the base price of $15. Because this is over $20, a 5% discount is applied.

Sample Input 2:
**AAAAAAAMMTGTMMMXMMT**
Sample Output 2:
**19.62**
Explanation 2:
Though some toppings are repeated and in a random order, they still only count once. Avocadoes, mushrooms, and tomatoes add $5.65 to the base price of $15. Because this is over $20, a 5% discount is applied. The characters that do not correspond to valid toppings (G and X) are ignored.
```

> Notes:
>
> - the seven inputs will be passed in (through stdin) separated by newlines; make sure your output (returned on stdout) is also separated by newlines
> - format your outputs as standard dollar amounts (rounded to the nearest cent with trailing zeroes as necessary) without the dollar sign
> - Every input will consist of at least one valid topping.

**Solution:**

```python
import sys

def main():
    price = []

    for topping in sys.stdin:
        if topping == "": # Empty line means end of input
            break
        else:
            p = 15
            if "T" in topping: # Tomato ... $1.50
                p += 1.5
            if "O" in topping: # Onion ... $1.25
                p += 1.25
            if "P" in topping: # Pineapple ... $3.50
                p += 3.5
            if "M" in topping: # Mushrooms ... $3.75
                p += 3.75
            if "A" in topping: # Avocado ... $0.40
                p += 0.4
            
            if p > 20: # 5% DC for order over $20
                p *= 0.95
            
            price.append(p)
    
    for pr in price:
        print("{:.2f}".format(pr))


main()
```

## Euler's Method (35 pts)

> Naturally, your favorite class of the day is AP Calculus BC and you've recently been learning Euler's Method. Your teacher has had a lot on their plate, so they've just been using the same curve for your homework problems every day, y'(x) = x^2 - 6y^2, y(5) = 2. To simplify matters, you're going to write a program to automate this trivial task for you.
>
> For each input, you will receive a space-separated set of two numbers (each between -10 and 10). The first is your step size and the second is the x-value of the point you need the estimated y-value for (to the nearest tenth and incuding trailing zero if necessary). Your output will be between -1,000 and 1,000.

```text
Sample Input 1:
0.8 5.8
Sample Output 1:
2.8

Sample Input 2:
0.9 7.7
Sample Output 2:
-645.1
```

> Notes:
>
> - the inputs will be passed in (through stdin) separated by newlines; make sure your output is also separated by newlines
> - the first line of input will contain only one integer representing the number of additional lines of input you will receive

**Solution:**

```python
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
```

## Cloudy w/ a Chance of Rain (45 pts)

> To help out your local meteorologist, you decide to write a sophisticated program that can determine the chance of rain for any given six hours. Hint: think about or's and and's in probability!
>
> For each input, you will receive a space-separated array of integers (each between 0 and 100) that represent the percent chance of rain for each hour in a six hour period. Your program should return the percent chance (rounded down to the nearest integer) that it rains during any of those six hours.

```text
Sample Input 1:
5 93 83 28 100 8
Sample Output 1:
100

Sample Input 2:
26 13 4 16 28 30
Sample Output 2:
73
```

> Notes:
>
>
> - the inputs will be passed in (through stdin) separated by newlines; make sure your output (returned on stdout) is also separated by newlines
> - the first line of input will contain only one integer representing the number of additional lines of input you will receive

**Solution:**

```python
import sys

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
            table = line.strip().split(" ") # Six Hr Table input
            precipitation = 100.0
            noprecipitation = 1.0
            for h in table:
                hp = 1.0 - (0.01 * int(h))
                noprecipitation *= hp
            
            precipitation -= 100 * noprecipitation

            res.append(int(precipitation))
            linecount += 1
        if linecount >= num_input:
            break

    for r in res:
        print("{:d}".format(r))

main()
```

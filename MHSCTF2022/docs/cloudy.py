# Solution for the problem "Cloudy w/ a Chance of Rain"
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
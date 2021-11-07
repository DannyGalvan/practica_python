import math

def run():
    # dictionary = {}

    # for i in range (1,101):
    #     if i % 3 != 0:
    #         dictionary[i] = i**3
    # print(dictionary)        

    # dictionary = {keys:keys**3 for keys in range(1,101) if keys % 3 != 0}


    dictionary = {round(math.sqrt(i),2): i for i in range (1,1000) if key % 2 == 0}
    print(dictionary)

if __name__ == "__main__":
    run()
def run():
    # list = []
    # for i in range (1,101):
    #     if i % 3 != 0:
    #         list.append(i*i)
    # print(list)    

    list = [i for i in range(1,100000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(list)

if __name__ == "__main__":
    run()
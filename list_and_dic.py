def run():
    my_list = [1, "hello", True, 4.5]
    my_dic = {"Firstname" : "Daniel", "Lastname" : "Galvan"}

    super_list = [ 
        {"Firstname" : "Daniel", "Lastname" : "Galvan"},
        {"Firstname" : "Hector", "Lastname" : "Whilhelm"},
        {"Firstname" : "Odelfa", "Lastname" : "Morales"},
        {"Firstname" : "Alexander", "Lastname" : "Lopez"},
        {"Firstname" : "Andrea", "Lastname" : "Cardona"},
    ]

    super_dic = {
        "natural_nums" : [1,2,3,4,5],
        "integer_nums" : [-1,-2,0,1,2],
        "float_nums" : [1.1,4.5,6.43]
    }

    for key, value  in super_dic.items():
        print(key, " ", value)

    for object in super_list:
        for key, values in object.items():
            print(key, " ", values)

    for i in super_list: 
        print(i["Firstname"], " ", i["Lastname"])   


if __name__ == "__main__":
    run()
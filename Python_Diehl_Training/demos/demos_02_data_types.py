from copy import copy


def demo02dataTypes():  # camel case structure of def name
    #TODO: this is place where I should do something



    # NUMBERS
    a = 12
    print(a,type(a),id(a),sep="--->")
    b = 12.5
    print(b,type(b),id(b),sep="--->")

    c = float(a)
    print(c,type(c),id(c),sep="--->")

    d = c
    print(d,type(d),id(d),sep="--->")
    d = copy(a)
    print(d,type(d),id(d),sep="--->")

    d=14
    print(a)
    print(d)

    # STRING

    fname = "Dariusz"

    # BOOLEAN
    rich = True

    # NONE
    nothing = None

    # COLLECTION TYPES
    names = [1,2,3,4,5,6] #list
    tnames = tuple(names) #tuple, krotkas
    ourSet = set(names) #dynamicset
    ourStaticSet = frozenset(ourSet) #staticset

    # MAPPING TYPE - dict
    pers = {
        'fname': "Jacek",
        "age": 18,
        "rich": True
    }

    print("For dict:")
    try:
        for i in pers.keys():
            print(pers.get(i))
            print(pers['i'])
    except KeyError as ex:
        print(ex)









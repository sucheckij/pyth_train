def demo_start():
    """
    Document of method
    :return: None
    """
    fname = 'Jacek' #line comment
    lname = "Such"
    address = '''
    ul. Cwiartki 3/4
    '''
    path = r'../files\date.txt'

    print(fname,lname,sep=",",end=" end of text \n") # add sep between variables


    names = ['Micha','Erwin', "Jacek"]
    print(*names, sep = ",")
    [print(n,end=",") for n in names]
    print('-*-'*5, "-*-"*3, sep = " ")

    with open("files/date.txt", 'a', encoding='utf-8') as f:
        print(*names, sep=";", file =f )

    print()

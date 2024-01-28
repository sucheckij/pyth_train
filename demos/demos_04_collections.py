from time import time
from lib.utils.matma_utils import *
def demo04Collections():
    names = ["michal", "milosz", "filip", "erwin"]
    print(*names)
    names.sort()
    print(*names)
    names.sort(reverse=True)
    names.append("Maciej")
    otherNames = ["Mateusz", "Baltazar"]
    names.extend(otherNames)
    print(*names)

    names.append("Maciej")
    print(names.count("Maciej"))

    if "Maciej" in names:
        print("jest")
    else:
        print("nie ma")

    names.pop(1) # usuwanie po indeksie


    numbers = [2,4,5,6,7,89,88,92]

    double_num = list(map(double_number,numbers))
    print(double_num)

    parzyste = list(filter(isEven,numbers))
    print(parzyste)

    names.clear() # czysci liste do pustej
    del names     # kasuje liste calkowicie

    projekty = ["Brexit", "Mexico Border", "Nord-Stream", "Polski Lad"]
    liderzy = ["Threresa May", "Bill Clinton", "Wlodek Putin", "Sasin"]

    for i, (p,l) in enumerate(zip(projekty, liderzy), start =1):
        print(f"{i}  -> liderem projektu {p} jest {l}")


    par = {
        "fname" : "Jacek",
        "lname" : "Such",
        "certificates" : "langolian"}

    par['certificates'] = 45
    print(par)

    del par["certificates"]
    print(par)

    # kompilacja
    n = 123
    kod_eval = "100*200*300*n"
    kod_exec = """
l = 34
l += 123
l += n
    """

    start = time()
    for i in range(1000000):
        eval(kod_eval)
        exec(kod_exec)
    print(f"Czas bez kompilacji: {time() - start: .2f}")

    start = time()
    kod_eval_komp = compile(kod_eval,"komentarz docs", "eval")
    kod_exec_komp = compile(kod_exec,"komentarz docs", "exec")
    for i in range(1000000):
        eval(kod_eval_komp)
        exec(kod_exec_komp)
    print(f"Czas bez kompilacji: {time() - start: .2f}")



import os, platform, logging, re

def demo06Modules():
    path = r"archive"
    if not os.path.exists(path):
        os.mkdir(path)


    if os.path.exists(r"files\date.txt"):
        os.remove(r"files\date.txt")

    print(f"Root folder: {os.getcwd()}")

    print(platform.python_version())
    print(platform.system())

    if platform.system() == "Windows":
        plik_os = os.path.join(os.getenv("HOMEDRIVE"),os.getenv("HOMEPATH"), 'plik_log.log')
    else:
        plik_os = os.path.join(os.getenv("HOME"),'plik_log.log')

    print('zapis do logu')
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s : %(levelname)s : %(message)s",
                        filename=plik_os, filemode='w')

    logging.debug('aplikacja startuje')
    logging.info('aplikacja działa')
    logging.warning('aplikacja tryb ostrzeżenia dziąłania')
    logging.error('aplikacja wywołała error')


    text = """w tym tekscie
    znajduje sie kod pin 1234
    który jest mi potrzebny żeby w Rudzie Śląskiej
    wyciągnąć kase z bankomatu
    """

    patt = r"\d\d\d\d"

    if re.search(patt,text):
        print(re.search(patt,text).group())












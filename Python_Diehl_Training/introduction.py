from sys import exit as sexit
import sys
from demos.demos_01_print import demo_start
from demos.demos_02_data_types import demo02dataTypes
from demos.demos_03_strings import *
from demos.demos_04_collections import *
from demos.demos_05_cust_methods import *
from lib.utils.validator import isNumber
from demos.demos_06_modules import *
from demos.demos_07_files import *
from demos.demos_08_www import *
from demos.demos_09_oop import *


def demo_print():
    ...


if __name__ == "__main__":

    while True:
        print("Menu:")
        print("1 - demo print")
        print("2 - demo data types:")
        print("3 - demo string")
        print("4 - demo collections")
        print("5 - custom methods")
        print("6 - fibonacci")
        print("7 - modules")
        print("8 - files operations")
        print("9 - www handler")
        print("9 - www handler")
        print("9 - www handler")
        print("12 - Object Oriented Programing")

        choice = input("Choose an option: ")

        if choice == '1':
            print(demo_start.__doc__)
            demo_start()
        if choice == '2':
            demo02dataTypes()
        if choice == '3':
            demo03Strings()
            countingPython()
        if choice == '4':
            demo04Collections()
        if choice == '5':
            demos05CustomMethods()
            print("Check the number:",isNumber('22'))
        if choice == "6":
            sumLikeExcel(sumLikeExcel(1,2.3,"5,4"))
            for i in range(38):
                print(f"Fibonacci for {i} is {fib(i)}")
        if choice == "7":
            demo06Modules()
        if choice == "8":
            demo_pliki()
        if choice == "9":
            demo_web_api_nbp(nbp_flag=True)
        if choice == "10":
            demo_www_scrapping_coronavirus()
        if choice == '11':
            www_search_titles()
        if choice == "12":
            demo_oop()
        else:
            break


from lib.classes.car import Car

my_car = Car()
while True:
    action = input("Co robimy?\n[A]ccelerate\n[B]rake\n"
                   "show [O]dometer\naverage [S]peed\n"
                   "[E]end\n").upper()
    if action not in "ABOSE" or len(action) != 1:
        print("Serio?")
        continue
    if action == 'A':
        my_car.accelerate()
        print("Accelerating...")
    elif action == 'B':
        my_car.brake()
        print("Braking...")
    elif action == 'O':
        print("The car has driven {} kilometers".format(my_car.odometer))
    elif action == 'S':
        print("The car's average speed was {} km/h".format(my_car.average_speed()))
    elif action == "E":
        break
    my_car.step()
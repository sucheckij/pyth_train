import pytest

from lib.classes.car import Car

speed_values = {45 ,50,55,100}


def test_brake_when_pass():
    # Arrange
    c = Car(50)
    #Execution
    c.brake()
    #Assert
    assert c.speed == 45


def test_brake_when_fail():
    with pytest.raises(Exception):
        # Arrange
        c = Car(50)
        #Execution
        c.brake()
        #Assert
        assert c.speed != 45

@pytest.mark.parametrize('speed_brake', speed_values)
def test_brake_with_parameters(speed_brake):
    with pytest.raises(Exception):
        # Arrange
        c = Car(speed_brake)
        #Execution
        c.brake()
        #Assert
        assert c.speed != 45
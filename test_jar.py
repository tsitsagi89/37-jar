from jar import Jar

def test_initialization():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

def test_deposit():
    jar = Jar(10)
    jar.deposit(3)
    assert jar.size == 3

    jar.deposit(5)
    assert jar.size == 8

    # Testing exceeding capacity
    try:
        jar.deposit(5)
    except ValueError:
        assert jar.size == 8
    else:
        assert False, "Expected ValueError when depositing more cookies than capacity"

def test_withdraw():
    jar = Jar(10)
    jar.deposit(7)
    jar.withdraw(2)
    assert jar.size == 5

    # Testing withdrawing more than available cookies
    try:
        jar.withdraw(10)
    except ValueError:
        assert jar.size == 5
    else:
        assert False, "Expected ValueError when withdrawing more cookies than available"

def test_str():
    jar = Jar(5)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

    jar.withdraw(1)
    assert str(jar) == "🍪🍪"

def test_invalid_capacity():
    try:
        jar = Jar(-5)
    except ValueError:
        assert True
    else:
        assert False, "Expected ValueError when initializing with negative capacity"

    try:
        jar = Jar(3.14)
    except ValueError:
        assert True
    else:
        assert False, "Expected ValueError when initializing with non-integer capacity"

def test_invalid_deposit_withdraw():
    jar = Jar(5)
    try:
        jar.deposit(-2)
    except ValueError:
        assert True
    else:
        assert False, "Expected ValueError when depositing negative number of cookies"

    try:
        jar.withdraw(2.5)
    except ValueError:
        assert True
    else:
        assert False, "Expected ValueError when withdrawing non-integer number of cookies"

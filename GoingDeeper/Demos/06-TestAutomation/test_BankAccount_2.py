import pytest
from bankAccount import BankAccount

acc = None

@pytest.fixture(autouse=True)
def run_around_tests():

    # Code that will run before each test.
    print("Do something before a test")
    global acc
    acc = BankAccount("David")

    # A test function will be run at this point
    yield

    # Code that will run after each test.
    print("Do something after a test")


def test_accountCreated_zeroBalanceInitially():
    assert acc.balance == 0


def test_deposit_singleDeposit_correctBalance():
    acc.deposit(100)
    assert acc.balance == 100


def test_deposit_multipleDeposits_cumulativeBalance():
    acc.deposit(100)
    acc.deposit(200)
    acc.deposit(300)
    assert acc.balance == 600


def test_deposit_withdrawalsWithinLimits_balanceReduced():
    acc.deposit(600)
    acc.withdraw(100)
    acc.withdraw(200)
    assert acc.balance == 300


def test_deposit_withdrawalsUptoLimit_balanceZero():
    acc.deposit(600)
    acc.withdraw(100)
    acc.withdraw(200)
    acc.withdraw(300)
    assert acc.balance == 0


def test_deposit_withdrawalsExceedLimits_exceptionOccursV1():
    acc.deposit(600)
    with pytest.raises(Exception):
        acc.withdraw(601)


def test_deposit_withdrawalsExceedLimits_exceptionOccursV2():
    acc.deposit(600)
    with pytest.raises(Exception) as excinfo:
        acc.withdraw(601)
    assert excinfo.typename == "Exception"
    assert excinfo.value.args[0] == "Insufficient funds"


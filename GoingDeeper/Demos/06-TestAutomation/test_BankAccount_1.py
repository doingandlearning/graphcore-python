import pytest
from bankAccount import BankAccount


def test_accountCreated_zeroBalanceInitially():
    acc = BankAccount("David")
    assert acc.balance == 0


def test_deposit_singleDeposit_correctBalance():

    # Arrange.
    acc = BankAccount("David")

    # Act.
    acc.deposit(100)

    # Assert.
    assert acc.balance == 100


def test_deposit_multipleDeposits_cumulativeBalance():

    # Arrange.
    acc = BankAccount("David")

    # Act.
    acc.deposit(100)
    acc.deposit(200)
    acc.deposit(300)

    # Assert.
    assert acc.balance == 600


def test_deposit_withdrawalsWithinLimits_balanceReduced():

    # Arrange.
    acc = BankAccount("David")

    # Act.
    acc.deposit(600)
    acc.withdraw(100)
    acc.withdraw(200)

    # Assert.
    assert acc.balance == 300


def test_deposit_withdrawalsUptoLimit_balanceZero():

    # Arrange.
    acc = BankAccount("David")

    # Act.
    acc.deposit(600)
    acc.withdraw(100)
    acc.withdraw(200)
    acc.withdraw(300)

    # Assert.
    assert acc.balance == 0


def test_deposit_withdrawalsExceedLimits_exceptionOccursV1():

    # Arrange.
    acc = BankAccount("David")

    # Act.
    acc.deposit(600)

    # Verify expected exception occurs
    with pytest.raises(Exception):
        acc.withdraw(601)


def test_deposit_withdrawalsExceedLimits_exceptionOccursV2():

    # Arrange.
    acc = BankAccount("David")

    # Act.
    acc.deposit(600)

    # Verify expected exception occurs
    with pytest.raises(Exception) as excinfo:
        acc.withdraw(601)

    # Assert the exception type and error message are correct
    assert excinfo.typename == "Exception"
    assert excinfo.value.args[0] == "Insufficient funds"


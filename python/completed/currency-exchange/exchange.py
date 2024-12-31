"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""



def exchange_money(budget, exchange_rate):
    """
    Calculate the amount of foreign currency you can receive.

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """
    Calculate the remaining amount of money after exchanging.

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of money you want to exchange.
    :return: float - remaining amount of money after exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """
    Calculate the total value of bills.

    :param denomination: int - the value of a single bill.
    :param number_of_bills: int - the number of bills you have.
    :return: int - total value of the bills.
    """
    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """
    Calculate the number of bills that can be obtained within the budget.

    :param budget: float - the amount of money you have.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills that can be obtained.
    """
    return int(budget // denomination)


def get_leftover_of_bills(budget, denomination):
    """
    Calculate the leftover amount that cannot be exchanged into bills.

    :param budget: float - the amount of money you have.
    :param denomination: int - the value of a single bill.
    :return: float - leftover amount that cannot be exchanged into bills.
    """
    return budget % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate the maximum value of foreign currency you can receive within the budget.

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    effective_rate = exchange_rate * (1 + spread / 100)
    exchanged_money = budget / effective_rate
    return int(exchanged_money // denomination) * denomination

"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_emitted: int or float - number of neutrons emitted per second.
    :return: bool - is criticality balanced?

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800 K.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    return temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted) < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess reactor efficiency zone.

    :param voltage: int or float - voltage value.
    :param current: int or float - current value.
    :param theoretical_max_power: int or float - theoretical maximum power.
    :return: str - efficiency zone ('green', 'orange', 'red', or 'black').

    Efficiency can be grouped into 4 bands:
    1. green -> efficiency of 80% or more,
    2. orange -> efficiency of less than 80% but at least 60%,
    3. red -> efficiency below 60% but at least 30%,
    4. black -> efficiency less than 30%.
    """
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100

    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess and return reactor status code.

    :param temperature: int or float - temperature value in kelvin.
    :param neutrons_produced_per_second: int or float - number of neutrons produced per second.
    :param threshold: int or float - threshold value.
    :return: str - one of ('LOW', 'NORMAL', 'DANGER').

    1. 'LOW' -> `temperature * neutrons_produced_per_second` < 90% of `threshold`
    2. 'NORMAL' -> `temperature * neutrons_produced_per_second` +/- 10% of `threshold`
    3. 'DANGER' -> `temperature * neutrons_produced_per_second` is not in the above-stated ranges
    """
    product = temperature * neutrons_produced_per_second
    lower_bound = 0.9 * threshold
    upper_bound = 1.1 * threshold

    if product < lower_bound:
        return 'LOW'
    elif lower_bound <= product <= upper_bound:
        return 'NORMAL'
    else:
        return 'DANGER'
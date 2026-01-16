"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    # Check if all conditions for criticality are satisfied
    return (temperature < 800 and 
            neutrons_emitted > 500 and 
            temperature * neutrons_emitted < 500000)
   
    


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    
    return (
        'green' if efficiency >= 80 else
        'orange' if efficiency >= 60 else
        'red' if efficiency >= 30 else
        'black'
    )


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    product = temperature * neutrons_produced_per_second
    lower_bound, upper_bound = 0.9 * threshold, 1.1 * threshold
    print(temperature)
    if product < lower_bound:
        return 'LOW'
    elif lower_bound <= product <= upper_bound:
        return 'NORMAL'
    return 'DANGER'


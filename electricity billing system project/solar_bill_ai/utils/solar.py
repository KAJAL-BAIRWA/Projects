def calculate_solar(units, days):

    """
    Calculate solar recommendation
    """

    # Prevent divide by zero
    if days == 0:
        days = 30

    # Daily consumption
    daily_units = units / days

    # Solar size estimate
    system_size = daily_units / 4

    # Approx solar cost
    estimated_cost = system_size * 50000

    # Estimated yearly savings
    yearly_savings = units * 12 * 8

    # Payback calculation
    if yearly_savings == 0:
        payback = 0
    else:
        payback = estimated_cost / yearly_savings

    return {

        "system_size_kw": round(system_size, 2),

        "estimated_cost_rs": round(estimated_cost),

        "payback_years": round(payback, 1)
    }
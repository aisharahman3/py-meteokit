import math

__version__ = "0.2.0"

def saturation_vapor_pressure(temp_c):
    """Magnus-Tetens, result in hPa."""
    return 6.112 * math.exp(17.62 * temp_c / (243.12 + temp_c))

def actual_vapor_pressure(temp_c, rh):
    return rh / 100.0 * saturation_vapor_pressure(temp_c)

def dew_point(temp_c, rh):
    a, b = 17.62, 243.12
    gamma = math.log(rh / 100.0) + a * temp_c / (b + temp_c)
    return b * gamma / (a - gamma)

def heat_index(temp_f, rh):
    # Rothfusz regression (NWS)
    t, r = temp_f, rh
    return (-42.379 + 2.04901523 * t + 10.14333127 * r - 0.22475541 * t * r
            - 6.83783e-3 * t * t - 5.481717e-2 * r * r + 1.22874e-3 * t * t * r
            + 8.5282e-4 * t * r * r - 1.99e-6 * t * t * r * r)

def wind_chill(temp_c, wind_kmh):
    v = wind_kmh ** 0.16
    return 13.12 + 0.6215 * temp_c - 11.37 * v + 0.3965 * temp_c * v

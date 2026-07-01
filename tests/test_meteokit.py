from meteokit import dew_point, saturation_vapor_pressure
assert dew_point(25,100)>24.5
assert saturation_vapor_pressure(0)>6.0

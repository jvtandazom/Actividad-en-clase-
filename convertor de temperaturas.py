def conversion_temperatura(grad_cent):
    fahrenheit = (9/5) * grad_cent + 32
    kelvin = 273.15 + grad_cent
    return fahrenheit, kelvin

# Ejemplo de uso
grados_celsius = 25
fahrenheit_resultado, kelvin_resultado = conversion_temperatura(grados_celsius)
print(f"{grados_celsius} grados Celsius son {fahrenheit_resultado} grados Fahrenheit y {kelvin_resultado} grados Kelvin.")
import vwxlink as vw

# Crear un nuevo archivo de Vectorworks con el nombre 'ejemplo.vwx'
doc = vw.NewDocument()
doc.Open('ejemplo.vwx')

# Crear un rectángulo rojo de 100 x 50 unidades en la posición (0, 0)
rect = vw.CreateRectangle(0, 0, 100, 50)
rect.SetFill(1, 0, 0)  # Establecer el color de relleno a rojo

# Crear un círculo azul de radio 25 unidades en la posición (150, 50)
circle = vw.CreateCircle(150, 50, 25)
circle.SetFill(0, 0, 1)  # Establecer el color de relleno a azul

# Guardar el archivo de Vectorworks
doc.Save()

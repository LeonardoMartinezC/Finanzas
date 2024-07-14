import pandas as pd
from dataframe_image import export

# Crear un DataFrame de ejemplo
dt = {'column1': ["AA", "BBBB", "CCC", "DDDDD"],
      'column2': [143.40, 144.60, 153.40, 92.50],
      'column3': [144.21, 142.60, 155.65, 92.77]}
cuadro = pd.DataFrame(data=dt)

# Exportar el DataFrame como una imagen
export(cuadro, 'tabla.png')
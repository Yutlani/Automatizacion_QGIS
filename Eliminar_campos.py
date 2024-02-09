# Importar las bibliotecas necesarias
from qgis.core import QgsField, QgsVectorLayer

# Obtener la capa activa
layer = iface.activeLayer()

# Lista de nombres de campos a eliminar
campos_a_eliminar = ['nombre_capa']

# Iniciar la edición de la capa
layer.startEditing()

# Eliminar campos
for campo in campos_a_eliminar:
    if layer.fields().indexFromName(campo) != -1:
        layer.dataProvider().deleteAttributes([layer.fields().indexFromName(campo)])

# Finalizar la edición y guardar los cambios
layer.commitChanges()

# Actualizar los campos de la capa
layer.updateFields()

# Imprimir un mensaje cuando se complete
print('Proceso de eliminación de campos completado.')

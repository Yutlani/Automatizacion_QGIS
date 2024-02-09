# Importar las bibliotecas necesarias
from qgis.core import QgsField

# Obtener la capa por su nombre
nombre_capa = 'nombre_capa'
capa = QgsProject.instance().mapLayersByName(nombre_capa)[0]

# Asegurarse de que la capa existe y es del tipo correcto (línea o polígono)
if capa and (capa.geometryType() == QgsWkbTypes.LineGeometry or capa.geometryType() == QgsWkbTypes.PolygonGeometry):
    # Crear un nuevo campo para almacenar el perímetro
    field = QgsField('Perimetro', QVariant.Double)
    capa.dataProvider().addAttributes([field])
    capa.updateFields()

    # Calcular y almacenar el perímetro para cada entidad
    with edit(capa):
        for feature in capa.getFeatures():
            perimetro = feature.geometry().length()
            feature['Perimetro'] = perimetro
            capa.updateFeature(feature)

    # Imprimir un mensaje cuando se complete
    print(f'Proceso de cálculo de perímetro para la capa {nombre_capa} completado.')
else:
    print(f'La capa {nombre_capa} no existe o no es del tipo de geometría de línea o polígono.')

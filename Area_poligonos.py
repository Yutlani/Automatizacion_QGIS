# Importar las bibliotecas necesarias
from qgis.core import QgsField

# Obtener la capa por su nombre
nombre_capa = 'nombre_capa'
capa = QgsProject.instance().mapLayersByName(nombre_capa)[0]

# Asegurarse de que la capa existe y es del tipo correcto (polígono)
if capa and capa.geometryType() == QgsWkbTypes.PolygonGeometry:
    # Crear un nuevo campo para almacenar el área
    field = QgsField('Area_m2', QVariant.Double)
    capa.dataProvider().addAttributes([field])
    capa.updateFields()

    # Calcular y almacenar el área para cada polígono
    with edit(capa):
        for feature in capa.getFeatures():
            area = feature.geometry().area()
            feature['Area_m2'] = area
            capa.updateFeature(feature)

    # Imprimir un mensaje cuando se complete
    print(f'Proceso de cálculo de área para la capa {nombre_capa} completado.')
else:
    print(f'La capa {nombre_capa} no existe o no es del tipo de geometría de polígono.')

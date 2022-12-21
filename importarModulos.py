# TRES MANERAS DE IMPORTAR
from PRUEBAS_MODULOS.fichero import main #--> directamente main() ya funcionaría
from PRUEBAS_MODULOS.fichero import * #--> directamente cualquier función ya funcionaría
from PRUEBAS_MODULOS import fichero #--> fichero.main()
import PRUEBAS_MODULOS.fichero #--> PRUEBAS_MODULOS.fichero.main()


print("IMPORTACIÓN_1: ", end=' ')
main()
print("IMPORTACIÓN_2: ", end=' ')
test()
print("IMPORTACIÓN_3: ", end=' ')
fichero.test()
print("IMPORTACIÓN_4: ", end=' ')
PRUEBAS_MODULOS.fichero.test()

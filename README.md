# Funcionarios y habilitaciones

La Municipalidad de Córdoba libera víá webservice:
 - La lista de funcionarios
 - Listas de propietarios de servicios (taxis, remises, geriátricos, etc)

En ambos casos se incluyen identificadores únicos de las personas. Es por esto que puede conocerse si hay _funcionarios_ que poseen habilitaciones comerciales.  

Esto en general no es un problema pero en casos específicos podría representar conflictos de intereses. Por ejmplo si el responsable de la habilitación de Geriátricos es dueño de uno o más de estos es posible que deba prestarse especial atención al caso.  

Este repositorio busca conectar la lista de funcionarios y la de los prestatarios para encontrar conexiones.  

## Datos

Los datos usados son:
 - Web Service de funcionarios. [Link](https://gobiernoabierto.cordoba.gob.ar/api/funciones/)
 - Lista de Taxis Habilitados. [Link](https://gobiernoabierto.cordoba.gob.ar/api/v2/transporte-publico/taxis/)
 - Lista de Remises habilitados. [Link](https://gobiernoabierto.cordoba.gob.ar/api/v2/transporte-publico/remis/)
 - Lista de Geriátricos habilitados. [Link](https://gobiernoabierto.cordoba.gob.ar/api/v2/entes-privados/geriatricos/)
 - Lista de Jardines Maternales habilitados. [Link](https://gobiernoabierto.cordoba.gob.ar/api/v2/entes-privados/jardines/)
 - Lista de transportistas escolares habilitados. [Link](https://gobiernoabierto.cordoba.gob.ar/api/v2/transporte-publico/escolar/)


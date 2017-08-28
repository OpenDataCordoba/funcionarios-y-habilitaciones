"""
    Obtener datos de un webservice de la municipalidad de Córdoba
    https://gobiernoabierto.cordoba.gob.ar/api/
"""

import requests
from abc import ABC, abstractmethod
import os.path
import json


class ApiMuniCBAData(ABC):
    ''' obtener datos del API de la Municipalidad de Córdona '''

    def __init__(self):
        self.url = None
        self.datos = None
        self.ids = None
        self.data_folder = 'data'

    def get_data(self, url):
        """ obtener los datos específicos paginando y acumulando resultados"""
        data_type = self.url.split('/')[-2:-1][0]
        save_to = '{}/{}.json'.format(self.data_folder, data_type)
        
        if os.path.isfile(save_to):
            with open(save_to, 'r') as fp:
                res = json.load(fp)
                return res

        res = []  # resultados a devolver
        while url:
            r = requests.get(url=url)
            # print('Getting {} ({})'.format(url, len(res)))
            respuesta = r.json()
            resultados = respuesta["results"]
            for resultado in resultados:
                resultado["_UID"] = self.get_id_from_object(resultado)
                resultado["_NAME"] = self.get_nombre_from_object(resultado)
                res.append(resultado) 
            url = respuesta["next"]

        with open(save_to, 'w') as fp:
            json.dump(res, fp, sort_keys=True, indent=4)

        return res

    def load_data(self, force=False):
        if force or self.datos is None:
            self.datos = self.get_data(url=self.url)

    @abstractmethod
    def get_id_from_object(self):
        pass

    @abstractmethod
    def get_nombre_from_object(self):
        pass


class CbaFuncionarios(ApiMuniCBAData):
    ''' funcionarios obtenidos vía API '''
    def __init__(self):
        super().__init__()
        self.url = "https://gobiernoabierto.cordoba.gob.ar/api/funciones/"

    def get_id_from_object(self, obj):
        ''' obtener el ID único (DNI o CUIT) de cada objeto'''
        return obj["funcionario"]["uniqueid"].replace('DNI (AR) ', '')

    def get_nombre_from_object(self, obj):
        ''' obtener el ID único (DNI o CUIT) de cada objeto'''
        return '{} {}'.format(obj["funcionario"]["nombre"], obj["funcionario"]["apellido"])


class CbaTaxis(ApiMuniCBAData):
    ''' taxis obtenidos vía API '''
    def __init__(self):
        super().__init__()
        self.url = "https://gobiernoabierto.cordoba.gob.ar/api/v2/transporte-publico/taxis/"

    def get_id_from_object(self, obj):
        ''' obtener el ID único (DNI o CUIT) de cada objeto'''
        return obj["CUIT"].replace(',', '')

    def get_nombre_from_object(self, obj):
        ''' obtener el ID único (DNI o CUIT) de cada objeto'''
        return obj["titular"]

class CbaRemises(ApiMuniCBAData):
    ''' Remises obtenidos vía API '''
    def __init__(self):
        super().__init__()
        self.url = "https://gobiernoabierto.cordoba.gob.ar/api/v2/transporte-publico/remis/"

    def get_id_from_object(self, obj):
        ''' obtener el ID único (DNI o CUIT) de cada objeto'''
        return obj["CUIT"].replace(',', '')

    def get_nombre_from_object(self, obj):
        ''' obtener el ID único (DNI o CUIT) de cada objeto'''
        return obj["titular"]

class CbaGeriatricos(ApiMuniCBAData):
    ''' Geriatricos obtenidos vía API '''
    def __init__(self):
        super().__init__()
        self.url = "https://gobiernoabierto.cordoba.gob.ar/api/v2/entes-privados/geriatricos/"

    def get_id_from_object(self, obj):
        ''' obtener el ID único (DNI desde CUIT) de cada objeto'''
        # ejemplo: "CUIT": "30-07115107-5",
        p = obj["CUIT"].split('-')
        if len(p) != 3:
            print('CUIT MALFORMADO: {}'.format(obj["CUIT"]))
            res = obj["CUIT"]
        else:
            res = p[1]
        return res

    def get_nombre_from_object(self, obj):
        ''' obtener el ID único (DNI o CUIT) de cada objeto'''
        return obj["titular"]

class CbaJardines(ApiMuniCBAData):
    ''' Jardines obtenidos vía API '''
    def __init__(self):
        super().__init__()
        self.url = "https://gobiernoabierto.cordoba.gob.ar/api/v2/entes-privados/jardines/"

    def get_id_from_object(self, obj):
        ''' obtener el ID único (DNI desde CUIT) de cada objeto'''
        # ejemplo: "CUIT": "30-07115107-5",
        p = obj["CUIT"].split('-')
        if len(p) != 3:
            print('CUIT MALFORMADO: {}'.format(obj["CUIT"]))
            res = obj["CUIT"]
        else:
            res = p[1]
        return res

    def get_nombre_from_object(self, obj):
        ''' obtener el ID único (DNI o CUIT) de cada objeto'''
        return obj["titular"]


class CbaTransportesEscolares(ApiMuniCBAData):
    ''' Transportes escolares obtenidos vía API '''
    def __init__(self):
        super().__init__()
        self.url = "https://gobiernoabierto.cordoba.gob.ar/api/v2/transporte-publico/escolar/"

    def get_id_from_object(self, obj):
        ''' obtener el ID único (DNI desde CUIT) de cada objeto'''
        # ejemplo: "CUIT": "30-07115107-5",
        p = obj["CUIT"].split('-')
        if len(p) != 3:
            print('CUIT MALFORMADO: {}'.format(obj["CUIT"]))
            res = obj["CUIT"]
        else:
            res = p[1]
        return res

    def get_nombre_from_object(self, obj):
        ''' obtener el ID único (DNI o CUIT) de cada objeto'''
        return obj["titular"]
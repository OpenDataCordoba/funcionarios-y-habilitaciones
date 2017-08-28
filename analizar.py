import sys
from source.get_data import *


print('Obteniendo funcionarios ...')
funcionarios = CbaFuncionarios()
funcionarios.load_data()
print('Funcionarios encontrados: {}'.format(len(funcionarios.datos)))

print('Obteniendo taxis ...')
taxis = CbaTaxis()
taxis.load_data()
print('Taxis encontrados: {}'.format(len(taxis.datos)))

print('Obteniendo remises ...')
remises = CbaRemises()
remises.load_data()
print('Remises encontrados: {}'.format(len(remises.datos)))

print('Obteniendo Geriatricos ...')
geriatricos = CbaGeriatricos()
geriatricos.load_data()
print('Geriatricos encontrados: {}'.format(len(geriatricos.datos)))

print('Obteniendo Jardines ...')
jardines = CbaJardines()
jardines.load_data()
print('Jardines encontrados: {}'.format(len(jardines.datos)))

print('Obteniendo Transportes escolares ...')
transportes_escolares = CbaTransportesEscolares()
transportes_escolares.load_data()
print('Transportes escolares encontrados: {}'.format(len(transportes_escolares.datos)))

print('Buscar funcionarios con taxis ...')
for funcionario in funcionarios.datos:
    
    funcionarios_con_taxis = 0
    for taxi in taxis.datos:
    
        if funcionario['_UID'] == taxi['_UID']:
            funcionarios_con_taxis += 1
            print('ENCONTRADO!')
            print('FUNC: {}'.format(funcionario))
            print('TAXI: {}'.format(taxi))

    funcionarios_con_remises = 0
    for remis in remises.datos:
    
        if funcionario['_UID'] == remis['_UID']:
            funcionarios_con_remises += 1
            print('ENCONTRADO!')
            print('FUNC: {}'.format(funcionario))
            print('REMIS: {}'.format(remis))

    funcionarios_con_geriatricos = 0
    for geriatrico in geriatricos.datos:
    
        if funcionario['_UID'] == geriatrico['_UID']:
            funcionarios_con_geriatricos += 1
            print('ENCONTRADO!')
            print('FUNC: {}'.format(funcionario))
            print('GERIATRICO: {}'.format(geriatrico))

    funcionarios_con_jardines = 0
    for jardin in jardines.datos:
    
        if funcionario['_UID'] == jardin['_UID']:
            funcionarios_con_jardines += 1
            print('ENCONTRADO!')
            print('FUNC: {}'.format(funcionario))
            print('JARDIN: {}'.format(jardin))

    funcionarios_con_tranportes_escolares = 0
    for transporte_escolar in transportes_escolares.datos:
    
        if funcionario['_UID'] == transporte_escolar['_UID']:
            funcionarios_con_tranportes_escolares += 1
            print('ENCONTRADO!')
            print('FUNC: {}'.format(funcionario))
            print('GERIATRICO: {}'.format(transporte_escolar))


print('Funcionarios con Taxis: {}'.format(funcionarios_con_taxis))
print('Funcionarios con Remises: {}'.format(funcionarios_con_remises))
print('Funcionarios con Geriatricos: {}'.format(funcionarios_con_geriatricos))
print('Funcionarios con Jardines: {}'.format(funcionarios_con_jardines))
print('Funcionarios con Transportes escolares: {}'.format(funcionarios_con_tranportes_escolares))

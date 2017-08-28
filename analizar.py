import sys
import csv
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


# ---- ANALIZAR PROPIETARIOS (independientemente de que sean funcionarios)
# Buscar a los permisionarios de todos los servicios y acumular resultados

print('Analizando propietarios (no funcionarios)')
uids = {}

for obj in remises.datos:
    uid = obj['_UID']
    if uid not in uids.keys():
        uids[uid] = {'uid': uid, 'total': 0, 'remises': 0, 'geriatricos': 0, 'jardines maternales': 0, 'taxis': 0, 'transportes escolares': 0}

    uids[uid]['nombre'] = obj['_NAME']
    uids[uid]['total'] += 1
    uids[uid]['remises'] += 1

for obj in taxis.datos:
    uid = obj['_UID']
    if uid not in uids.keys():
        uids[uid] = {'uid': uid, 'total': 0, 'remises': 0, 'geriatricos': 0, 'jardines maternales': 0, 'taxis': 0, 'transportes escolares': 0}

    uids[uid]['nombre'] = obj['_NAME']
    uids[uid]['total'] += 1
    uids[uid]['taxis'] += 1
    
for obj in geriatricos.datos:
    uid = obj['_UID']
    if uid not in uids.keys():
        uids[uid] = {'uid': uid, 'total': 0, 'remises': 0, 'geriatricos': 0, 'jardines maternales': 0, 'taxis': 0, 'transportes escolares': 0}

    uids[uid]['nombre'] = obj['_NAME']
    uids[uid]['total'] += 1
    uids[uid]['geriatricos'] += 1

for obj in jardines.datos:
    uid = obj['_UID']
    if uid not in uids.keys():
        uids[uid] = {'uid': uid, 'total': 0, 'remises': 0, 'geriatricos': 0, 'jardines maternales': 0, 'taxis': 0, 'transportes escolares': 0}

    uids[uid]['nombre'] = obj['_NAME']
    uids[uid]['total'] += 1
    uids[uid]['jardines maternales'] += 1

for obj in transportes_escolares.datos:
    uid = obj['_UID']
    if uid not in uids.keys():
        uids[uid] = {'uid': uid, 'total': 0, 'remises': 0, 'geriatricos': 0, 'jardines maternales': 0, 'taxis': 0, 'transportes escolares': 0}

    uids[uid]['nombre'] = obj['_NAME']
    uids[uid]['total'] += 1
    uids[uid]['transportes escolares'] += 1

ordenados = sorted(uids.values(), key=lambda k: k['total'], reverse=True) 
top = 50

print('Grabando mayores propietarios')
with open('data/mayores-propietarios-no-funcionarios.csv', 'w') as csvfile:
    fieldnames = ['uid', 'nombre', 'total', 'remises', 'geriatricos', 'jardines maternales', 'taxis', 'transportes escolares']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for uid in ordenados[:top]:
        writer.writerow(uid)


print('Grabando mayores propietarios taxis')
taxis_ordenados = sorted(uids.values(), key=lambda k: k['taxis'], reverse=True) 
top = 10

with open('data/mayores-propietarios-de-taxis-no-funcionarios.csv', 'w') as csvfile:
    fieldnames = ['uid', 'nombre', 'total', 'remises', 'geriatricos', 'jardines maternales', 'taxis', 'transportes escolares']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for uid in taxis_ordenados[:top]:
        writer.writerow(uid)

print('Grabando mayores propietarios remises')
remises_ordenados = sorted(uids.values(), key=lambda k: k['remises'], reverse=True) 
top = 10

with open('data/mayores-propietarios-de-remises-no-funcionarios.csv', 'w') as csvfile:
    fieldnames = ['uid', 'nombre', 'total', 'remises', 'geriatricos', 'jardines maternales', 'taxis', 'transportes escolares']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for uid in remises_ordenados[:top]:
        writer.writerow(uid)

print('Grabando mayores propietarios jardines')
jardines_ordenados = sorted(uids.values(), key=lambda k: k['jardines maternales'], reverse=True) 
top = 10

with open('data/mayores-propietarios-de-jardines-no-funcionarios.csv', 'w') as csvfile:
    fieldnames = ['uid', 'nombre', 'total', 'remises', 'geriatricos', 'jardines maternales', 'taxis', 'transportes escolares']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for uid in jardines_ordenados[:top]:
        writer.writerow(uid)

print('Grabando mayores propietarios geriatricos')
geriatricos_ordenados = sorted(uids.values(), key=lambda k: k['geriatricos'], reverse=True) 
top = 10

with open('data/mayores-propietarios-de-geriatricos-no-funcionarios.csv', 'w') as csvfile:
    fieldnames = ['uid', 'nombre', 'total', 'remises', 'geriatricos', 'jardines maternales', 'taxis', 'transportes escolares']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for uid in geriatricos_ordenados[:top]:
        writer.writerow(uid)


transportes_ordenados = sorted(uids.values(), key=lambda k: k['transportes escolares'], reverse=True) 
top = 10

with open('data/mayores-propietarios-de-transportes-escolares-no-funcionarios.csv', 'w') as csvfile:
    fieldnames = ['uid', 'nombre', 'total', 'remises', 'geriatricos', 'jardines maternales', 'taxis', 'transportes escolares']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for uid in transportes_ordenados[:top]:
        writer.writerow(uid)

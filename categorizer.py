def busquedaVacuna(tweet):
    vacunas = ''
    if 'rusa' in tweet:
        vacunas = 'Rusa'
    if 'china' in tweet:
        if(vacunas == 'Rusa'):
            vacunas = 'Ambas'
        else:
            vacunas='China'
    return vacunas
def formata_tamanho(tamanho):
    base = 1024
    kilobyte = base
    megabyte = base ** 2
    gigabyte = base ** 3
    terabyte = base ** 4
    petabyte = base ** 5

    if tamanho < kilobyte:
        texto = 'B'
    elif tamanho < megabyte:
        tamanho /= kilobyte
        texto = 'K'
    elif tamanho < gigabyte:
        tamanho /= megabyte
        texto = 'M'
    elif tamanho < terabyte:
        tamanho /= gigabyte
        texto = 'G'
    elif tamanho < petabyte:
        tamanho /= terabyte
        texto = 'T'
    else:
        tamanho /= petabyte
        texto = 'P'

    tamanho = round(tamanho, 2)
    return f'{tamanho}{texto}'.replace('.', ',')

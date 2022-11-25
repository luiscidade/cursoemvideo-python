def dadosnotas(*notas, sit=False):

    d_notas = dict()

    d_notas["total"] = len(notas)
    d_notas["média"] = sum(notas) / len(notas)
    d_notas['maior'] = max(notas)
    d_notas['menor'] = min(notas)

    return d_notas


print(dadosnotas(1))
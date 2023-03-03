'''
Метод удаляет значения в списке с конца
'''


def cleaning_cache(cache):
    cache.rpop('ready_list')



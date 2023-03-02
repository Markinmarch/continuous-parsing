'''
Метод удаляет значения в списке с конца
'''


def cleaning_timer(cache):
    cache.rpop('ready_list')



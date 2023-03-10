'''
Модуль "comparision" содержит методы, которые осуществляют запись
полученных данных в резидентную БД. На вход модуль получает параметры price
и cache - класс подключения к БД, на выходе получаем список данных, 
которые затем сравниваем по номиналу и в случае отличия более, чем на 1%,
сообщаем об этом в консоль. 
'''


import logging


class CryptoTracking():

    def __init__(
        self,
        different_percent: float,
        price: str,
        cache,
    ):  
        self.DP = different_percent
        self.price = price
        self.cache = cache

    def data_prepare(self):
        '''
        Метод преобразует полученные данные в удобочитаемый вид
        '''
        ready_price = self.price[1:].replace(',', '') # убираем из строки знак $ и запятую
        return float(ready_price)

    def data_comparison(self):
        '''
        Метод получает готове данные, вычисляет процент полученных данных
        и в случае большой разницы - выводит информацию в консоль и записывает
        их в резидентную БД
        '''
        ready_price = self.data_prepare()
        ready_list = [float(item) for item in self.cache.lrange('ready_list', 0, -1)]           # redis сохраняет данные в список, оборачивая в str
        if ready_list == []:                                                                    # поэтому, чтобы сохранить формат, приходится дважды
            logging.info(f'НАЧАЛО РАБОТЫ. ТЕКУЩИЙ КУРС ФЬЮЧЕРСА ETHUSDT {ready_price}')     # преобразовывать в float                                                        
            return self.cache.lpush('ready_list', ready_price)                        
        else:
            if ready_price not in ready_list: # если цена не содержится в списке, то записываем, так бережём память
                current_percent = ready_price/100
                max_price = max(ready_list)
                min_price = min(ready_list)
                max_percent = max_price/100
                min_percent = min_price/100
                if (current_percent + self.DP) < min_percent: 
                    logging.info(f'ФЬЮЧЕРС ETHUSDT УПАЛ НА ↓{(min_price - ready_price).__round__(2)}$ '
                        f'↓{(((min_percent-current_percent)/min_percent)*100).__round__(3)} % '
                        f'ТЕКУЩИЙ КУРС ↓{ready_price}$')
                elif current_percent > (max_percent + self.DP): 
                    logging.info(f'ФЬЮЧЕРС ETHUSDT ВЫРОС НА ↑{(ready_price - max_price).__round__(2)}$ '
                        f'↑{(((current_percent-max_percent)/max_percent)*100).__round__(3)} % '
                        f'ТЕКУЩИЙ КУРС ↑{ready_price}$')
                return self.cache.lpush('ready_list', ready_price)
            return ready_list
        


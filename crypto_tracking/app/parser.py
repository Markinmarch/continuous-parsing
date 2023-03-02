'''
Модуль "parser" содержит методы, которые осуществляют асинхронный способ
парсинга данных. На вход модуль получает параметр "URL_PARS",
на выходе получаем строку с текущим курсом криптовалюты ETH. 
'''


from bs4 import BeautifulSoup
import aiohttp


async def search_course(url):
    '''
    Метод по параметру "url" парсит данные с сайта.
    '''
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'html.parser')
            search_on_tag = soup.find_all('span', class_ = 'no-wrap')[0] # эта строка индивидуальна для каждого сайта
            for course in search_on_tag:
                return course

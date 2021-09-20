import json
import requests
import hashlib
import os
import decorator



''' Класс итератор поиск стран  из файла в системе WIKI '''
class Search_Wiki:
    def __init__(self, country_item):
        self.country_item = country_item
        self.i = 0


    def get_info_wiki(self, country_name):
        res_dic = {}
        r = requests.get("https://en.wikipedia.org/api/rest_v1/page/summary/" + country_name)
        page = r.json()
        res_dic['Title'] = page['title']
        res_dic['Description'] = page['extract']
        res_dic['Link'] = page['content_urls']['desktop']['page']
        return res_dic

    def __iter__(self):
        self.i = 0
        return self


    def __next__(self):
        country_items = self.get_info_wiki(self.country_item[self.i]['name']['common'])
        self.i += 1
        if self.i > 5:
            raise StopIteration
        if country_items is None:
            raise StopIteration
        return str(list(country_items.values())).strip(",")


@decorator.parametrizeddecor('log_file.log')
def convert_md5(path_file, txt):
    return hashlib.md5(txt.upper().encode('utf-8')).hexdigest()


with open('countries.json', 'r', encoding='utf-8') as f:  # открыли файл с данными
 text = json.load(f)  # загнали все, что получилось в переменную
 f.close()
# Файл для записи
with open('countries_result.txt', 'w', encoding='utf-8') as myFile:

 my_path = os.path.abspath('countries_result.txt')
 for txt_ in Search_Wiki(text):
     # вызываем генератор MD5
    md5_hesh = convert_md5(str(my_path), txt_)
    myFile.write(txt_ + " \n")
    myFile.write("MD5: " + str(md5_hesh)+" \n")

 myFile.close()

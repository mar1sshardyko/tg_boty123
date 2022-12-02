import urllib.request
opener = urllib.request.build_opener()
response =  opener.open ("https://vk.com/")
print (response.read())
print("=======================================")
#кхурс dollar
import requests
res_parse_list = []
response = requests.get('https://minfin.com.ua/currency/')
response_text = response.text.split("<span>")
for parse_elem_1 in res_parse_list:
        if parse_elem_1.startswith('$'):
            #print(parse_elem_1)
            for parse_elem_2 in parse_elem_1.split('</span>'):
                    if parse_elem_2.startswith('$') and parse_elem_2[1].isdigit():
                            res_parse_list.append(parse_elem_2)
dollar = res_parse_list[0]
print(dollar)
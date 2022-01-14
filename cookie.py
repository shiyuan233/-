import json
import re

f = open("cookie.txt", "r", encoding="utf-8")
cookie_str = f.read()
f.close()

print(cookie_str)
cookie_str_re = cookie_str.replace(" ", '')
print(cookie_str_re)
cookie_str_list = re.split(";", cookie_str_re)
print(cookie_str_list)
cookie_value_str_list = [tuple(re.split("=", li)) for li in cookie_str_list]
print(cookie_value_str_list)
cookie_dict = {key: value for key, value in cookie_value_str_list}
print(cookie_dict)
s = open("cookie.json", 'w', encoding="utf-8")
s.write(json.dumps(cookie_dict))
s.close()

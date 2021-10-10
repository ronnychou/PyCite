# %%
import re
import importlib
from reflib.searcher import BaiduScholar
from reflib import constructor
from reflib.parser import GBT7714_Parser

# %%
title = 'Intercomparisons of cloud mask products among Fengyun-4A, Himawari-8, and MODIS'
title = title.encode('utf-8')
refs = BaiduScholar(title)()
ref_parse = GBT7714_Parser(refs['GBT7714'])()
ref = constructor.Acta_Meteorologica_Sinica(ref_parse)
print(ref)

# %%
GBT = '李五生,王洪庆,吴琼,王玉,王烨芳.静止卫星云图的云位置偏差及其几何校正[J].北京大学学报(自然科学版),2012,48(05):732-736.'
parse = GBT7714_Parser(GBT)()
ref = constructor.ActaMeteorologicaSinica(parse)()
print(ref)
# %%
parse = GBT7714_Parser(GBT)
author = parse['author']
title = parse['title']
journal = parse['journal']
year = parse['year']
volum = parse['volumn']
page = parse['page']
# %%
#                  作者          文献名[类型]        刊名      年份    卷号(期号):起止页码
pattern = '(.*?et al.|.*?)\.[ ]*(.*?)\[(\w?)\]\.[ ]*(.*?),[ ]*(.*?),[ ]*(.*):(.*?)\.$'
re.search(pattern, GBT).groups()
# %%
pattern = '(.*?)\.[ ]*(.*?)\[(\w?)\]\.[ ]*(.*?),[ ]*(.*?)\.$'
re.search(pattern, GBT).groups()
# %%
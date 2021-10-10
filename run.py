# %%
from reflib.searcher import BaiduScholar
from reflib import constructor
from reflib.parser import GBT7714_Parser

# %%
title = 'Intercomparisons of cloud mask products among Fengyun-4A, Himawari-8, and MODIS'
title = title.encode('utf-8')
refs = BaiduScholar(title)()
ref_parse = GBT7714_Parser(refs['GBT7714'])()
ref = constructor.ActaMeteorologicaSinica(ref_parse)
print(ref)
# %%
import re
import importlib
from reflib import search_ref
from reflib import ref_rule
importlib.reload(ref_rule)
# %%

# %%
title = 'Intercomparisons of cloud mask products among Fengyun-4A, Himawari-8, and MODIS'
title = title.encode('utf-8')
refs = search_ref(title)
ref_parse = ref_rule.journal_parser(refs['GBT7714'])
ref = ref_rule.Acta_Meteorologica_Sinica(ref_parse)
print(ref)


# %%
parse = ref_rule.journal_parser(GBT)
author = parse['author']
title = parse['title']
journal = parse['journal']
year = parse['year']
volum = parse['volumn']
page = parse['page']
# %%
GBT = '李五生,王洪庆,吴琼,王玉,王烨芳.静止卫星云图的云位置偏差及其几何校正[J].北京大学学报(自然科学版),2012,48(05):732-736.'
if '[D]' in GBT:
    ref_parse = ref_rule.dissertation_parser(GBT)
elif '[J]' in GBT:
    ref_parse = ref_rule.journal_parser(GBT)
ref = ref_rule.Acta_Meteorologica_Sinica(ref_parse)
print(ref)
# %%
#                  作者          文献名[类型]        刊名      年份    卷号(期号):起止页码
pattern = '(.*?et al.|.*?)\.[ ]*(.*?)\[(\w?)\]\.[ ]*(.*?),[ ]*(.*?),[ ]*(.*):(.*?)\.$'
re.search(pattern, GBT).groups()
# %%
pattern = '(.*?)\.[ ]*(.*?)\[(\w?)\]\.[ ]*(.*?),[ ]*(.*?)\.$'
re.search(pattern, GBT).groups()
# %%
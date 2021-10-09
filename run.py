# %%
import re
import importlib
from reflib import search_ref
from reflib import ref_rule
importlib.reload(ref_rule)
# %%

# %%
title = 'The role of orographic and parallax corrections on real time high resolution satellite rainfall rate distribution'
title = title.encode('utf-8')
refs = search_ref(title)
# print(refs['GBT7714'])
ref_parse = ref_rule.journal_parser(refs['GBT7714'])
ref = ref_rule.Acta_Meteorologica_Sinica(ref_parse)
print(ref)
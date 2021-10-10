import re
from .utils import baidu_translate
from . import journal_abbr as abbr
    

def Acta_Meteorologica_Sinica(parse):
    # import pypinyin

    author = parse['author']
    title = parse['title']
    journal = parse['journal']
    year = parse['year']
    volumn = parse['volumn']
    page = parse['page']

    author = author.split(',')
    author = [a.strip() for a in author]
    eng_flag = 1  # 英文，不做多余处理
    if author[0].upper()==author[0]:
        eng_flag = 0  # 中文，需要加各部分对应的英文翻译
        # TODO pypinyin for eng_author
        
        eng_title = baidu_translate(title)
        try:
            jn_abbr = abbr.abbr_zh[journal]
        except:
            jn_abbr = '!REPLACE!'
    if eng_flag:
        try:
            jn_abbr = abbr.abbr_en[journal]
        except:
            jn_abbr = journal
    
    if len(author)>3:
        author = author[:3]
        if eng_flag:
            author[-1] = author[-1] + ', et al'
        else:
            author[-1] = author[-1] + '等'
    author = ', '.join(author)
    if eng_flag:
        ref = f'{author}. {year}. {title}. {jn_abbr}, {volumn}: {page}.'
    else:
        ref = f'{author}. {year}. {title}. {journal}, {volumn}: {page}. NAME. {year}. {eng_title}. {jn_abbr}, {volumn}: {page} (in Chinese)'
    return ref

import re
from .utils import baidu_translate
from . import journal_abbr as abbr


def journal_parser(ref):
    # type=[J] 
    # parse = {'author':None, 'title':None, 'journal':None, 'year':None, 'page':None}
    parse = {}
    #                   作者          文献名[类型]       刊名      年份   卷号(期号):起止页码   
    pattern = '(.*?et al.|.*?)\.[ ]*(.*?)\[(\w?)\]\.[ ]*(.*?),[ ]*(.*?),[ ]*(.*):(.*?)\.$'
    _ref = re.search(pattern, ref).groups()
    parse['author'] = _ref[0]
    parse['title'] = _ref[1]
    parse['type'] = _ref[2]
    parse['journal'] = _ref[3]
    parse['year'] = _ref[4]
    parse['volumn'] = _ref[5]
    parse['page'] = _ref[6]
    return parse


def dissertation_parser(ref):
    # type=[D]
    parse = {}
    '王筱. 基于卫星云图与微波散射计的台风中心定位研究[D]. 杭州师范大学, 2017.'
    #           作者       文献名[类型]       保存单位    年份      
    pattern = '(.*?)\.[ ]*(.*?)\[(\w?)\]\.[ ]*(.*?),[ ]*(.*?)\.$'
    _ref = re.search(pattern, ref)
    parse['author'] = _ref[0]
    parse['title'] = _ref[1]
    parse['type'] = _ref[2]
    parse['loc'] = _ref[3]
    parse['year'] = _ref[4]
    return parse
    

def Acta_Meteorologica_Sinica(parse):
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
            eng_journal = abbr.abbr_zh[journal]
        except:
            eng_journal = '!REPLACE!'
    
    if len(author)>3:
        author = author[:3]
        if eng_flag:
            author[-1] = author[-1] + ', et al'
        else:
            author[-1] = author[-1] + '等'
    author = ', '.join(author)
    if eng_flag:
        ref = f'{author}. {year}. {title}. {journal}, {volumn}: {page}.'
    else:
        ref = f'{author}. {year}. {title}. {journal}, {volumn}: {page}. NAME. YEAR. {eng_title}. {eng_journal}, {volumn}: {page} (in Chinese)'
    return ref

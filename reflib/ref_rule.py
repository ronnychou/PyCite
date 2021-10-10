from .utils import baidu_translate
from . import journal_abbr as abbr


class ActaMeteorologicaSinica():
    """构造气象学报的引用格式"""

    def __init__(self, parse) -> None:
        self.parse = parse
        self.type = parse['type']
    
    def __call__(self):
        if self.type=='J':
            return self.journal()
        if self.type=='D':
            return self.dissertation()

    # import pypinyin
    def journal(self):
        parse = self.parse
        author = parse['author']
        title = parse['title']
        journal = parse['journal']
        year = parse['year']
        volumn = parse['volumn']
        page = parse['page']

        author = author.split(',')
        author = [a.strip() for a in author]
        en_flag = 1  # 英文，不做多余处理
        if author[0].upper()==author[0]:
            en_flag = 0  # 中文，需要加各部分对应的英文翻译
            # TODO pypinyin for author_pinyin
            author_pinyin = 'NAME'
            try:
                title_en = baidu_translate(title)
            except:
                title_en = 'TITLE_EN'
            try:
                jn_abbr = abbr.abbr_zh[journal]
            except:
                jn_abbr = 'JOURNAL_ABBR_EN'
        if en_flag:
            try:
                jn_abbr = abbr.abbr_en[journal]
            except:
                jn_abbr = journal
        
        if len(author)>3:  # 超过3人的部分简写成“等”
            author = author[:3]
            if en_flag:
                author[-1] = author[-1] + ', et al'  # et al.
            else:
                author[-1] = author[-1] + '等'
        author = ', '.join(author)
        if en_flag:
            ref = f'{author}. {year}. {title}. {jn_abbr}, {volumn}: {page}.'
        else:
            ref = f'{author}. {year}. {title}. {journal}, {volumn}: {page}. {author_pinyin}. {year}. {title_en}. {jn_abbr}, {volumn}: {page} (in Chinese)'
        return ref

    def dissertation(self):
        pass

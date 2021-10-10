import re


class GBT7714_Parser():
    def __init__(self, ref) -> None:
        self.ref = ref

    def __call__(self):
        if '[J]' in self.ref:
            ref_parse = self.journal_parser()
        if '[D]' in self.ref:
            ref_parse = self.dissertation_parser()
        return ref_parse

    def journal_parser(self):
        # type=[J] 
        # parse = {'author':None, 'title':None, 'journal':None, 'year':None, 'page':None}
        parse = {}
        #                   作者          文献名[类型]       刊名      年份   卷号(期号):起止页码   
        pattern = '(.*?et al.|.*?)\.[ ]*(.*?)\[(\w?)\]\.[ ]*(.*?),[ ]*(.*?),[ ]*(.*):(.*?)\.$'
        try:
            _ref = re.search(pattern, self.ref).groups()
            parse['author'] = _ref[0]
            parse['title'] = _ref[1]
            parse['type'] = _ref[2]
            parse['journal'] = _ref[3]
            parse['year'] = _ref[4]
            parse['volumn'] = _ref[5]
            parse['page'] = _ref[6]
        except:
            print('请检查<GB/T 7714>的<期刊>引用格式! 其必须是 <作者.文献名[类型].刊名.年份,卷号(期号):起-止页码.>')
        return parse

    def dissertation_parser(self):
        # type=[D]
        parse = {}
        #           作者       文献名[类型]       保存单位    年份      
        pattern = '(.*?)\.[ ]*(.*?)\[(\w?)\]\.[ ]*(.*?),[ ]*(.*?)\.$'
        try:
            _ref = re.search(pattern, self.ref)
            parse['author'] = _ref[0]
            parse['title'] = _ref[1]
            parse['type'] = _ref[2]
            parse['loc'] = _ref[3]
            parse['year'] = _ref[4]
        except:
            print('请检查<GB/T 7714>的<学位论文>引用格式! 其必须是 <作者.文献名[类型].保存单位,年份.>')
        return parse


class MLA_Parser():
    pass


class APA_Parser():
    pass


class BibTex_Parser():
    pass
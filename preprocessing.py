import numpy as np
import pandas as pd
import re
import jieba

if __name__ == '__main__':
    f = open('./ptt/gossip.json', 'r', encoding='utf-8')
    lines = f.readlines()
    articals = []
    for line in lines:
        try:
            articals.append(eval(line)[0])
        except:
            pass
    f.close()

    # 1.正、負向文章排序
    tit = []
    sco = []
    url = []

    # 2.正、負評論常見詞
    up = []
    down = []
    for i in range(len(articals)):
        # 1.
        tit.append(articals[i]['title'])
        sco.append(articals[i]['score'])
        url.append(articals[i]['url'])
        
        # 2.
        if articals[i]['comments']:
            for com in articals[i]['comments']:
                if com['score'] == 1:
                    up.append(com['content'][2:])
                elif com['score'] == -1:
                    down.append(com['content'][2:])

    # 1.
    sco = np.array(sco)
    asc = np.argsort(sco)
    dsc = np.flipud(asc) 
    # for i in range(3):
    #     print('positive articals\n', tit[dsc[i]], url[dsc[i]], sco[dsc[i]])
    #     print('negitive articals\n', tit[asc[i]], url[asc[i]], sco[asc[i]])

    good = {'title': [tit[dsc[i]] for i in range(10)],
            'score': [sco[dsc[i]] for i in range(10)],
            'url': [url[dsc[i]] for i in range(10)]
            }

    bad = {'title': [tit[asc[i]] for i in range(10)],
            'score': [sco[asc[i]] for i in range(10)],
            'url': [url[asc[i]] for i in range(10)]
            }

    df = pd.DataFrame(good, columns= ['title', 'score', 'url'])
    df.to_csv ('good.csv', index = False, header=True)
    df = pd.DataFrame(bad, columns= ['title', 'score', 'url'])
    df.to_csv ('bad.csv', index = False, header=True)

    # 2.
    def comment(up):
        count  = jieba.lcut("".join(up))
        cop = re.compile("[^\u4e00-\u9fa5^a-z^A-Z^0-9]") # 匹配不是中文、大小写、数字的其他字符

        #定义空字典，对分词结果进行词频统计
        word_count={}
        for word in count:
            word = cop.sub('', word)
            if word: # 非空字符
                word_count[word] = word_count.get(word, 0) + 1

        items = list(word_count.items())
        items.sort(key=lambda x: x[1], reverse=True)
        
        tmp = []
        for k, v in items:
            if len(k) > 1:
                tmp.append((k,v))
        return tmp
        
    u = comment(up)
    d = comment(down)

    up = {'keywords': [u[i][0] for i in range(30)],
            'counts': [u[i][1] for i in range(30)]
            }
    down = {'keywords': [d[i][0] for i in range(30)],
            'counts': [d[i][1] for i in range(30)]
            }

    df = pd.DataFrame(up, columns= ['keywords', 'counts'])
    df.to_csv ('up.csv', index = False, header=True)
    df = pd.DataFrame(down, columns= ['keywords', 'counts'])
    df.to_csv ('down.csv', index = False, header=True)
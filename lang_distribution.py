import os
import json
import operator
import numpy as np
from matplotlib import pyplot as plt

def language_distribution(path):
    langs = {} 
    for par, dirs, fs in os.walk(path):
        for f in fs:
            fpath = os.path.join(par, f)
            name = f.split("_")[0]
            if name not in langs:
                langs[name] = {}
            with open(fpath, "r") as fp:
                for line in fp.readlines():
                    data_dict = json.loads(line)
                    if data_dict['language'] not in langs[name]:
                        langs[name][data_dict['language']] = 1
                    else:
                        langs[name][data_dict['language']] += 1
    return langs
 
def plot_lang_dis(lang_dict):

    for name, langs in lang_dict.items():
        sorted_langs = sorted(langs.items(), key=operator.itemgetter(1), reverse=True)[:5]
        sorted_langs = [tup for tup in sorted_langs if tup[0] != 'und'][:4]
        ind = np.arange(4)
        height = []
        tag = []
        for tup in sorted_langs:
            tag.append(tup[0])
            height.append(tup[1])
        plt.bar(ind, height)    
        plt.xticks(ind, tag)
        plt.title(name)
        plt.xlabel("language")
        plt.ylabel("#")

        # plt.show()
        fname = 'team_view/%s.png' % (name) 
        plt.savefig(fname)
        plt.close()


        

def plot_team_dis(lang_dict):
    lang_type = list(lang_dict['WashingtonJustice'].keys())
    for ty in lang_type:
        if ty == 'und':
            continue
        bar_data = {}
        for tname, t_count in lang_dict.items():
            if ty in t_count.keys():
                bar_data[tname] = t_count[ty]
        sorted_team = sorted(bar_data.items(), key=operator.itemgetter(1), reverse=True)
        height = []
        tag = []
        for tup in sorted_team:
            tag.append(tup[0])
            height.append(tup[1])
        ind = np.arange(len(tag))
        plt.bar(ind, height)
        plt.xticks(ind, tag, rotation="vertical")
        plt.title(ty)

        fname = 'lang_view/%s.png' % (ty)
        plt.savefig(fname)
        plt.close()


plot_lang_dis(language_distribution("data"))
plot_team_dis(language_distribution("data"))
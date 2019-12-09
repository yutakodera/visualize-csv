#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

# for using Japanese fonts
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = {'Hiragino Maru Gothic Pro','Yu Gothic', 'Meirio','Takao','IPAexGothic','IPAPGothic','VL PGothic','Noto Sans CJK JP'}


#df.iat[0,0] = "date"
#for l in range(1,len(df)):
#  df.iat[l,0] = df.iat[l,0].encode('utf-8').replace('年','/').replace('月','/').replace('日','')
#  print(df.iat[l,0])
#  date.append(d.encode('utf-8').replace('年','/').replace('月','/').replace('日',''))
  

#print(df.iat[0,0])
#print(type(df.iat[0,0]))
#print(df.iat[0,0].replace("年","-")

def plot_and_savefig(index,filename):
  plt.figure()

  #df.plot(x=df.columns[0],y=df.columns[column_index])
  df.plot(x=df.columns[0],y=df.columns[index])
  plt.xticks(rotation=90,size='small') 
  plt.subplots_adjust(left=0.1,right=0.95,bottom=0.3,top=0.95)
  plt.savefig(filename)
  plt.close("all")

def generate_html(df):
  column_index = []
 
  # get the label of columns only consisting of digits
  column_label = df.select_dtypes(include=[int,float])
 
  html = '<!DOCTYPE html>\n'\
         '<html lang="ja">\n'\
         '<head>\n'\
         '<meta charset="utf-8">\n'\
         '<meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit-no">\n'\
         '<title>オリジナルデータ</title>\n'\
         '</head>\n'\
         '<body>\n'\
         '<ul>\n<li><a href="raw_data.html">Raw data</a></li>'

  # example for generating graphs as links
  for label in column_label:
    filename = 'fig/' + label.replace('/','_per_') + '.png'
    plot_and_savefig(df.columns.get_loc(label),filename)
    new_label = '<a href="' + filename + '">' + label + '</a>'
    df = df.rename(columns={label: new_label})

  html += df.to_html().replace('&lt;','<').replace('&gt;','>')
  html += '\n</body>\n'\
          '</html>\n'
  with open('raw_data.html','w') as f:
    f.write(html)


  # example for embedding graphs into html as figures
#  html = '<!DOCTYPE html>\n'\
#         '<html lang="ja">\n'\
#         '<head>\n'\
#         '<meta charset="utf-8">\n'\
#         '<meta name="viewport" content="width=device-width,initial-scale=1,shrink-to-fit-no">\n'\
#         '<title></title>\n'\
#         '</head>\n'\
#         '<body>\n'
#
#  html += '<ul>\n<li><a href="raw_data.html">Raw data</a></li>'
#  for label in column_label:
#    filename = 'fig/' + label.replace('/','_per_') + '.png'
#
#    html += '<li>' + label + '<br><img src="'+ filename + '">'+ '</li>\n'
#    plot_and_savefig(df.columns.get_loc(label),filename)
#
#  html += '</ul>\n'
#  html += '</body>\n'\
#          '</html>\n'
#  with open('sample.html','w') as f:
#    f.write(html.encode('utf-8'))


if __name__ == '__main__': 
  df = pd.read_csv('okayama_weatherdata.csv',encoding='shift-jis',header=0)
  generate_html(df)
  


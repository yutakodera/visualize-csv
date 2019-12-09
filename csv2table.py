#!/usr/bin/python3
#-*- coding: utf-8 -*-

import cgi
import pandas as pd
import sys
import io
import os
import glob


sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
print('Content-Type: text/html; charset="utf-8"\n\n')
html = """
  <!DOCTYPE html>
  <html>
    <head>
      <meta charset='utf-8'>
      {0}
    </head>
    <body>
      {1}
    </body>
  </html>
  """

def ReceiveFile():
  fileitem = ''
  form = cgi.FieldStorage()
  filename = form['upfile'].filename
  filepath = '/var/www/html/dlc/' + filename
  fileitem = form['upfile'].value

  return filename, filepath,fileitem


if __name__ == '__main__':
  filelist = glob.glob('/var/www/html/dlc/*')
  for file in filelist:
    os.remove(file)

  filename, filepath, fileitem = ReceiveFile()
  with open(filepath,'wb') as f:
    f.write(fileitem)
  df = pd.read_csv(filepath,encoding='utf-8')
  
  meta = """\
    <style>\
    html,body {\
      margin: 10px;\
      padding: 0;\
    }\
    table,thead,th,td {\
      table-layout: fixed;\
      border-collapse: collapse;\
      width: 200px;\
      line-height: 1.5;\
      border: solid 1px;\
    }\
    .options_form { \
      margin-left: 10px;\
    }\ 
    </style>\
  """ + '<title>{0}</title>'.format(filename)
  
  body = """\
    <h3>Available options</h3> 
    <ol> 
      <li>Remove columns: <br />
        <div class="options_form">
          <p>Input the name of column labels that you want to remove from below</p>
          <p>Line up the name of columns with comma separation if you have two or more candidates for eliminating from the table without any spaces</p>
          <form method="post" action="/cgi-bin/edit_table.py" accept-charset="utf-8"> 
""" \
+ '          <p>filename: </p><input name="filename" type="text" value="{0}" readonly="readonly">'.format(filename) + \
"""
          <p>column labels: </p><input name="remove" type="text"> <br />
          <input value="submit" type="submit">
          </form>
        </div>
      </li> <br />
      <li>Pickup columns: <br />
        <div class="options_form">
          <p>Input the name of column labels that you want to pickup from below</p>
          <p>Line up the name of columns with comma separation if you have two or more candidates</p>
          <form method="post" action="/cgi-bin/edit_table.py" accept-charset="utf-8"> 
""" \
+ '          <p>filename: </p><input name="filename" type="text" value="{0}" readonly="readonly">'.format(filename) + \
"""
          <p>column labels: </p><input name="pickup" type="text"> <br />
          <input value="submit" type="submit">
          </form>
        </div>
      </li> <br />
""" \
+ '      <li><a href="http://localhost/dlc/{0}" download="{0}">Download the current table</a></li>'.format(filename) + \
"""
    </ol>
     <br />
  """ + df.to_html(escape=False).replace(' style="text-align: right;"','')
  
  print(html.format(meta,body))


from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd


app = Flask(__name__)

df1 = pd.read_csv('good.csv', index_col=False)  
df2 = pd.read_csv('bad.csv', index_col=False) 
df3 = pd.read_csv('up.csv', index_col=False) 
df4 = pd.read_csv('down.csv', index_col=False) 

@app.route('/')
def html_table():
    pos = []; neg = []; up = []; down = []
    for i in range(df1.index.stop):
        pos.append({
            'title': df1.iloc[i][0],
            'score': df1.iloc[i][1],
            'url': df1.iloc[i][2]
        })
    for i in range(df2.index.stop):
        neg.append({
            'title': df2.iloc[i][0],
            'score': df2.iloc[i][1],
            'url': df2.iloc[i][2]
        })
    for i in range(df3.index.stop):
        up.append({
            'keywords': df3.iloc[i][0],
            'counts': df3.iloc[i][1]
        })
    for i in range(df4.index.stop):
        down.append({
            'keywords': df4.iloc[i][0],
            'counts': df4.iloc[i][1]
        })
    return render_template(
        'index.html',
        pos = pos,
        neg = neg,
        up = up,
        down = down
    )


if __name__ == '__main__':
    app.run(debug=True)
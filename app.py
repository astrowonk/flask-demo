from flask import Flask, render_template, request, redirect

import requests

from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.models import ColumnDataSource
import pandas as pd
app = Flask(__name__)

def getStockInfo(ticker):

  queryString = "https://api.iextrading.com/1.0/stock/" + ticker + "/chart/1y"
  myRaw = requests.get(queryString)
  if myRaw.status_code == 200:
    myData = pd.DataFrame.from_dict(myRaw.json())
    myData['date'] = pd.to_datetime(myData['date'])
  else:
    myData = pd.DataFrame()
  return(myData)



@app.route('/',methods=['GET','POST'])
def index():
  aTicker = request.form.get('symbol')
  if aTicker == None:
    print('what?')
    aTicker='TSLA'

  myData = getStockInfo(aTicker)

  if myData.size == 0:
    errorText = "No Stock Price Data for: " + aTicker.upper()
    script = ""
    div = ""
  else:
    errorText = ""
    fig = figure(plot_width=800, plot_height=600, x_axis_type='datetime')
    source = ColumnDataSource(data=myData)

    fig.circle(x='date', y='close', source=source)
    script, div = components(fig)

  if request.method == 'GET':
    return render_template('index.html',script=script, div=div, text=aTicker.upper(),errorText=errorText)
  else:
    aTicker = request.form.get('symbol')
    return render_template('index.html',script=script, div=div, text=aTicker.upper(), errorText=errorText)


@app.route('/about')
def about():
  return render_template('about.html')



if __name__ == '__main__':
  app.run(port=33507)

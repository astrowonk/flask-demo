# Flask on Heroku

This is my first Flask project, [deployed here on Heroku](https://stockplot-astrowonk.herokuapp.com).

I used the [IEX Trading API](https://iextrading.com/developer/docs/#getting-started) for the data source and [Bokeh](https://bokeh.pydata.org/) for plotting.

The app takes a stock ticker as input and plots a one-year history of the stock price. It will plot nothing and show a message if the ticker does not exist in IEX's data.

The data is loaded with requests and stored in a pandas data frame, before being passed to Bokeh.


import yfinance as yf
import matplotlib.pyplot as plt

dat = yf.Ticker("MSFT")

stock_data = dat.history(period='1mo')

close_data = stock_data.Close
close_data_plt = close_data.plot()
close_data_plt.grid('minor')
close_data_plt.figure.show()


plt.show(block=True)
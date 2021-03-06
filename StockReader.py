#econogee, 1/28/2016
#Stock Data Retrieval Script
#If executed via the command line, will produce 500 data files with stock price information
#between the dates specified in the main method.  Can also be imported to use the RetrieveStock method.

import os
import sys
import numpy as np
import urllib2


def RetrieveStock(TickerSymbol,start,end):
	startday,startmonth,startyear = (str(s) for s in start)
	endday,endmonth,endyear = (str(s) for s in end)
	response = urllib2.urlopen('http://real-chart.finance.yahoo.com/table.csv?s='+str(TickerSymbol)+\
								'&a=' + startday + '&b=' + startmonth + '&c=' + startyear + \
								'&d=' + endday + '&e=' + endmonth + '&f=' + endyear + \
								   '&g=d&ignore=.csv')
	html = response.read()
	html = html.split('\n')
	html = np.array(html)
	
	return html



def main():
	startday = str(0)
	startmonth = str(1)
	startyear = str(2005)

	endday = str(30)
	endmonth = str(1)
	endyear = str(2016)


	symbols = []
	with open('stocklist.csv') as f:
		content = f.readlines()
		for l in content:
			symbols.append(l.split(",")[0])
			
	for s in symbols:
		html = RetrieveStock(s,(startday,startmonth,startyear),(endday,endmonth,endyear))
		np.savetxt(str(s),html,fmt='%s',delimiter=',')

if __name__ == "__main__": main()
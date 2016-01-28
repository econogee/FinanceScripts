#econogee, 1/28/2016
#Stock Data Retrieval Script

import os
import numpy as np
import urllib2

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
    response = urllib2.urlopen('http://real-chart.finance.yahoo.com/table.csv?s='+str(s)+\
                            '&a=' + startday + '&b=' + startmonth + '&c=' + startyear + \
                            '&d=' + endday + '&e=' + endmonth + '&f=' + endyear + \
                               '&g=d&ignore=.csv')
    html = response.read()
    html = html.split('\n')
    html = np.array(html)
    np.savetxt(str(s),html,fmt='%s',delimiter=',')

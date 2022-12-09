# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 15:24:54 2022

@author: Rupesh
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 19:13:38 2022

@author: Rupesh
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns


def getdata(filename):
    '''
    

    Parameters
    ----------
    filename : TYPE
        DESCRIPTION.

    Returns
    ------- 
    df : TYPE
        DESCRIPTION.
    df2 : TYPE
        DESCRIPTION.

    '''
    df = pd.read_csv(filename, skiprows=(4), index_col=False)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.loc[df['Country Name'].isin(countries)]
    df2 = df.melt(id_vars=['Country Name','Country Code','Indicator Name','Indicator Code'], var_name='Years')
    
    del df2['Country Code']
    df2 = df2.pivot_table('value',['Years','Indicator Name','Indicator Code'],'Country Name').reset_index()

    return df, df2

#df2.to_excel('test_data.xlsx')
countries = ['Finland','Belgium','Spain','Switzerland','Germany']

#for Lineplot
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('EG.USE.ELEC.KH.PC')]

plt.figure()
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title='Electric power consumption (kWh per capita)')
plt.show()



#For Piechart
df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('EG.ELC.RNWX.ZS')]
print(df2)

#df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','EN.ATM.CO2E.SF.ZS')
#df2.dropna()

fin= np.sum(df2['Finland'])
bel= np.sum(df2['Belgium'])
spe= np.sum(df2['Spain'])
swi= np.sum(df2['Switzerland'])
ger= np.sum(df2["Germany"])

total= fin + bel + spe + swi + ger

fin_eu= fin/ total*100
bel_eu= bel/ total*100
spe_eu= spe/ total*100
swi_eu= swi/ total*100
ger_eu= ger/ total*100

Energy_use= np.array([fin_eu, bel_eu,spe_eu,swi_eu, ger_eu])


plt.figure(dpi=144)
plt.pie(Energy_use, labels= countries, shadow=True, autopct=('%1.1f%%'))# We used autopct for showing percantages on piechart
plt.title("Electricity production from renewable sources, excluding hydroelectric (% of total)") # This function is for showing title of data
plt.show()

#For Barplot

df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('EG.FEC.RNEW.ZS')]
print(df2)
#df2.to_excel('test_data5.xlsx')



df2 = df2.loc[df2['Years'].isin(['2000','2001','2002','2003','2004'])]
num = np.arange(5)
width = 0.2
years = df2['Years'].tolist()

plt.figure(dpi=120)
plt.title('Access to electricity (% of population)')
plt.bar(num, df2['Finland'], width, label='Finland')
plt.bar(num+0.2, df2['Belgium'], width, label='Belgium')
plt.bar(num-0.2, df2['Spain'], width, label='Spain')
plt.bar(num+0.4, df2['Switzerland'], width, label='Switzerland')
plt.bar(num-0.2, df2['Germany'], width, label='Germany')
plt.xticks(num, years)
#plt.yticks(np.arange(100,6000,1000))
plt.xlabel('Years')
plt.ylabel('% Of Population')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
#plt.xlim(2000,2004)
plt.show()

# new one Line plot2

df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('EG.ELC.RNEW.ZS')]

plt.figure()
df2['Years'] = pd.to_numeric(df2['Years'])
df2.plot("Years", countries, title='Renewable electricity output (% of total electricity output)')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
plt.show()

# new pie chart2


df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('EG.ELC.HYRO.ZS')]
print(df2)

#df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv','EN.ATM.CO2E.SF.ZS')
#df2.dropna()

fin= np.sum(df2['Finland'])
bel= np.sum(df2['Belgium'])
spe= np.sum(df2['Spain'])
swi= np.sum(df2['Switzerland'])
ger= np.sum(df2["Germany"])

total= fin + bel + spe + swi + ger

fin_eu= fin/ total*100
bel_eu= bel/ total*100
spe_eu= spe/ total*100
swi_eu= swi/ total*100
ger_eu= ger/ total*100

Energy_use= np.array([fin_eu, bel_eu,spe_eu,swi_eu, ger_eu])


plt.figure(dpi=144)
plt.pie(Energy_use, labels= countries, shadow=True, autopct=('%1.1f%%'))# We used autopct for showing percantages on piechart
plt.title("Electricity production from hydroelectric sources (% of total)") # This function is for showing title of data
plt.show()

#bar plot2

df, df2 = getdata('API_19_DS2_en_csv_v2_4700503.csv')
df2 = df2.loc[df2['Indicator Code'].eq('SP.POP.TOTL')]
print(df2)
#df2.to_excel('test_data5.xlsx')



df2 = df2.loc[df2['Years'].isin(['2000','2001','2002','2003','2004'])]
num = np.arange(5)
width = 0.2
years = df2['Years'].tolist()

plt.figure(dpi=120)
plt.title('Population, total')
plt.bar(num, df2['Finland'], width, label='Finland')
plt.bar(num+0.2, df2['Belgium'], width, label='Belgium')
plt.bar(num-0.2, df2['Spain'], width, label='Spain')
plt.bar(num+0.4, df2['Switzerland'], width, label='Switzerland')
plt.bar(num-0.2, df2['Germany'], width, label='Germany')
plt.xticks(num, years)
#plt.yticks(np.arange(100,6000,1000))
plt.xlabel('Years')
plt.ylabel('% Of Population')
plt.legend(loc='center left',bbox_to_anchor=(1,0.5))
#plt.xlim(2000,2004)
plt.show()


#heatmap




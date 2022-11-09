import pandas as pd
from bs4 import BeautifulSoup
import requests

def sum_of_company(company_url):      #will give the basic summary of the company
    html_text= requests.get(company_url).text
    soup = BeautifulSoup(html_text,'lxml')
    abcd= soup.find('div', class_='innerpagecontent')
    summ=abcd.find('div',id='compess')
    inside_summ=summ.find('div', id='mainContent_divCompanyEssentials')
    para_summ=inside_summ.find_all('div', class_ ='col-6 col-md-4 compess')
    a=0
    for i in para_summ:
        if(a==16):
            break
        para_name=para_summ[a].small.text
        para_val=para_summ[a].p.text
        para_val_ws=para_val.replace(' ','')
        para_name_ws=para_name.replace(' ','')
        print(f'{para_name_ws.strip()}:') 
        print(f'{para_val_ws.strip()}\n')
        a=a+1

#________________________________________________________________________________________

#def quarterly_result(company_url):
    html_text=requests.get(company_url).text
    soup=BeautifulSoup(html_text,'lxml')
    qua_res_big=soup.find('div',class_='innerpagecontent')
    qua_res_small=qua_res_big.find('div',id='mainContent_pnlCompanyDetails')
    qua_res_fin=qua_res_small.find('div',id='mainContent_quarterly')
    abc=qua_res_fin.find('div',class_='col-12')
    xyz=abc.find('div',class_='card cardscreen')
    print(xyz.h4.text)
    full_table=xyz.find('table', class_='table')
    header=[]
    for i in full_table.thead.find_all('th'):
        title=i.text.strip()
        header.append(title)
    df =pd.DataFrame(columns = header)
    print(df)


#_______________________________________________________________________________________

company_name=input("Enter the company name: ")
company_url='https://ticker.finology.in/company/'+company_name
sum_of_company(company_url)
#quarterly_result(company_url)

print('Hello World')
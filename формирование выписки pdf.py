from fpdf import FPDF
from translate import Translator
import pandas as pd

time=['12:45','13:12','16:39','20:20']
name=['Татьяна В.','Серафима Л.','Максим П.','Екатерина П.']
summa=['+3200','-5100','+6100','-1200']
currency=['Рубль России','Рубль России','Доллар США','Фунт стерлингов']
history=pd.DataFrame()
history['time']=time
history['name']=name
history['summa']=summa

history['currency']=currency
history['user']='Крапивина Елизавета Антоновна'

def translating(words):
    translator=Translator(from_lang='ru',to_lang='en')
    end_text=translator.translate(words)
    return end_text
def create_bank_statement(table_of_history):
    for i in list(table_of_history.columns.values):
        table_of_history[i]=table_of_history[i].apply(translating)
    pdf=FPDF('P','mm','letter')
    pdf.add_page()
    pdf.set_font('helvetica','',16)
    pdf.cell(40,10,table_of_history.iloc[0][3],ln=True)
    for i in range(table_of_history.shape[0]):
        pdf.cell(40,10,table_of_history.iloc[i][0]+' '+table_of_history.iloc[i][1]+' '+table_of_history.iloc[i][2]+' '+table_of_history.iloc[i][3],ln=True)
    pdf.output('bank-statement.pdf')


create_bank_statement(history)

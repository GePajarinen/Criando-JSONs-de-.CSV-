from csv import reader
import re
import json

'''
-- SEM cabeçalho
0."COLUMN_NAME",*
1."DATA_TYPE",*
2."NULLABLE",*
3."DATA_DEFAULT", X
4."COLUMN_ID", X
5."COMMENTS" *
'''

def _descrp(string):
 s = string.encode(encoding='ASCII',errors='ignore')
 c = s.decode("utf-8")
 return c


def _tipo(string):
  if string == 'VARCHAR2':
    return "STRING";
  if string == 'NUMBER':
    return "NUMERIC";
  else:
    return string;
    

arquivo = input('Nome do arquivo: ')


arquivo = arquivo +'.csv'
destino = arquivo[:-3] + 'json'

conta = len(open(arquivo).readlines())
maxi = conta

with open(arquivo, 'r') as read_obj:
    
    csv_reader = reader(read_obj)

    for row in csv_reader:
      #NAME:
      name = row[0]
      
      #TYPE:
      typo = re.match(r"^[^(]*", row[1]).group(0)
      typo = _tipo(typo)
     
      #MODE:
      if row[2] == 'true':
        mode = "NULLABLE"
      else:
        mode = "REQUIRED"

      #DESCRIPTION:
      description = _descrp(row[5])


      x = {
        "name": name, 
        "type": typo,
        "mode": mode,
        "description": description
      }
      # convert into JSON:
      j = json.dumps(x)
      #print(j)

      with open(destino, 'a') as fp:
        pass

        if conta==maxi:
          fp.write('[')

        fp.write(j)
       
        if conta !=1:
          fp.write(',')
        if conta ==1:
          fp.write(']')

      conta=conta-1
      
print("Pronto!")
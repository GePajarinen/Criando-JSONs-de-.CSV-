# Criando .JSON a partir de .CSV

Criei essa função para suprir a necessidade de criar arquivos json com um modelo determidado a partir de arquivos csv.   
O modelo do json foi determinado para atender à criação de tabelas no BigQuery.    
O arquivo orignal csv é exportado do Oracle sem cabeçalho e delimitado por vírgulas, constando as informações das colunas:   
COLUMN_NAME | DATA_TYPE | NULLABLE | DATA_DEFAULT | COLUMN_ID | COMMENTS   
Então são feitas as seguintes converções:   




## Como funciona:  
Abra essa pasta dento do VS code. Ou se preferir, abra no idle online:  
Basta acionar o arquivo csv entro desta pasta.    
Rodar o arquivo main.py.   
A execução pede o nome do arquivo. Escreva-o sem a extensão. Exemplo: se o nome do arquivo for lista_comercial.csv escreva somente lista_comercial.   
Logo então, o arquivo json será criado dentro desta pasta.    

Problemas que podem ocorrer:
Se os dados expostados do Oracle estiverem no formato errado.
Se houver espaços de enter e/ou tabs dentro das linhas de cometário.
Para solucionar estes problemas, você deveria arrumar os dados manualmente ou utilizar de outra ferramenta.

Às vezes, o arquivo csv também pode sofre modificações e aparecer com aspas duplas no início e no final de cada linha (row). Isso faz que cada linha seja considerada como uma única coluna.
Copiar os dados do csv e colar diretamente em outro arquivo pode resolver o problema. Dê ao arquivo o mesmo nome do arquivo orginal de onde copiou os dados.

foto exemplo 1

foto exemplo 2

Este sistema inda não converte caracteres especiais. Então, o resultado pode ficar assim:   
"C\u00c3\u00b3digo \u00c3\u00banico da configura\u00c3\u00a7\u00c3\u00a3o do Card do sis   

-Enquanto resolvo esse problema, você pode copiar todos o resultado do arquivo json e colar em um json editor como . https://jsoneditoronline.org/#right=local.xosome
Nele, as conversões de caracteres são corrigidas e também tem a opção de editar o json em formato de árvore ao invés de linha. 



### Exemplo do json:

[
    {
      "name": "id",
      "type": "INT64",
      "mode": "REQUIRED",
      "description": "ID de registro (Clave Primaria)."
    },
    {
      "name": "short_desc",
      "type": "STRING",
      "mode": "REQUIRED",
      "description": "Descripcion corta de este elemento."
    },
    {
      "name": "amount",
      "type": "INT64",
      "mode": "NULLABLE",
      "description": "Sobre mimos valores"
    },
    {
      "name": "date_from",
      "type": "DATE",
      "mode": "REQUIRED",
      "description": "Fecha de inicio"
    },
    {
      "name": "status_date",
      "type": "TIMESTAMP",
      "mode": "REQUIRED",
      "description": "Fecha de ultimo cambio de estado"
    },
  ]
OK no REPLIT e no VS code. Mas queria fazer funcionar no cmd

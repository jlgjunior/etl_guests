# etl_guests

O resultado após t1 pode ser visualizado no arquivo pessoasTableT1.csv.
<br/>
<br/>
Foram usados os frameworks SQLAlchemy para mapeamento ORM e flask, flask-scripts e flask-migration para realizar migrações.
<br/>
<br/>
O driver usado para acessar um banco postgres foi o psycopg2.
<br/>
<br/>
Os comandos que devem ser executados em ordem para o funcionamento, possuindo o servidor postgres instalado com as bases stag_int e cli (o nome de usuário e senha usados foram application), são:
<br/>
python3 manageStag.py db init
<br/>
python3 manageStag.py db migrate
<br/>
python3 manageStag.py db upgrade
<br/>
python3 manageStag.py seed
<br/>
rm -R migrations/
<br/>
python3 manageCli.py db init
<br/>
python3 manageCli.py db migrate
<br/>
python3 manageCli.py db upgrade
<br/>
python3 manageCli.py seed
<br/>
<br/>
Com isso o banco de dados é inicializado com os valores iniciais de T0.
<br/>
<br/>
Após isso rodar o arquivo ETL.py
<br/>
nohup python3 ETL.py &
<br/>
disown
<br/>
<br/>
O serviço continuamente consulta a tabela hospedes na base stag_ini e arquivos txt com campos separados por tab, como era o arquivo de exemplo, localizados na pasata data/
<br/>
<br/>
Os valores encontrados na tabela hospedes atualizam valores na tabela pessoas da base cli, tabela que também é atualizada pelos arquivos da pasta data, porém apenas para novas entradas, visto que o arquivo não fornece nenhum identificador único de uma pessoa.
<br/>
A tabela pessoasTableT2.csv contém o csv com os dados da tabela no tempo T2.
<br/>
A verificação de importaçao de novos dados para a tabela pessoas da base cli é realizada a cada 30s.

# Introdução
O repositório tem como objetivo fornecer um ambiente de desenvolvimento para PySpark, contendo :
* datalake - estrutura de diretórios e arquivos fontes para os desenvolvimentos.
* docker - Arquivo DockerFile para criação da imagem utilizada no desenvolvimento.
* pyspark - Contem os notebooks python e arquivo docker-compose, responsável pela orquestração do * * * container docker.

# Criação da imagem docker utilizada
Para a criação da imagem docker utilizada, é necessário utilizar o comando docker build.
O comando docker build le arquivo DockerFile e cria uma imagem seguinto os passos listados no arquivo.
No caso do arquivo DockerFile, existem várias bibliotecas python que deve ser instaladas, então o arquivo requirements.txt contem a lista dessas bibliotecas, no caso de alguma mudança nas versões ou mesma  adição de uma nova biblioteca, o arquivo requirements.txt pode ser facilmente alterado.
docker build -t NOME_DA_IMAGEM .  , com o nome da imagem - pysark-3.2.0-deltalake
O comando deve ser executado na mesma pasta do arquivo Dockerfile 


# Utilização do docker compose
Para a execução do ambiente, executar o comando docker compose up -d, na pasta pyspark.
O comando docker compose executa todos os container listados no arquivo docker-compose.yml, onde os container estão numa mesma rede.
 Após a execução do comando docker compose up -d, executar o comando docker ps -a, para verificar o correto funcionamento do container.

 # Utilização do ambiente.
 Abra uma janela do seu navegador de preferencia e digite localhost:8888 , o ambiente jupyter lab será aberto no navegador, dando acesso ao cluster pyspark .
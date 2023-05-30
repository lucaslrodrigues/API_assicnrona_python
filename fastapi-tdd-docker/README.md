##Para executar a api
uvicorn app.main:app --reload

# Tomando nota

## Variaveis de ambiente
As variaveis de ambiente não são case sensitive.Uma variavel de ambiente declarada com "enviroment" no **/app/config** pode ser declarada com "ENVIROMENT"

## Assincronismo
O fast api possibilita a utilização de funções assíncronas com a palavra chave "**async**" na assinatura da função.
<br>

## Docs
Desinstalar ambiente poetry: https://stackoverflow.com/questions/70064449/how-to-rebuild-poetry-environment-from-scratch-and-force-reinstall-everything
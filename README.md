# eris
O bot pessoal e privado do servidor [Cosmic ✨](https://discord.gg/SsfvNvNEZR).

## Rodando
Recomendo que não crie sua própria instância do bot para uso pessoal, este repositório foi criado com intenções educacionais.

**Nota:** É necessário ter o [PostgreSQL](https://www.postgresql.org/) e o [Redis](https://redis.io/) instalados e configurados.

1. Configure um ambiente virtual.
```bash
# criando o ambiente virtual
python -m venv venv
# ativando o ambiente virtual
source venv/bin/activate
# instalando dependências
pip install -r requirements.txt
```
2. Crie o banco de dados no PostgreSQL.
```sql
CREATE ROLE eris WITH LOGIN PASSWORD 'sua_senha';
CREATE DATABASE eris OWNER eris;
```
3. Configurando arquivos.

Crie um arquivo `config.py` dentro da pasta `bot/` e coloque as seguintes informações:
```py
# discord
token = '<token_do_bot>'
prefix = '<prefixo>'

# banco de dados e cache
postgres = 'postgres://eris:<senha>@<host>/eris' # suas informações de cima
redis = 'redis://<host>'
```
4. Configurando o banco de dados.

Para configurar o PostgreSQL, digite `python launcher.py db init` dentro da pasta `bot/`.

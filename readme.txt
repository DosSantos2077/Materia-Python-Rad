Sistema para organizar arquivos pessoais
O banco de dados SQLite guarda o caminho,descrição,ID,ID do Usuario e o estatus(trabalhando:SIM/NÃO) do arquivo.
Se voce nao tem o SQLite instalado em sua maquina rode o arquivo(instalarAqlite), um comando pip será inserido em seo prompt de comando.

A primeira tela faz o login ou cadastra um usuario ainda nao cadastrado

O usuario ao ser cadastrado recebe um id proprio, esse id é usado para consultar, e manipular os registro do banco de dados cadastrados pelo mesmo.

Diferentes usuarios nao podem ver ou manipular registros de outros.

Para deletar ou alterar um registro primeiro deve-se consultar o banco para descobrir o seu id de registro.

Nas telas de alterar/deletar primeiro o espaço para o id do registro deve ser preenchido, após disso o sistema irá ser capaz de achar o registro no banco.

Ao consultar, todos os registros do usuario serão exibidos.
# To do list (backend) - Junto Seguros

Para o desenvolvimento do backend foram utilizadas as seguintes bibliotecas que necessitam de instalação adicional:
- Flask (para criação da api restful)
- flask_cors (necessário para fazer as requisições no frontend feito em reactjs)
- Pyrebase (para utilização do banco de dados firebase do google)

O desenvolvimento do backend é todo em python e utiliza o serviço firebase do google para realizar a persistência de dados, este serviço do google foi escolhido pois seria o melhor para evitar qualquer tipo de problema na hora da validação e correção deste teste. Isso também facilita a execução do backend, assim ele podendo ser executado de qualquer lugar sem precisar da criação de um banco de dados toda vez que fosse utilizado em alguma máquina diferente.

O backend funciona seguindo a estrutura restful, conforme o solicitado. Além disso o backend é capaz de salvar arquivos de log de forma local.

É possível executar esta aplicação em container, existe uma Dockerfile para isso no repositório, além de um script "startContainer.sh" para buildar e executar o container.

### Instalação

Para dar funcionalidade a API, é necessário possuir instalada a versão 3.8 do python. Para as dependências é somente necessário instalar via pip utilizando o arquivo "requirements.txt", neste arquivo estão listadas todas as dependências, isso pode ser feito através do comando "python -m pip install requirements.txt". Caso esteja em ambiente linux é necessário somente executar "chmod +x setup.sh && ./setup.sh". O script setup.sh foi desenvolvido para ambientes que utilizam apt-get como seu gerenciador de pacotes.

A aplicação pode funcionar também em containers, neste caso em um container Docker, para isso é necessário subir um container com a Dockerfile presente no projeto.

### Métodos da API

**Caso ocorra algum erro durante a requisição, todos os métodos irão retornar 500 juntamente com o erro ocorrido, caso contrário retornará 200 junto com o solicitado**

##### Home - GET
/

"Raíz" da api, onde é possível visualizar uma mensagem se a api está sendo executada ou não e se a conexão com o banco de dados esta funcional

##### Criação de uma nova tarefa para um usuário - POST
/tarefas/nova/idUsuario&tarefa

Cria uma nova tarefa para um usuário, retorna um "OK" para informar que tudo ocorreu do jeito que deveria ser

idUsuário = id do usuário para qual a tarefa será salva

tarefa = descrição da tarefa

##### Seleção de todas as tarefas de um usuário - GET
/tarefas/todas/idUsuario

Seleciona todas as tarefas de um respectivo usuário, retorna um json possuindo todas as tarefas dele

idUsuario = id do usuário que terá suas tarefas consultadas

##### Seleção de todas as tarefas concluídas de um usuário - GET
/tarefas/todasConcluidas/idUsuario

Seleciona todas as tarefas concluídas de um respectivo usuário, retornando um json com elas

idUsuario = id do usuário que terá suas tarefas concluídas consultadas

##### Exclusão de uma tarefa de um determinado usuário - DELETE
/tarefas/deleta/idUsuario&idTarefa

Deleta uma determinada tarefa de um determinado usuário, retorna "OK" caso a solicitação ocorra bem

idUsuario = id do usuário que terá sua tarefa deletada

idTarefa = id da tarefa a ser deletada

##### Marcação de uma tarefa como concluída - PUT
/tarefas/conclui/idUsuario&idTarefa

Atualiza como concluída uma determinada tarefa de um determinado usuário, retorna "OK" caso a solicitação ocorra bem

idUsuario = id do usuário que terá sua tarefa maracada como concluída

idTarefa = id da tarefa a ser marcada como concluída

##### Criação de um novo usuário - POST
/usuario/novo/email&senha

Cria um novo usuário

email = endereço de e-mail do usuário

senha = senha provida pelo usuário para acessar a lista

##### Autenticação de um usuário - GET
/usuario/autentica/email&senha

Autentica um usuário já existente

email = endereço de e-mail do usuário

senha = senha provida pelo usuário para acessar a lista

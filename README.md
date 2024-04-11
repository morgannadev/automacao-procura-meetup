# Descrição do projeto
Neste projeto, vamos criar uma automação RPA com Python e utilizando as ferramentas da BotCity que realizará consulta de meetups de comunidades no site meetup.com de acordo com alguns parâmetros, como tecnologia, distância e local.

# Preparar o ambiente
Para executar este projeto, você deverá fazer a etapa de [pré-requisitos desta documentação](https://documentation.botcity.dev/pt/getting-started/prerequisites/), que basicamente são os itens abaixo.

## Pré-requisitos:
- [Conta BotCity](https://developers.botcity.dev/app/signup);
- [BotCity Studio SDK](https://documentation.botcity.dev/pt/getting-started/botcity-studio-sdk/);
- [Python 3.7 ou superior](https://www.python.org/downloads/);
- Ter uma IDE instalada, por exemplo: [Visual Studio Code](https://code.visualstudio.com/download) ou [PyCharm](https://www.jetbrains.com/pycharm/download/).

Ao instalar o BotCity Studio SDK, caso aconteça algum problema, você pode usar a ferramenta de diagnóstico para validar o que pode ter acontecido. Para acessar essa ferramenta, verifique [este link](https://documentation.botcity.dev/pt/getting-started/botcity-studio-sdk/#ferramenta-de-diagnostico) da documentação.

# Antes de executar
Atenção aos passos que deve seguir após fazer o fork e clone do projeto em seu computador.

## 01. Crie ambiente virtual (opcional)
Você pode utilizar ambiente virtual com o Python, se preferir. E para criá-lo, execute o seguinte comando:
```
python -m venv venv
```

Após a criação, é necessário ativá-lo. Para isso, execute o comando abaixo:
```
venv\Scripts\activate
```

## 02. Instale as dependências do `requirements.txt`
Para fazer a instalação das dependências do projeto, você deve executar no terminal da sua IDE o comando abaixo, a partir da pasta do projeto:
```
pip install --upgrade -r requirements.txt
```

## 03. Valide permissionamento
Para executar no seu computador ou máquina virtual, garanta que você tem permissão para rodar scripts, códigos etc.

## 04. Criar as credenciais
No código, fazemos o login no site meetup.com com as credenciais salvas com segurança pelo Orquestrador. Para fazer essa configuração, siga [o passo a passo da documentação](https://documentation.botcity.dev/pt/maestro/features/credentials/). Caso mude o nome das credenciais, ajuste também no código:
```
    # busca as credenciais
    credencial_email = maestro.get_credential(label="login_meetup", key="email")
    credencial_senha = maestro.get_credential(label="login_meetup", key="senha")
```

# Para executar local
Se você quiser testar primeiramente no seu computador ou máquina virtual, você deverá:

## 01. Comente os códigos que usam o `execution`
Quando estamos executando o robô localmente, não temos uma tarefa criada. Sendo assim, precisamos comentar os códigos que tenham relação com isso para evitar erros. Identifique no código as chamadas pela instância do maestro com `execution`.

## 02. Adicione a chamada de login no Orquestrador
Como você irá utilizar a parte de buscar as credenciais no Orquestrador, será necessário adicionar o seguinte código para o login:
```
maestro.login(
    server="https://developers.botcity.dev", 
    login="<LOGIN>",
    key="<KEY>"
)
```

Siga [essa parte da documentação](https://documentation.botcity.dev/pt/maestro/maestro-sdk/setup/#utilizando-as-informacoes-do-workspace) para verificar como saber as informações de login e key.

## 03. Execute o robô
Você pode executar clicando no botão de play ou de execução da sua IDE favorita, ou ainda executar o comando abaixo no seu terminal:
```
python bot.py
```

# Para executar no BotCity Orquestrador
Quando estamos executando o robô no Orquestrador, a tarefa será criada, então não precisamos deixar os códigos do item anterior comentados. Tire os comentários para que os códigos possam ser executados corretamente.

Lembre-se de seguir as orientações da [documentação](https://documentation.botcity.dev/pt/tutorials/orchestrating-your-automation/) para fazer o deploy da sua automação no Orquestrador e executar com apoio do Runner.

# Próximos passos
Há diversas possibilidades de melhorias neste projeto e deixo à disponibilidade da comunidade para explorarmos essas melhorias e implementarmos. Algumas sugestões:
- Verificar se há necessidade de refatorar o código;
- Enviar as informações dos eventos encontrados por [e-mail](https://documentation.botcity.dev/pt/plugins/email/) ou ainda por [alertas](https://documentation.botcity.dev/pt/maestro/features/alerts/);
- Entre outros.

Fiquem à vontade de mandar sugestões e correções pelas issues do projeto.

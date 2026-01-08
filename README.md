# Sistema-de-Cadastro-e-Cat-logo-de-Jogos
Sistema de cadastro de jogos com foco em modelagem de dados. Atuei como DBA, estruturando banco SQLite, definindo tipos de dados, regras de integridade e evitando duplicidades. Integrei a API RAWG, complementei dados manualmente e publiquei tudo via Flask em aplicação web funcional.


🎮 Edu Games – Sistema de Cadastro e Catálogo de Jogos
📌 Descrição do Projeto

Este projeto consiste no desenvolvimento de um site de cadastro e exibição de jogos digitais, onde atuei como DBA (Database Administrator) e desenvolvedor da aplicação.

O sistema permite o cadastro, armazenamento e visualização de informações de jogos como nome, preço, nota, data de lançamento, gênero e imagem, além da importação de dados externos através de uma API pública de games.

👤 Meu Papel no Projeto

Neste projeto, atuei principalmente como DBA, sendo responsável por:

Modelagem do banco de dados

Definição de tipos de dados

Criação de regras para integridade dos dados

Prevenção de duplicatas

Validação das informações antes da persistência

Integração entre banco de dados e aplicação web

Também participei do desenvolvimento da aplicação web utilizando Python e Flask.

🛠️ Tecnologias Utilizadas

Python

Flask

SQLite

Jinja2 (Templates HTML)

HTML5 e CSS3

API RAWG (Games Database API)

🌐 Integração com API Externa (RAWG)

Foi utilizada a API RAWG, uma API pública de jogos, para importação inicial dos dados.

Limitação da API

A API fornecia apenas algumas informações básicas, como:

Nome do jogo

Imagem

Devido a essa limitação, foi necessário realizar uma modelagem de dados própria, complementando manualmente as informações que não eram entregues pela API, como:

Preço

Nota

Gênero

Data de lançamento

🗃️ Modelagem do Banco de Dados

Foi utilizado o SQLite, por ser leve, simples e ideal para projetos de pequeno e médio porte.

Estrutura da Tabela jogos
Campo	Tipo	Descrição
id	INTEGER	Chave primária
nome	TEXT	Nome do jogo
preco	REAL	Preço do jogo
imagem	TEXT	URL da imagem
genero	TEXT	Gênero do jogo
nota	REAL	Nota do jogo
lancamento	TEXT	Data de lançamento
🔒 Regras e Validações (Visão DBA)

Durante o desenvolvimento, foram aplicadas boas práticas de banco de dados:

🔁 Verificação de duplicatas para evitar jogos repetidos

🚫 Regras de bloqueio para impedir inserções inválidas

✔ Validação de campos obrigatórios

🧠 Tipagem correta dos dados (REAL, TEXT, INTEGER)

🧪 Testes de integridade antes da exibição no site

🚀 Aplicação Web

A aplicação foi desenvolvida com Flask, responsável por:

Gerenciar rotas

Receber dados via formulários HTML

Persistir dados no banco SQLite

Exibir os jogos cadastrados dinamicamente no site

Os dados são renderizados utilizando Jinja2, permitindo:

Exibição condicional (ex: jogos grátis)

Formatação de valores monetários

Integração direta com o banco de dados

📈 Resultado Final

Ao final do projeto, os dados foram:

Corretamente modelados

Armazenados de forma segura no banco

Validados

Exibidos dinamicamente no site

O sistema funciona como um catálogo completo de jogos, simulando um ambiente real de administração de dados.

🧠 Conclusão

Este projeto proporcionou uma excelente experiência prática como DBA, permitindo aplicar conceitos reais de:

Modelagem de dados

Integridade de banco

Integração com APIs

Persistência de dados

Comunicação entre back-end e front-end

Foi uma jornada muito enriquecedora, unindo desenvolvimento web e administração de banco de dados, reforçando na prática o papel fundamental de um DBA em sistemas reais.

# login_security
Cadastro de Usuários
O sistema permite o cadastro simples de usuários com os seguintes dados:

Nome de usuário: Identificador único para o usuário.
Número de telefone: Para envio de mensagens via WhatsApp (apenas números, com 11 dígitos).
E-mail: Para armazenar dados de contato.
Senha: Para autenticação do usuário no sistema.
Durante o cadastro, o número de telefone inserido é verificado e formatado corretamente antes de ser registrado. Após o cadastro, o sistema envia automaticamente uma mensagem de boas-vindas para o número informado via WhatsApp Web.

Funcionalidades de Cadastro:
Criação de conta: O usuário fornece seu nome de usuário, número de telefone, e-mail e senha.
Validação de número de telefone: O número de telefone deve conter apenas dígitos e ter 11 caracteres (formato esperado para o Brasil).
Armazenamento em memória: O banco de dados simples (em memória) armazena os dados dos usuários para uso posterior.
Mensagem de boas-vindas: Assim que a conta é criada, o usuário recebe uma mensagem automática no WhatsApp.

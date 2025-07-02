# 🤫 GossipBot — Bot de Mensagens Anônimas para Discord

**GossipBot** é um bot simples e leve em Python que permite que usuários enviem mensagens **totalmente anônimas** para um canal do Discord. Nenhum administrador, moderador ou log pode rastrear quem enviou.

---

## ✨ Funcionalidades

- 💬 Slash commands modernos (`/enviar`, `/config`)
- 🕵️ Total anonimato (sem log de autor, sem ID, sem rastreio)
- 🎨 Mensagens exibidas com embeds estilizados
- 🔐 Confirmação privada (ephemeral) ao remetente
- 📁 Logs de manutenção (sem conteúdo ou autores)
- ⚙️ Canal configurável pelos administradores

---

## 📦 Tecnologias Utilizadas

- Python 3.9+
- [discord.py 2.0+](https://discordpy.readthedocs.io/en/stable/)
- Slash Commands com `bot.tree.command`
- [python-dotenv](https://pypi.org/project/python-dotenv/)
- Sistema de logging nativo com `logging`

---

## 🗂️ Estrutura do Projeto

GossipBot/
├── main.py # Código principal com os comandos slash
├── config.py # Carregamento das variáveis de ambiente
├── .env # Configurações sensíveis (não subir para o Git)
├── utils/
│ └── logger.py # Sistema de logging
├── gossip.log # Arquivo de log gerado automaticamente
├── requirements.txt # Dependências do projeto


---

## 🚀 Como Rodar

### 1. Clone o repositório
git clone https://github.com/seu-usuario/gossip.git
cd gossip

2. Instale as dependências
pip install -r requirements.txt

3. Configure seu .env
Crie um arquivo .env na raiz com o seguinte conteúdo:

TOKEN=seu_token_do_discord
DEFAULT_CHANNEL=123456789012345678  #ID do canal para onde as mensagens anônimas serão enviadas
LOG_LEVEL=INFO

    ⚠️ Importante: nunca suba seu .env para o GitHub!

4. Inicie o bot
python main.py

## 💬 Comandos Slash Disponíveis
/enviar [mensagem]

Envia uma mensagem anônima para o canal padrão. O remetente receberá uma confirmação privada.

/config [canal] (somente admins)

Define o canal padrão para onde as mensagens anônimas serão enviadas.

## 🧾 Exemplo de Log
2025-07-02 18:42:01 INFO     Mensagem anônima enviada para o canal #fofocas
2025-07-02 18:44:15 INFO     Canal padrão atualizado para #confissoes (123456789012345678)

Nenhuma mensagem nem autor é logado. Apenas ações administrativas e de saúde do bot.

## 🛡️ Segurança e Privacidade

✅ Não coleta nem armazena nenhuma identificação de usuários

✅ Logs não contêm conteúdo sensível

✅ As mensagens são enviadas pelo bot, e não reenviadas (sem rastros)

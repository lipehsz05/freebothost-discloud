<div align="center">
  <h1>🤖 Guia Completo de Hospedagem de Bots</h1>
  <h2>📚 Discloud Hosting Guide</h2>
  <h3>🚀 Deploy Gratuito de Bots</h3>
</div>

<br>

<div align="center">
  <img src="https://img.shields.io/badge/Discloud-Hosting-00D9FF?style=for-the-badge&logo=cloudflare&logoColor=white" alt="Discloud Hosting" />
  <img src="https://img.shields.io/badge/Free-100MB-00FF88?style=for-the-badge&logo=github&logoColor=white" alt="Free 100MB" />
  <img src="https://img.shields.io/badge/Bots-Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord Bots" />
</div>

---

## 📖 Sobre Este Guia

Descobri recentemente a **[Discloud](https://discloud.com/)** e achei muito legal para hospedar bots gratuitamente! Decidi criar este guia para compartilhar como funciona, já que é uma plataforma brasileira bem interessante.

<p align="center">
  <a href="https://discloud.com/">
    <img src="https://raw.githubusercontent.com/discloud/discloud/main/assets/logo.png" alt="Discloud Logo" width="50" height="50"/>
  </a>
</p>

### 🤔 Por que usei a Discloud?

- 🆓 **Tem plano gratuito** - 100MB de RAM para testar
- 🇧🇷 **É brasileira** - Suporte em português
- ⚡ **Deploy rápido** - Em poucos segundos
- 🔧 **Interface simples** - Fácil de usar
- 📱 **Tem app mobile** - Prático para gerenciar

---

## 💰 Planos e Preços

### 🆓 **Plano Gratuito**
- **RAM:** 100MB
- **Ideal para:** Bots simples, testes, projetos pessoais
- **Limitações:** Apenas 1 aplicação ativa

### 💎 **Planos Pagos** (a partir de R$ 1,99/mês)
- **RAM:** 256MB, 512MB, 1GB ou mais
- **Ideal para:** Bots complexos, múltiplas aplicações
- **Vantagens:** Sem limitações, suporte prioritário

> 💡 **Dica:** Eu comecei com o plano gratuito para testar meus bots. Se precisar de mais recursos, tem planos a partir de R$ 1,99/mês.

---

## 🚀 Passo a Passo Completo

### 📋 **Passo 1: Preparação**

Antes de começar, você precisa ter:

- [x] **Conta na Discloud** - [Crie aqui](https://discloud.com/)
- [x] **Bot do Discord criado** - [Guia oficial](https://discord.com/developers/applications)
- [x] **Código do seu bot** - Pode ser JavaScript, Python, etc.
- [x] **Token do bot** - Obtido no Discord Developer Portal

> 💭 **Minha experiência:** Foi bem simples criar a conta e começar a usar!

### 🔧 **Passo 2: Estrutura do Projeto**

Organize seu projeto assim:

```
meu-bot/
├── index.js          # Arquivo principal (ou main.py)
├── package.json      # Dependências (Node.js)
├── discloud.config   # Configuração da Discloud
└── README.md
```

### ⚙️ **Passo 3: Configuração (discloud.config)**

Crie um arquivo `discloud.config` na raiz do seu projeto:

```json
{
  "MAIN": "index.js",
  "TYPE": "bot",
  "RAM": 100,
  "VERSION": "18.x"
}
```

**Explicação dos parâmetros:**
- `MAIN`: Nome do arquivo principal do seu bot
- `TYPE`: Tipo de aplicação (`bot`, `site`, `api`)
- `RAM`: Quantidade de RAM em MB (100 para plano gratuito)
- `VERSION`: Versão do Node.js

### 📦 **Passo 4: Dependências**

#### Para Bots JavaScript/Node.js:
```json
// package.json
{
  "name": "meu-bot",
  "version": "1.0.0",
  "main": "index.js",
  "dependencies": {
    "discord.js": "^14.0.0"
  }
}
```

#### Para Bots Python:
```txt
# requirements.txt
discord.py>=2.0.0
```

### 🚀 **Passo 5: Deploy - Método 1 (Interface Web)**

1. **Acesse** [discloud.com](https://discloud.com/) e faça login
2. **Clique** em "Upload App" ou "Nova Aplicação"
3. **Selecione** seu arquivo ZIP (compacte toda a pasta do bot)
4. **Configure** as variáveis de ambiente (se necessário):
   - `TOKEN`: Seu token do bot do Discord
   - Outras variáveis que seu bot precise
5. **Clique** em "Deploy" e aguarde alguns segundos
6. **Pronto!** Seu bot estará online! 🎉

> 🎯 **Funcionou perfeitamente:** Meus bots ficaram online em menos de 30 segundos!

### 💻 **Passo 5: Deploy - Método 2 (CLI)**

Se preferir usar linha de comando:

```bash
# 1. Instalar CLI da Discloud
npm install -g discloud-cli

# 2. Fazer login
discloud login

# 3. Navegar até a pasta do seu bot
cd meu-bot

# 4. Fazer deploy
discloud upload
```

### 🧩 **Passo 5: Deploy - Método 3 (VSCode)**

Para quem usa Visual Studio Code:

1. **Instale** a extensão "Discloud" no VSCode
2. **Configure** seu token da Discloud
3. **Abra** a pasta do seu bot
4. **Clique** com botão direito no projeto
5. **Selecione** "Deploy to Discloud"

---

## 🛠️ Exemplos Práticos

### 🤖 **Bot Básico em JavaScript**

```javascript
// index.js
const { Client, GatewayIntentBits } = require('discord.js');

const client = new Client({
    intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages]
});

client.once('ready', () => {
    console.log(`✅ Bot ${client.user.tag} está online!`);
    console.log(`📊 Servindo ${client.guilds.cache.size} servidores`);
});

client.on('messageCreate', message => {
    if (message.content === '!ping') {
        message.reply('🏓 Pong!');
    }
    
    if (message.content === '!info') {
        message.reply(`🤖 Bot hospedado na Discloud!\n📊 Uptime: ${client.uptime}ms`);
    }
});

// Use variável de ambiente para o token
client.login(process.env.TOKEN);
```

### 🐍 **Bot Básico em Python**

```python
# main.py
import discord
from discord.ext import commands
import os

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'✅ {bot.user} está online!')
    print(f'📊 Servindo {len(bot.guilds)} servidores')

@bot.command()
async def ping(ctx):
    await ctx.send('🏓 Pong!')

@bot.command()
async def info(ctx):
    await ctx.send('🤖 Bot hospedado na Discloud!')

# Use variável de ambiente para o token
bot.run(os.getenv('TOKEN'))
```

---

## 🔗 Integração com GitHub

### 🔄 **Deploy Automático**

Para ter deploy automático sempre que você fizer push:

1. **Conecte** seu repositório GitHub na Discloud
2. **Configure** webhook para deploy automático
3. **Faça push** e seu bot será atualizado automaticamente!

```yaml
# .github/workflows/discloud.yml
name: Deploy to Discloud
on:
  push:
    branches: [ main ]
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to Discloud
        run: discloud upload
```

---

## 📊 Meus Bots em Produção

<div align="center">

### 🤖 **Bots Hospedados na Discloud**

[![Bot Pagamentos PushinPay](https://img.shields.io/badge/Bot%20Pagamentos%20PushinPay-4%20⭐-5865F2?style=for-the-badge&logo=telegram&logoColor=white)](https://github.com/lipehsz05/bot-pagamentos-telegram-pushinpay)
[![Bot Pagamentos Mercado Pago](https://img.shields.io/badge/Bot%20Pagamentos%20Mercado%20Pago-11%20⭐-00D9FF?style=for-the-badge&logo=telegram&logoColor=white)](https://github.com/lipehsz05/bot-pagamentos-telegram)

</div>

### 📝 **Sobre os Bots:**

**🤖 Bot Pagamentos PushinPay** - [4 ⭐](https://github.com/lipehsz05/bot-pagamentos-telegram-pushinpay)
- Automação de pagamentos via PIX
- Controle de acesso a grupos VIP
- Banco de dados SQLite integrado
- Expulsão automática de usuários expirados

**🤖 Bot Pagamentos Mercado Pago** - [11 ⭐](https://github.com/lipehsz05/bot-pagamentos-telegram)
- Integração com Mercado Pago
- Envio automático de produtos digitais
- Gerenciamento de produtos
- Notificações de pagamento

---

## ❓ Dúvidas Frequentes

### **Q: Posso hospedar mais de um bot no plano gratuito?**
**R:** No plano gratuito, você pode ter apenas 1 aplicação ativa por vez. Para múltiplos bots, considere os planos pagos.

### **Q: Meu bot está consumindo muita RAM, o que fazer?**
**R:** Otimize seu código ou faça upgrade para um plano com mais RAM (a partir de R$ 1,99/mês).

### **Q: Como faço para atualizar meu bot?**
**R:** Simples! Faça upload do novo arquivo ZIP ou use o deploy automático via GitHub.

### **Q: A Discloud é confiável?**
**R:** Sim! É uma plataforma brasileira estabelecida, com suporte ativo e comunidade grande.

---

## 🆘 Suporte e Recursos

### 📚 **Documentação Oficial**
- [Discloud Docs](https://docs.discloud.com/) - Documentação completa
- [FAQ](https://docs.discloud.com/faq) - Perguntas frequentes
- [API](https://docs.discloud.com/api) - Documentação da API

### 🎯 **Links Úteis**
- [Discord da Discloud](https://discord.gg/discloud) - Comunidade e suporte
- [Status da Discloud](https://status.discloud.com/) - Status dos serviços
- [GitHub da Discloud](https://github.com/discloud) - Projetos open-source

### 💬 **Precisa de Ajuda?**
- **Discord:** Entre no servidor da Discloud
- **Email:** Suporte via ticket
- **Instagram:** [@discloud](https://instagram.com/discloud)

---

## 🌐 Contato

<div align="center">

[![Instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/lipehsz)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/lipehsz)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:ftsu2570@gmail.com)

</div>

---

<div align="center">
  
  ![Footer](https://capsule-render.vercel.app/api?type=waving&color=0:0066cc,100:0099ff&height=65&section=footer)
  
  **"Hospedagem gratuita para todos os desenvolvedores"** 🚀
  
  *Feito com ❤️ para a comunidade brasileira de desenvolvedores*
  
</div>

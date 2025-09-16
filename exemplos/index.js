const { Client, GatewayIntentBits } = require('discord.js');

const client = new Client({
    intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages]
});

client.once('ready', () => {
    console.log(`✅ Bot ${client.user.tag} está online!`);
    console.log(`📊 Servindo ${client.guilds.cache.size} servidores`);
    console.log(`🤖 Hospedado na Discloud - Plano Gratuito`);
});

client.on('messageCreate', message => {
    // Comando !ping
    if (message.content === '!ping') {
        message.reply('🏓 Pong!');
    }
    
    // Comando !info
    if (message.content === '!info') {
        const embed = {
            color: 0x00D9FF,
            title: '🤖 Informações do Bot',
            description: 'Bot hospedado gratuitamente na Discloud!',
            fields: [
                {
                    name: '📊 Uptime',
                    value: `${Math.floor(client.uptime / 1000)} segundos`,
                    inline: true
                },
                {
                    name: '🏠 Servidores',
                    value: `${client.guilds.cache.size}`,
                    inline: true
                },
                {
                    name: '👥 Usuários',
                    value: `${client.users.cache.size}`,
                    inline: true
                }
            ],
            footer: {
                text: 'Hospedado na Discloud - 100MB RAM Gratuito'
            }
        };
        message.reply({ embeds: [embed] });
    }
    
    // Comando !help
    if (message.content === '!help') {
        const embed = {
            color: 0x00FF88,
            title: '📚 Comandos Disponíveis',
            description: 'Lista de comandos do bot:',
            fields: [
                {
                    name: '!ping',
                    value: 'Testa a latência do bot',
                    inline: false
                },
                {
                    name: '!info',
                    value: 'Mostra informações do bot',
                    inline: false
                },
                {
                    name: '!help',
                    value: 'Mostra esta lista de comandos',
                    inline: false
                }
            ],
            footer: {
                text: 'Bot hospedado gratuitamente na Discloud'
            }
        };
        message.reply({ embeds: [embed] });
    }
});

// Tratamento de erros
client.on('error', error => {
    console.error('❌ Erro no bot:', error);
});

process.on('unhandledRejection', error => {
    console.error('❌ Erro não tratado:', error);
});

// Use variável de ambiente para o token
client.login(process.env.TOKEN);

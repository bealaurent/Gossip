import discord
from discord import app_commands
from discord.ext import commands
from config import TOKEN, DEFAULT_CHANNEL
from utils.logger import logger

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)
default_channels = {}

@bot.event
async def on_ready():
    await bot.tree.sync()
    logger.info(f"Bot online como {bot.user}")
    print(f"✅ {bot.user} conectado e comandos sincronizados.")

@bot.tree.command(name="enviar", description="Envie aqui sua fofoca.")
@app_commands.describe(mensagem="Escreva aqui sua mensagem")
async def anonimo_enviar(interaction: discord.Interaction, mensagem: str):
    try:
        guild_id = interaction.guild.id
        channel_id = default_channels.get(guild_id)

        if not channel_id:
            await interaction.response.send_message("❌ Nenhum canal foi configurado para este servidor. Use `/config`.", ephemeral=True)
            return

        channel = bot.get_channel(channel_id)
        if not channel:
            await interaction.response.send_message("❌ Canal configurado não encontrado. Verifique se ele ainda existe.", ephemeral=True)
            return

        embed = discord.Embed(
            title="📩 Correio Eletrônico",
            description=mensagem,
            color=discord.Color.blurple()
        )

        await channel.send(embed=embed)
        logger.info(f"Mensagem anônima enviada no servidor {interaction.guild.name}, canal {channel.name}")
        await interaction.response.send_message("✅ Sua mensagem foi enviada anonimamente!", ephemeral=True)

    except Exception as e:
        logger.error(f"Erro ao enviar mensagem anônima: {e}")
        await interaction.response.send_message("❌ Ocorreu um erro ao enviar sua mensagem.", ephemeral=True)


@bot.tree.command(name="config", description="Configure o canal padrão para mensagens anônimas (somente admins).")
@app_commands.describe(canal="Canal onde as mensagens anônimas devem ser enviadas")
@app_commands.checks.has_permissions(administrator=True)
async def config(interaction: discord.Interaction, canal: discord.TextChannel):
    default_channels[interaction.guild.id] = canal.id
    logger.info(f"Canal padrão do servidor {interaction.guild.name} configurado para {canal.name} ({canal.id}) por {interaction.user}")
    await interaction.response.send_message(f"✅ Canal configurado para {canal.mention}", ephemeral=True)


@config.error
async def config_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message("❌ Você não tem permissão para isso.", ephemeral=True)
    else:
        logger.error(f"Erro inesperado no comando /config: {error}")
        await interaction.response.send_message("❌ Ocorreu um erro inesperado.", ephemeral=True)

@bot.tree.command(name="ajuda", description="Saiba como usar o bot e enviar mensagens anônimas.")
async def ajuda(interaction: discord.Interaction):
    embed = discord.Embed(
        title="❓ Como funciona o bot?",
        description=(
            "Este bot permite que você envie **mensagens anônimas** para um canal específico do servidor.\n\n"
            "📝 **Para enviar uma mensagem anônima:**\n"
            "Use o comando `/enviar` seguido da sua mensagem.\n"
            "Exemplo: `/enviar O fulano tá pegando o ciclano!`\n\n"
            "📨 A mensagem será enviada **anonimamente** no canal configurado, sem mostrar seu nome ou avatar.\n\n"
            "⚙️ **Para admins:**\n"
            "Use `/config` para definir o canal onde as mensagens anônimas devem ser postadas.\n"
            "Exemplo: `/config #fofocas`\n\n"
            "🔒 **Privacidade:**\n"
            "Nenhum log de autor é salvo. As mensagens são totalmente anônimas."
        ),
        color=discord.Color.green()
    )
    await interaction.response.send_message(embed=embed)


bot.run(TOKEN)
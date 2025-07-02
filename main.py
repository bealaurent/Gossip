import discord
from discord import app_commands
from config import TOKEN, DEFAULT_CHANNEL
from utils.logger import logger

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

default_channel_id = DEFAULT_CHANNEL

@bot.event
async def on_ready():
    await tree.sync()
    logger.info(f"Bot online como {bot.user}")
    print(f"✅ {bot.user} conectado e comandos sincronizados.")

@tree.command(name="enviar", description="Envie aqui sua fofoca.")
@app_commands.describe(mensagem="Escreva aqui sua mensagem")
async def anonimo_enviar(interaction: discord.Interaction, mensagem: str):
    global default_channel_id

    try:
        channel = bot.get_channel(default_channel_id)
        if not channel:
            await interaction.response.send_message("❌ Canal padrão não configurado corretamente.", ephemeral=True)
            return

        embed = discord.Embed(
            title="📩 Mensagem Anônima",
            description=mensagem,
            color=discord.Color.blurple()
        )

        await channel.send(embed=embed)
        logger.info(f"Mensagem anônima enviada para o canal {channel.name}")
        await interaction.response.send_message("✅ Sua mensagem foi enviada anonimamente!", ephemeral=True)

    except Exception as e:
        logger.error(f"Erro ao enviar mensagem anônima: {e}")
        await interaction.response.send_message("❌ Ocorreu um erro ao enviar sua mensagem.", ephemeral=True)

@tree.command(name="config_canal", description="Configure o canal padrão para mensagens anônimas (somente admins).")
@app_commands.describe(canal="Canal onde as mensagens anônimas devem ser enviadas")
@app_commands.checks.has_permissions(administrator=True)
async def anonimo_config(interaction: discord.Interaction, canal: discord.TextChannel):
    global default_channel_id
    default_channel_id = canal.id
    logger.info(f"Canal padrão atualizado para {canal.name} ({canal.id}) por {interaction.user}")
    await interaction.response.send_message(f"✅ Canal configurado para {canal.mention}", ephemeral=True)

@anonimo_config.error
async def config_error(interaction: discord.Interaction, error):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message("❌ Você não tem permissão para isso.", ephemeral=True)
    else:
        logger.error(f"Erro inesperado no comando /anonimo_config: {error}")
        await interaction.response.send_message("❌ Ocorreu um erro inesperado.", ephemeral=True)

bot.run(TOKEN)

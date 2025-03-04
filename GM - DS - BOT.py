import discord
import asyncio
import websockets
from discord.ui import View, Button

# 🔧 Настройки
TOKEN = "ВАШ_ТОКЕН_БОТА"  # Токен бота Discord
GUILD_ID = 123456789       # ID сервера Discord
CHAT_CHANNEL_ID = 1122334455  # Канал для общения с сервером
ADMIN_CHANNEL_ID = 2233445566  # Канал для отправки админ-команд
ADMIN_ROLE = "GMod Admin"  # Название роли админов
WEBSOCKET_URI = "ws://127.0.0.1:8765"  # WebSocket сервер GMod

# Интенты
intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)
tree = discord.app_commands.CommandTree(client)

# 🛠️ Функция отправки команды в WebSocket
async def send_to_gmod(command):
    async with websockets.connect(WEBSOCKET_URI) as ws:
        await ws.send(command)

# 📌 Класс кнопок
class AdminPanel(View):
    def __init__(self):
        super().__init__(timeout=None)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        """Проверка, есть ли у пользователя роль администратора"""
        role = discord.utils.get(interaction.user.roles, name=ADMIN_ROLE)
        if not role:
            await interaction.response.send_message("⛔ У вас нет прав!", ephemeral=True)
            return False
        return True

    @discord.ui.button(label="Ban", style=discord.ButtonStyle.danger)
    async def ban_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(AdminCommandModal("ban"))

    @discord.ui.button(label="Kick", style=discord.ButtonStyle.primary)
    async def kick_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(AdminCommandModal("kick"))

    @discord.ui.button(label="Mute", style=discord.ButtonStyle.secondary)
    async def mute_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(AdminCommandModal("mute"))

    @discord.ui.button(label="Gag", style=discord.ButtonStyle.secondary)
    async def gag_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(AdminCommandModal("gag"))

    @discord.ui.button(label="CSay", style=discord.ButtonStyle.success)
    async def csay_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(AdminCommandModal("csay"))

    @discord.ui.button(label="RCON", style=discord.ButtonStyle.danger)
    async def rcon_button(self, interaction: discord.Interaction, button: Button):
        await interaction.response.send_modal(AdminCommandModal("rcon"))

# 📌 Модальное окно для ввода команды
class AdminCommandModal(discord.ui.Modal, title="Выполнение команды"):
    def __init__(self, command_name):
        super().__init__()
        self.command_name = command_name
        self.command_input = discord.ui.TextInput(label="Введите команду", placeholder="Ник / SteamID / Причина...")
        self.add_item(self.command_input)

    async def on_submit(self, interaction: discord.Interaction):
        command = f"!cmd {self.command_name} {self.command_input.value}"
        await send_to_gmod(command)
        await interaction.response.send_message(f"✅ Команда `{command}` отправлена!", ephemeral=True)

@client.event
async def on_ready():
    """Запуск бота"""
    print(f'✅ Бот {client.user} запущен!')
    
    # Проверяем, есть ли уже сообщение с кнопками
    admin_channel = client.get_channel(ADMIN_CHANNEL_ID)
    if admin_channel:
        async for msg in admin_channel.history(limit=10):
            if msg.author == client.user and msg.components:
                return
    
        # Отправляем кнопки
        await admin_channel.send("🎮 **Админ-команды**", view=AdminPanel())

    asyncio.create_task(receive_gmod_messages())

async def receive_gmod_messages():
    """Получение сообщений с сервера GMod"""
    while True:
        try:
            async with websockets.connect(WEBSOCKET_URI) as ws:
                while True:
                    message = await ws.recv()
                    chat_channel = client.get_channel(CHAT_CHANNEL_ID)
                    if chat_channel:
                        await chat_channel.send(f"🎮 {message}")
        except Exception as e:
            print(f"Ошибка WebSocket: {e}")
            await asyncio.sleep(5)

@client.event
async def on_message(message):
    """Отправка сообщений из Discord в GMod"""
    if message.author.bot:
        return

    if message.channel.id == CHAT_CHANNEL_ID:
        async with websockets.connect(WEBSOCKET_URI) as ws:
            await ws.send(f"{message.author.display_name}: {message.content}")

client.run(TOKEN)

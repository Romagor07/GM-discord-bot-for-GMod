# Инструкция / Instruction
- [Русский](https://github.com/Romagor07/GM-discord-bot-for-GMod#%D1%80%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9)
- [English](https://github.com/Romagor07/GM-discord-bot-for-GMod?tab=readme-ov-file#english)
# Русский:
Это мой собственный проект по реализации одной из самых главных и нужных вещей для серверов GMod
Бот который создаст двухстороннее общение между людьми на сервере и людьми в дискорде (ТОЛЬКО ЧАТ)

## Что же входит в этого бота:

- Двустороннее общение между Discord и Garry's Mod
- Админ панель для управления сервером с базовыми командами (бан, кик, мут и т.д.)

## Что же нужно для его работы:

- Сервер Garry's Mod
- [GWSockets](https://github.com/FredyH/GWSockets)
- [ULX](https://steamcommunity.com/sharedfiles/filedetails/?l=russian&id=557962280)
- Python и библиотеки

# Как все настроить:

- Установите питон версии 3.12.2 и выше (``` ОБЯЗАТЕЛЬНО С PIP ```)
- Установите библиотеки данной командой: 
```pip install discord.py websockets asyncio```
- Далее отправляемся в питоновский файл (```GM - DS - BOT.py```) и настраиваем все как написанно ниже:

| Что менять | Где менять | Пример | Рекомендации |
|---------------------------------|------------------------|-------------------------|-------------------------|
| Токен бота Discord | TOKEN = "ВАШ_ТОКЕН_БОТА" | TOKEN = "Mz...your-token" | Можно найти на странице Developer portal |
| ID сервера Discord  | GUILD_ID = 123456789 | GUILD_ID = 987654321 | в режиме разработчика пкм по иконке сервера |
| ID канала для панели управления | CHANNEL_ID = 987654321 | CHANNEL_ID = 1122334455 | в режиме разработчика пкм по каналу |
| Название роли админов | ADMIN_ROLE = "Администратор" | ADMIN_ROLE = "GMod Admin" | найти в настройках Discord сервера
| Адрес WebSocket сервера GMod | WEBSOCKET_URI = "ws://127.0.0.1:8765" | WEBSOCKET_URI = "ws://192.168.1.100:8765" | не менять если на все файлы на 1 серверной машине |

- После настройки файла питона настраиваем файл ```discord-GM.lua```

| Что менять | Где менять | Пример | Рекомендации |
|----------------|------------------------|-------------------------|-------------------------|
| IP WebSocket сервера | socket = GWSockets.createWebSocket("ws://127.0.0.1:8765") | socket = GWSockets.createWebSocket("ws://192.168.1.100:8765") | не менять если на все файлы на 1 серверной машине |
| Название команд ULX  | game.ConsoleCommand("ulx ban " .. target .. " 0\n") | game.ConsoleCommand("sam ban " .. target .. " 0\n") | Менять только при нахождении ошибок |

# Что же мы получаем в итоге?
🔹 Бота который:

🔹 создает панель кнопок в Discord.

🔹 Админы могут нажимать кнопки и вводить данные.

🔹 Бот отправляет команду в WebSocket → GMod выполняет команду.

🔹 Работает с ULX / SAM / RCON командами.

Теперь у вас полноценная панель управления сервером Garry’s Mod в Discord! 🎮🔥


# English:
This is my own project to implement one of the most important and necessary things for GMod servers
A bot that will create two-way communication between people on the server and people in Discord (CHAT ONLY)

## What is included in this bot:

- Two-way communication between Discord and Garry's Mod
- Admin panel for managing the server with basic commands (ban, kick, mute, etc.)

## What is needed for its operation:

- Garry's Mod server
- [GWSockets](https://github.com/FredyH/GWSockets)
- Python and libraries

# How to set everything up:

- Install Python version 3.12.2 and higher (``` WITH PIP MANDATORY ```)
- Install the libraries with this command:

```pip install discord.py websockets asyncio```
- Next, go to the Python file (```GM - DS - BOT.py```) and configure everything as written below:

| What to change | Where to change | Example | Recommendations |
|---------------------------------|-----------------------|-------------------------|-------------------------|
| Discord bot token | TOKEN = "YOUR_BOT_TOKEN" | TOKEN = "Mz...your-token" | Can be found on the Developer portal page |
| Discord server ID | GUILD_ID = 123456789 | GUILD_ID = 987654321 | in developer mode, right-click on the server icon |
| Channel ID for the control panel | CHANNEL_ID = 987654321 | CHANNEL_ID = 1122334455 | in developer mode, right-click on the channel |
| Admin role name | ADMIN_ROLE = "Administrator" | ADMIN_ROLE = "GMod Admin" | find in Discord server settings
| GMod server WebSocket address | WEBSOCKET_URI = "ws://127.0.0.1:8765" | WEBSOCKET_URI = "ws://192.168.1.100:8765" | do not change if for all files on 1 server machine |

- After setting up the python file, set up the ```discord-GM.lua``` file

| What to change | Where to change | Example | Recommendations |
|----------------|------------------------|-------------------------|-------------------------|
| WebSocket server IP | socket = GWSockets.createWebSocket("ws://127.0.0.1:8765") | socket = GWSockets.createWebSocket("ws://192.168.1.100:8765") | do not change if on all files on 1 server machine |
| ULX command name | game.ConsoleCommand("ulx ban " .. target .. " 0\n") | game.ConsoleCommand("sam ban " .. target .. " 0\n") | Change only if errors are found |

# What do we get in the end?
🔹 A bot that:

🔹 creates a button panel in Discord.

🔹 Admins can press buttons and enter data.

🔹 The bot sends a command to WebSocket → GMod executes the command.

🔹 Works with ULX / SAM / RCON commands.

Now you have a full control panel for your Garry's Mod server in Discord! 🎮🔥

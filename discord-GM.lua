util.AddNetworkString("DiscordChat")

local ws = require("gwsockets")

local socket = GWSockets.createWebSocket("ws://127.0.0.1:8765")

local function sendMessageToDiscord(msg)
    if socket and socket:isConnected() then
        socket:send(msg)
    end
end

hook.Add("PlayerSay", "SendToDiscordChat", function(ply, text, teamChat)
    sendMessageToDiscord(ply:Nick() .. ": " .. text)
end)

socket.onMessage = function(msg)
    local args = string.Explode(" ", msg)
    local command = args[1]

    if command == "!chat" then
        local chatMessage = table.concat(args, " ", 2)
        for _, ply in ipairs(player.GetAll()) do
            ply:ChatPrint("[Discord] " .. chatMessage)
        end
    elseif command == "!cmd" then
        local cmd = table.concat(args, " ", 2)
        game.ConsoleCommand("ulx " .. cmd .. "\n")
    end
end

socket.onConnected = function()
    print("[DISCORD] WebSocket подключен")
end

socket.onDisconnected = function()
    print("[DISCORD] WebSocket отключен")
end

socket:open()

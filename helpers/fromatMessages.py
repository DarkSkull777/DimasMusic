from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from utils.Logger import *
from utils.Config import Config

Config = Config()


def getMessage(message, action):
    try:
        ALLOWED_CHAT_TYPES = config.get("ALLOWED_CHAT_TYPES")

        if action == "private-chat":
            send_message = f"**Hai 🎵 {message.chat.first_name if hasattr(message.chat, 'first_name') else 'User'}**"
            send_message = send_message + \
                f"\n\n**[Dimas Music OS]({config.get('BOT_URL')})** is a [Dimasrmdani]({config.get('PARENT_URL')})."
            send_message = send_message + \
                f"\n__Ini dirancang untuk memutar, sesederhana mungkin, musik di grup Anda melalui **obrolan suara baru** yang diperkenalkan oleh Telegram.__"
            send_message = send_message + \
                f"\n\n**Jadi tunggu apa lagi 🌀 tambahkan bot ke grup dan mulai **\n\n**Kode SumberS :** [Repository]({config.get('GITHUB_REPO')})"
            return send_message, getReplyKeyBoard(message, action)

        elif action == "help-msg":
            helpMessage = f"**Dimas Music OS**\n**Source Code :** [Repository]({config.get('GITHUB_REPO')})"
            helpMessage = helpMessage + \
                f"\n\n• **/play nama lagu/link lagu: ** __Mulai sebuah lagu / tambahkan ke antrian.__"
            helpMessage = helpMessage + f"\n• **/skip : ** _Lewati ke lagu berikutnya dalam antrian..__"
            helpMessage = helpMessage + f"\n• **/stop : ** __Hentikan pemutaran.__"
            helpMessage = helpMessage + \
                f"\n• **/refreshadmins : ** __Menyegarkan daftar admin.__"
            helpMessage = helpMessage + \
                f"\n• **/auth : ** __Menambahkan pengguna sebagai balasan pesan sebagai admin.__"
            helpMessage = helpMessage + \
                f"\n• **/unauth : ** __Menghapus pengguna sebagai balasan pesan sebagai admin.__"
            helpMessage = helpMessage + \
                f"\n• **/listadmins : ** __Mencantumkan pengguna yang ditetapkan sebagai admin untuk bot.__"
            helpMessage = helpMessage + \
                f"\n• **/adminmode on|off : ** __Mengaktifkan ini membuat tindakan bot hanya tersedia untuk admin bot.__"
            helpMessage = helpMessage + \
                f"\n• **/loop [2-5]|off : ** __Loop pemutaran [x] kali(x antara 2-5) / Matikan pemutaran loop.__"
            helpMessage = helpMessage + f"\n\n**__Untuk masalah apapun hubungi @xskull7**"
            return helpMessage, getReplyKeyBoard(message, action)

        elif action == "chat-not-allowed":
            send_message = f"**😖 Maaf, obrolan ini belum diizinkan untuk mengakses layanan. Anda selalu dapat memeriksa demo di [Support Group]({config.get('SUPPORT_GROUP')}).**"
            send_message = send_message + \
                f"\n\n**Why ❓**\n- __karena penggunaan yang tinggi, kami telah membatasi penggunaan bot hanya di kami [Support Group]({config.get('SUPPORT_GROUP')}) __"
            send_message = send_message + \
                f"\n- __Bergabung dengan [Support Group]({config.get('SUPPORT_GROUP')}) untuk mengakses bot atau menggunakan bot Anda sendiri __ **Source Code :** [Github]({config.get('GITHUB_REPO')})"

            return send_message, getReplyKeyBoard(message, action)

        elif action == "start-voice-chat":
            send_message = f"**Silakan mulai obrolan suara dan kemudian kirim perintah lagi**"
            send_message = send_message + \
                f"\n**1.** __untuk memulai obrolan grup, Anda dapat menuju ke halaman deskripsi grup Anda.__"
            send_message = send_message + \
                f"\n**2.** __Kemudian ketuk tombol tiga titik di sebelah Bungkam dan Cari memulai Obrolan Suara.__"
            return send_message, getReplyKeyBoard(message, action)

    except Exception as ex:
        logException(f"**__Error : {ex}__**", True)


def getReplyKeyBoard(message, action):
    try:
        if action == "private-chat":
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "➕ Tambahkan ke grup ➕", url=f"{config.get('BOT_URL')}?startgroup=bot"),
                    ],
                    [
                        InlineKeyboardButton(
                            "👥 Support", url=f"{config.get('SUPPORT_GROUP')}"),

                        InlineKeyboardButton(
                            "📔 Kode Saya", url=f"{config.get('GITHUB_REPO')}"),
                    ],

                ]
            )
            return keyboard
        elif action == "chat-not-allowed":
            keyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "🏁 Gunakan Dalam Demo", url=f"{config.get('SUPPORT_GROUP')}"),
                    ],
                    [
                        InlineKeyboardButton(
                            "📔 Source Code", url=f"{config.get('GITHUB_REPO')}"),

                    ],

                ]
            )
            return keyboard
        return None
    except Exception as ex:
        logException(f"**__Error : {ex}__**", True)

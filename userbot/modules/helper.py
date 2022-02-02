""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.helpme$")
async def usit(e):
    await e.edit(
        f"__Hai {DEFAULTUSER} Kalau lu ga Tau cara buat__ **Memerintah** gua **Ketik** `.helpme` Atau `.help` atau Minta **Bantuan** __Ke:__\n"
        f"😑 **Channel support :** [Wiki Channel](t.me/WikiTapiChannel)\n"
        f"😑 **Group Support :** [Wiki Group](t.me/WikiTapiGroup)\n"
        f"😑 **Owner Repo :** [Wiki W](t.me/Hanya_W)\n"
        f"😑 **Repo :** [DIOR-UBOT](https://github.com/Wiki28/Wiki-Userbot)\n\n\n"
        f"__Powered by Wiki W__"
    )



@register(outgoing=True, pattern="^.rvars$")
async def var(m):
    await m.edit(
        f"**Daftar Vars** {DEFAULTUSER}:\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/Wiki28/Wiki-Userbot/Wiki-Userbot/varshelper.txt)")


CMD_HELP.update({
    "helper":
    "`.helpme`\
\nUsage: Bantuan Untuk DIOR-UBOT.\
\n`.rvars`\
\nUsage: Untuk Melihat Beberapa Daftar Vars."
})

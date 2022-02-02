from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.dior(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("😑 `introduce my self...`")
    sleep(2)
    await typew.edit("`kenalin saya Wiki`")
    sleep(2)
    await typew.edit("`bocah tele polos, polos seperti kain kafan kau kelak`")
    sleep(2)
    await typew.edit("`kalau pc, jan pc pas butuh doang babi...`")
    sleep(3)
    await typew.edit("`boleh sih mintol tapi gk ush ngelunjak babi, malah di bantuin seenak jidat kau!`")
    sleep(3)
    await typew.edit("**salken dh**")
# Create by myself @localheart

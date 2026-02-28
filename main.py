# Don't Remove Credit Tg - @VJ_Bots

import os
import re
import sys
import time
import asyncio
import requests

import core as helper
from utils import progress_bar
from vars import API_ID, API_HASH, BOT_TOKEN

from aiohttp import ClientSession
from pyromod import listen

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait


bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


# START
@bot.on_message(filters.command(["start"]))
async def start(bot: Client, m: Message):

    await m.reply_text(
        f"Hello {m.from_user.mention} 👋\n\nSend /upload and upload TXT file."
    )


# STOP
@bot.on_message(filters.command("stop"))
async def restart_handler(_, m):

    await m.reply_text("Stopped 🚦")
    os.execl(sys.executable, sys.executable, *sys.argv)



# UPLOAD
@bot.on_message(filters.command(["upload"]))
async def upload(bot: Client, m: Message):

    editable = await m.reply_text("Send TXT File ⚡")

    input: Message = await bot.listen(editable.chat.id)

    x = await input.download()

    await input.delete(True)

    try:

        with open(x, "r", encoding="utf-8") as f:

            content = f.read().splitlines()

        links = []

        for i in content:

            if "://" in i:

                links.append(i.split("://", 1))

        os.remove(x)

    except:

        await m.reply_text("Invalid file.")

        os.remove(x)

        return


    await editable.edit(

        f"Total Links 🔗 {len(links)}\nSend Start Number (1)"

    )

    input0 = await bot.listen(editable.chat.id)

    count = int(input0.text)

    await input0.delete(True)



    await editable.edit("Send Batch Name")

    input1 = await bot.listen(editable.chat.id)

    batch = input1.text

    await input1.delete(True)



    await editable.edit("Quality? 144/240/360/480/720/1080")

    input2 = await bot.listen(editable.chat.id)

    quality = input2.text

    await input2.delete(True)



    await editable.edit("Send Caption")

    input3 = await bot.listen(editable.chat.id)

    caption_extra = input3.text

    await input3.delete(True)



    await editable.delete()



    for i in range(count - 1, len(links)):

        try:

            url = "https://" + links[i][1]


            # SAFE NAME FIX 🔥

            raw_name = links[i][0]

            name1 = re.sub(r'[^\w\s-]', '', raw_name)

            name1 = re.sub(r'\s+', ' ', name1).strip()

            safe_name = name1.replace(" ", "_")

            name = f"{str(count).zfill(3)}_{safe_name[:60]}"



            if "youtu" in url:

                ytf = f"b[height<={quality}][ext=mp4]/bv[height<={quality}]+ba"

            else:

                ytf = f"b[height<={quality}]/bv[height<={quality}]+ba/b"



            cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'



            Show = (

                f"Downloading...\n\n"

                f"Name » {name}\n"

                f"Quality » {quality}\n"

                f"URL » {url}"

            )

            prog = await m.reply_text(Show)



            res_file = await helper.download_video(

                url,

                cmd,

                name

            )



            await prog.delete(True)



            caption = (

                f"Vid_ID {str(count).zfill(3)}\n"

                f"{name1}\n"

                f"Batch » {batch}\n"

                f"{caption_extra}"

            )



            await helper.send_vid(

                bot,

                m,

                caption,

                res_file,

                None,

                name,

                prog

            )



            os.remove(res_file)



            count += 1



            time.sleep(1)



        except FloodWait as e:

            await asyncio.sleep(e.value)



        except Exception as e:

            await m.reply_text(

                f"Downloading Interrupted\n{e}\nName » {name}\nLink » {url}"

            )



    await m.reply_text("Done Boss 😎")


bot.run()            res = "UN"
    
    

    await editable.edit("Now Enter A Caption to add caption on your uploaded file")
    input3: Message = await bot.listen(editable.chat.id)
    raw_text3 = input3.text
    await input3.delete(True)
    highlighter  = f"️ ⁪⁬⁮⁮⁮"
    if raw_text3 == 'Robin':
        MR = highlighter 
    else:
        MR = raw_text3
   
    await editable.edit("Now send the Thumb url/nEg » https://graph.org/file/ce1723991756e48c35aa1.jpg \n Or if don't want thumbnail send = no")
    input6 = message = await bot.listen(editable.chat.id)
    raw_text6 = input6.text
    await input6.delete(True)
    await editable.delete()

    thumb = input6.text
    if thumb.startswith("http://") or thumb.startswith("https://"):
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")
        thumb = "thumb.jpg"
    else:
        thumb == "no"

    if len(links) == 1:
        count = 1
    else:
        count = int(raw_text)

    try:
        for i in range(count - 1, len(links)):

            V = links[i][1].replace("file/d/","uc?export=download&id=").replace("www.youtube-nocookie.com/embed", "youtu.be").replace("?modestbranding=1", "").replace("/view?usp=sharing","") # .replace("mpd","m3u8")
            url = "https://" + V

            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                        text = await resp.text()
                        url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)

            elif 'videos.classplusapp' in url:
             url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': 'eyJhbGciOiJIUzM4NCIsInR5cCI6IkpXVCJ9.eyJpZCI6MzgzNjkyMTIsIm9yZ0lkIjoyNjA1LCJ0eXBlIjoxLCJtb2JpbGUiOiI5MTcwODI3NzQyODkiLCJuYW1lIjoiQWNlIiwiZW1haWwiOm51bGwsImlzRmlyc3RMb2dpbiI6dHJ1ZSwiZGVmYXVsdExhbmd1YWdlIjpudWxsLCJjb3VudHJ5Q29kZSI6IklOIiwiaXNJbnRlcm5hdGlvbmFsIjowLCJpYXQiOjE2NDMyODE4NzcsImV4cCI6MTY0Mzg4NjY3N30.hM33P2ai6ivdzxPPfm01LAd4JWv-vnrSxGXqvCirCSpUfhhofpeqyeHPxtstXwe0'}).json()['url']

            elif '/master.mpd' in url:
             id =  url.split("/")[-2]
             url =  "https://d26g5bnklkwsh4.cloudfront.net/" + id + "/master.m3u8"

            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{str(count).zfill(3)}) {name1[:60]}'

            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:  
                
                cc = f'**[📽️] Vid_ID:** {str(count).zfill(3)}.** {𝗻𝗮𝗺𝗲𝟭}{MR}.mkv\n**𝔹ᴀᴛᴄʜ** » **{raw_text0}**'
                cc1 = f'**[📁] Pdf_ID:** {str(count).zfill(3)}. {𝗻𝗮𝗺𝗲𝟭}{MR}.pdf \n**𝔹ᴀᴛᴄʜ** » **{raw_text0}**'
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                
                elif ".pdf" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                        count += 1
                        os.remove(f'{name}.pdf')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue
                else:
                    Show = f"**⥥ 🄳🄾🅆🄽🄻🄾🄰🄳🄸🄽🄶⬇️⬇️... »**\n\n**📝Name »** `{name}\n❄Quality » {raw_text2}`\n\n**🔗URL »** `{url}`"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(
                    f"**downloading Interupted **\n{str(e)}\n**Name** » {name}\n**Link** » `{url}`"
                )
                continue

    except Exception as e:
        await m.reply_text(e)
    await m.reply_text("**𝔻ᴏɴᴇ 𝔹ᴏ𝕤𝕤😎**")


bot.run()

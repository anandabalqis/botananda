import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')
@bot.command()
async def ping(ctx):
    await ctx.send(f'Hi! ananda is here how may i assist you {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def mem(ctx):
    with open('C:\\Users\\Ananda Balqis\\Documents\\CODING KODLAND ANANDA\\m2l1_meme\\images2.jpg.jpeg', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

@bot.command()
async def cara_melatih_anak_remaja_untuk_terbiasa_membuang_sampah_pada_tempatnya(ctx):
    await ctx.send(f'''cara melatih anak remaja untuk terbiasa membuang sampah pada tempatnya: 
- perlu nya kesadaran dari diri sendiri tentang kebersihan
- budaya saling mengingatkan
- contoh dari orang dewasa
- kalian bisa mendaur ulang sampah sejenis plastik untuk dijadikan kerajinan tangan
- jika sampah tersebut sejenis sampah organik (yang bisa terurai dalam jangka waktu pendek), kalian bisa mengubah sampah tersebut menjadi pupuk untuk tanaman kalian (contoh sampah: daun)
- gunakanlah produk-produk yang ramah lingkungan dan dapat terurai dengan cepat
- jika punya botol minum, kamu bisa mengurangi limbah botol plastik yang biasanya kamu beli
                   {bot.user} !''')
    
@bot.command()
async def cara_mendaur_ulang_untuk_sampah_anorganik(ctx):
    await ctx.send(f'''cara mendaur ulang sampah anorganik:
- plastik botol: tempat pensil, pot tanaman, kapal selam mainan, dan hiasan gantung
- plastik (kresek): hiasan gantung
- kardus bekas: aquarium mainan, tempat tissue, dan rumah mainan
- kertas bekas: bisa di daur ulang menjadi kertas baru dan bisa juga dibuat menjadi kerajinan rupa seperti rumah-rumahan mini
                    {bot.user} !''')
    
@bot.command()
async def cara_mendaur_ulang_untuk_sampah_organik(ctx):
    await ctx.send(f'''cara mendaur ulang sampah organik:
- Mengumpulkan Sampah. Sampah yang bisa digunakan dan didaur ulang menjadi pupuk kompos adalah sampah organik.
- Proses Pencacahan.
- Proses Pendiaman. 
- Tutup Rapat. 
- Tunggu Sampai 2 Minggu.
                     {bot.user} !''')

bot.run("MTE2MTI5MDgzNDEyNjMyNzgyOA.GHuGIN.cfn26JyGNZVVDTz3a7KdzR8xgXWItfNMYWvrbY")


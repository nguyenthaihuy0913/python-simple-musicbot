import discord
from discord.ext import commands
import yt_dlp

# Cấp quyền (Intents) cho bot đọc tin nhắn
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# --- LỆNH PHÁT NHẠC ---
@bot.command(name="play")
async def play(ctx, *, search: str):
    # 1. Kiểm tra xem người dùng đã vào phòng thoại chưa
    if not ctx.author.voice:
        return await ctx.send("❌ Bạn ơi, vào phòng thoại (Voice Channel) trước đi nàooo!")

    # 2. Cho bot tham gia phòng thoại
    vc = ctx.guild.voice_client
    if not vc:
        vc = await ctx.author.voice.channel.connect()
    elif vc.is_playing():
        vc.stop() # Dừng bài cũ nếu gõ bài mới

    await ctx.send("🔎 Đang tìm nhạc, chờ tui vài giây...")

    # 3. Cài đặt công cụ tìm nhạc và phát nhạc
    ytdl_opts = {'format': 'bestaudio', 'default_search': 'ytsearch1', 'quiet': True}
    ffmpeg_opts = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    try:
        with yt_dlp.YoutubeDL(ytdl_opts) as ydl:
            info = ydl.extract_info(search, download=False)
        
        if 'entries' in info:
            info = info['entries'][0] # Lấy kết quả đầu tiên
        
        url = info['url']
        title = info.get('title', 'Nhạc không tên')

        # 4. Phát nhạc
        source = discord.FFmpegPCMAudio(url, **ffmpeg_opts)
        vc.play(source)

        await ctx.send(f"🎶 Đang phát: **{title}**")

    except Exception as e:
        await ctx.send(f"❌ Huhu có lỗi rồi: {e}")

# --- CÁC LỆNH ĐIỀU KHIỂN ---
@bot.command(name="pause")
async def pause(ctx):
    vc = ctx.guild.voice_client
    if vc and vc.is_playing():
        vc.pause()
        await ctx.send("⏸️ Đã tạm dừng!")

@bot.command(name="resume")
async def resume(ctx):
    vc = ctx.guild.voice_client
    if vc and vc.is_paused():
        vc.resume()
        await ctx.send("▶️ Đã phát tiếp!")

@bot.command(name="stop")
async def stop(ctx):
    vc = ctx.guild.voice_client
    if vc:
        await vc.disconnect()
        await ctx.send("👋 Bai bai, tui đi ngủ đây!")

# --- SỰ KIỆN KHI BOT KHỞI ĐỘNG XONG ---
@bot.event
async def on_ready():
    print(f'✅ Khởi động thành công! Bot {bot.user} đã sẵn sàng nhận lệnh!')

# ==========================================
# 🛑 THAY TOKEN CỦA BẠN VÀO BÊN DƯỚI
# LƯU Ý: XÓA TOKEN TRƯỚC KHI ĐẨY LÊN GITHUB
# ==========================================
bot.run("DÁN_TOKEN_CỦA_BẠN_VÀO_ĐÂY")
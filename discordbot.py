from discord.ext import commands
import time
import requests
import json
import copy
from datetime import datetime, timedelta, timezone
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


Hololive = {
    "UCp6993wxpyDPHUpavwDFqgg": [
        "ときのそら",
        "https://twitter.com/tokino_sora/photo"
    ],
    "UCDqI2jOz0weumE8s7paEk6g": [
        "ロボ子さん",
        "https://twitter.com/robocosan/photo"
    ],
    "UC-hM6YJuNYVAmUWxeIr9FeA": [
        "さくらみこ",
        "https://twitter.com/sakuramiko35/photo"
    ],
    "UC5CwaMl1eIgY8h02uZw7u8A": [
        "星街すいせい",
        "https://twitter.com/suisei_hosimati/photo"
    ],
    "UC0TXe_LYZ4scaW2XMyi5_kw": [
        "AZKi",
        "https://twitter.com/AZKi_VDiVA/photo"
    ],
    "UCD8HOxPs4Xvsm8H0ZxXGiBw": [
        "夜空メル",
        "https://twitter.com/yozoramel/photo"
    ],
    "UCFTLzh12_nrtzqBPsTCqenA": [
        "アキ・ローゼンタール",
        "https://twitter.com/akirosenthal/photo"
    ],
    "UC1CfXB_kRs3C-zaeTG3oGyg": [
        "赤井はあと",
        "https://twitter.com/akaihaato/photo"
    ],
    "UCdn5BQ06XqgXoAxIhbqw5Rg": [
        "白上フブキ",
        "https://twitter.com/shirakamifubuki/photo"
    ],
    "UCQ0UDLQCjY0rmuxCDE38FGg": [
        "夏色まつり",
        "https://twitter.com/natsuiromatsuri/photo"
    ],
    "UC1opHUrw8rvnsadT-iGp7Cg": [
        "湊あくあ",
        "https://twitter.com/minatoaqua/photo"
    ],
    "UCXTpFs_3PqI41qX2d9tL2Rw": [
        "紫咲シオン",
        "https://twitter.com/murasakishionch/photo"
    ],
    "UC7fk0CB07ly8oSl0aqKkqFg": [
        "百鬼あやめ",
        "https://twitter.com/nakiriayame/photo"
    ],
    "UC1suqwovbL1kzsoaZgFZLKg": [
        "癒月ちょこ",
        "https://twitter.com/yuzukichococh/photo"
    ],
    "UCvzGlP9oQwU--Y0r9id_jnA": [
        "大空スバル",
        "https://twitter.com/oozorasubaru/photo"
    ],
    "UCp-5t9SrOQwXMU7iIjQfARg": [
        "大神ミオ",
        "https://twitter.com/ookamimio/photo"
    ],
    "UCvaTdHTWBGv3MKj3KVqJVCw": [
        "猫又おかゆ",
        "https://twitter.com/nekomataokayu/photo"
    ],
    "UChAnqc_AY5_I3Px5dig3X1Q": [
        "戌神ころね",
        "https://twitter.com/inugamikorone/photo"
    ],
    "UC1DCedRgGHBdm81E1llLhOQ": [
        "兎田ぺこら",
        "https://twitter.com/usadapekora/photo"
    ],
    "UCl_gCybOJRIgOXw6Qb4qJzQ": [
        "潤羽るしあ",
        "https://twitter.com/uruharushia/photo"
    ],
    "UCvInZx9h3jC2JzsIzoOebWg": [
        "不知火フレア",
        "https://twitter.com/shiranuiflare/photo"
    ],
    "UCdyqAaZDKHXg4Ahi7VENThQ": [
        "白銀ノエル",
        "https://twitter.com/shiroganenoel/photo"
    ],
    "UCCzUftO8KOVkV4wQG1vkUvg": [
        "宝鐘マリン",
        "https://twitter.com/houshoumarine/photo"
    ],
    "UCZlDXzGoo7d44bwdNObFacg": [
        "天音かなた",
        "https://twitter.com/amanekanatach/photo"
    ],
    "UCS9uQI-jC3DE0L4IpXyvr6w": [
        "桐生ココ",
        "https://twitter.com/kiryucoco/photo"
    ],
    "UCqm3BQLlJfvkTsX_hvm0UmA": [
        "角巻わため",
        "https://twitter.com/tsunomakiwatame/photo"
    ],
    "UC1uv2Oq6kNxgATlCiez59hw": [
        "常闇トワ",
        "https://twitter.com/tokoyamitowa/photo"
    ],
    "UCa9Y57gfeY0Zro_noHRVrnw": [
        "姫森ルーナ",
        "https://twitter.com/himemoriluna/photo"
    ],
    "UCFKOVgVbGmX65RxO3EtH3iw": [
        "雪花ラミィ",
        "https://twitter.com/amanekanatach/photo"
    ],
    "UCAWSyEs_Io8MtpY3m-zqILA": [
        "桃鈴ねね",
        "https://twitter.com/momosuzunene/photo"
    ],
    "UCUKD-uaobj9jiqB-VXt71mA": [
        "獅白ぼたん",
        "https://twitter.com/shishirobotan/photo"
    ],
    "UCK9V2B22uJYu3N7eR_BT9QA": [
        "尾丸ポルカ",
        "https://twitter.com/omarupolka/photo"
    ]
}  # 配信者のチャンネルID, 配信者名, アイコン画像のURLのリスト

webhook_url_Hololive = 'https://discord.com/api/webhooks/824612675753476117/Augy4FamRzkoPClwCcZPY2oymJtUMnv4OKGU09AMWb5prep9YGFRg4Z8JUSrjEc4eK8H'  # ホロライブ配信開始
webhook_url_Hololive_yotei = 'https://discord.com/api/webhooks/824612675753476117/Augy4FamRzkoPClwCcZPY2oymJtUMnv4OKGU09AMWb5prep9YGFRg4Z8JUSrjEc4eK8H'  # ホロライブ配信予定
broadcast_data = {}  # 配信予定のデータを格納

YOUTUBE_API_KEY = [
    "AIzaSyDqAGMl0spjURZvbLHKUZkr0OsqaQJ8Pkg",
    "AIzaSyBB73o6nMut-MCQcXQa7so_Q8iDR2mRXgQ",
    "AIzaSyA5CaErfon6WW7iclIW0vmc8IGaiohAMvY",
    "AIzaSyCfMdYMvAjLBxdt1Mey8PPxV0nsvieE-qQ",
    "AIzaSyCizi1jXzcZBCDiFJFSWRgL9ET3Cu5REq8",
    "AIzaSyAH2GjtmRoqvj4taeyNAJZDuobHrVOCPE0",
    "AIzaSyCz12fdVHeo9yYWWlxCdGzJXpteuOKHhws",
    "AIzaSyAjk8HkxQGG0L1INVuiH36iJAfDDJ557gQ",
    "AIzaSyDjdyycVzud59GCZMQmkNQ5h0r9P-eV-F0",

    "AIzaSyAtPTkPSyAmFsVcIkKlwEL4G0tgJ3-qjQw",
    "AIzaSyASRgfscK3lxYe2PGdTniA69VYuFXHP-sw",
    "AIzaSyB_GBaaKVZvga9GPkvWNGudSx6ukOi2EJg",
    "AIzaSyD2r924k1c2C5dbOPddYa0ARkQVxoOZe-k",
    "AIzaSyAgCEfL8RWyoJzT4nr9FSSweTL5z10sOfE",
    "AIzaSyDVFyH4cPAFJ8-BqoEiGkD1H2igZvYG_GI",
    "AIzaSyBUKotSFNDwzj9V0K_nPEXfE70goNILzXg",
    "AIzaSyBBi1F7fKRZbGW_YcYhJv3NbGOTLT5P8VQ",
    "AIzaSyDCC1KWgAskKvn-ahndvFHIdE1l0jcv5VU",
    "AIzaSyBxSy73nzPHUGFMv5vg128nO_y-15lxYog",

    "AIzaSyBHUQKMv_qCn32UetbzPNethbxzHHAgYDo",
    "AIzaSyBSuJ2dfoSflWkDcRhbNVJJ0s8XjzBwO5w",
    "AIzaSyAp4DtLvX1pNkijKqFytp1jTCXImsD-HYQ",
    "AIzaSyAPDH123lCyEuvgcLCmZm6mLNUGXchLRRY",
    "AIzaSyDZPmHC3knbfSh6fi7biFfUEtG8oHJA6Ac",
    "AIzaSyBlR-3s7n9-SLATphcMjgaFdGHqygeqT40",
    "AIzaSyCXzc0krq6YqFG008W73xXNhUlRbDpRvKw",
    "AIzaSyD2YKV5JYQylwNlxc1MrEn2pHJvAqeZL9c",
    "AIzaSyDtmtTV9P5zdJTBRm60HjIbarMZ6VRn7XM",
    "AIzaSyBSDkkXOqExzC4hb1slE1EaEQ6jOSsZw40",

    "AIzaSyB4qjANL4D8wbqf9mJoV4mVKKN17lomwLE",
    "AIzaSyANA0gQT2TOSnLClIqo_oaKhZKgc9j2A7E",
    "AIzaSyDllHB68VHOis1fLBnxa2C6AVKSEVlwIRk",
    "AIzaSyDfl_-klC3b64RCvSfw9ljTkowLFlHXI2U",
    "AIzaSyAF1Zys8eJ48hUIm6pk4upUaOzk83wL7-0",
    "AIzaSyC5F9YmbB894Valp0YfHrpbBozsS54hVlg",
    "AIzaSyAnIW9jTlDGXFMPeZh7FWUvXSXeOVu6g4Y",
    "AIzaSyAY2NnfGgCCa7I53mbG1ei2ygJl-NKw_nc",
    "AIzaSyAW7jXOsszB75Vsy--xffo0wh9DKH5PZME",
    "AIzaSyCFyO3BrGn0I77Rf6oo17dw4km_tBzP6y4"
]


def dataformat_for_python(at_time):  # datetime型への変換
    at_year = int(at_time[0:4])
    at_month = int(at_time[5:7])
    at_day = int(at_time[8:10])
    at_hour = int(at_time[11:13])
    at_minute = int(at_time[14:16])
    at_second = int(at_time[17:19])
    return datetime(at_year, at_month, at_day, at_hour, at_minute, at_second)


def replace_JST(s):
    a = s.split("-")
    u = a[2].split(" ")
    t = u[1].split(":")
    time = [int(a[0]), int(a[1]), int(u[0]), int(t[0]), int(t[1]), int(t[2])]
    if(time[3] >= 15):
        time[2] += 1
        time[3] = time[3] + 9 - 24
    else:
        time[3] += 9
    return (str(time[0]) + "/" + str(time[1]).zfill(2) + "/" + str(time[2]).zfill(2) + " " + str(time[3]).zfill(2) + "-" + str(time[4]).zfill(2) + "-" + str(time[5]).zfill(2))


def post_to_discord(userId, videoId):
    haishin_url = "https://www.youtube.com/watch?v=" + videoId  # 配信URL
    content = "配信中！\n" + haishin_url  # Discordに投稿される文章
    main_content = {
        "username": Hololive[userId][0],  # 配信者名
        "avatar_url": Hololive[userId][1],  # アイコン
        "content": content  # 文章
    }
    requests.post(webhook_url_Hololive, main_content)  # Discordに送信
    broadcast_data.pop(videoId)


def get_information():
    tmp = copy.copy(broadcast_data)
    api_now = 0  # 現在どのYouTube APIを使っているかを記録
    for idol in Hololive:
        api_link = "https://www.googleapis.com/youtube/v3/search?part=snippet&channelId=" + \
            idol + "&key=" + \
            YOUTUBE_API_KEY[api_now] + "&eventType=upcoming&type=video"
        api_now = (api_now + 1) % len(YOUTUBE_API_KEY)  # apiを1つずらす
        aaa = requests.get(api_link)
        v_data = json.loads(aaa.text)
        try:
            for item in v_data['items']:  # 各配信予定動画データに関して
                broadcast_data[item['id']['videoId']] = {
                    'channelId': item['snippet']['channelId']}  # channelIDを格納
            for video in broadcast_data:
                try:
                    # 既にbroadcast_dataにstarttimeがあるかチェック
                    _ = broadcast_data[video]['starttime']
                except KeyError:  # なかったら
                    aaaa = requests.get(
                        "https://www.googleapis.com/youtube/v3/videos?part=liveStreamingDetails&id=" + video + "&key=" + YOUTUBE_API_KEY[api_now])
                    api_now = (api_now + 1) % len(YOUTUBE_API_KEY)  # apiを1つずらす
                    vd = json.loads(aaaa.text)
                    print(vd)
                    broadcast_data[video]['starttime'] = vd['items'][0]['liveStreamingDetails']['scheduledStartTime']
        except KeyError:  # 配信予定がなくて403が出た
            continue
    for vi in broadcast_data:
        if(not(vi in tmp)):
            print(broadcast_data[vi])
            try:
                post_broadcast_schedule(
                    broadcast_data[vi]['channelId'], vi, broadcast_data[vi]['starttime'])
            except KeyError:
                continue


def check_schedule(now_time, broadcast_data):
    for bd in list(broadcast_data):
        try:
            # RFC 3339形式 => datetime
            sd_time = datetime.strptime(
                broadcast_data[bd]['starttime'], '%Y-%m-%dT%H:%M:%SZ')  # 配信スタート時間をdatetime型で保管
            sd_time += timedelta(hours=9)
            if(now_time >= sd_time):  # 今の方が配信開始時刻よりも後だったら
                post_to_discord(broadcast_data[bd]['channelId'], bd)  # ツイート
        except KeyError:
            continue


def post_broadcast_schedule(userId, videoId, starttime):
    st = starttime.replace('T', ' ')
    sst = st.replace('Z', '')
    ssst = replace_JST(sst)
    haishin_url = "https://www.youtube.com/watch?v=" + videoId  # 配信URL
    content = ssst + "に配信予定！\n" + haishin_url  # Discordに投稿される文章
    main_content = {
        "username": Hololive[userId][0],  # 配信者名
        "avatar_url": Hololive[userId][1],  # アイコン
        "content": content  # 文章
    }
    requests.post(webhook_url_Hololive_yotei, main_content)  # Discordに送信


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(
        traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.event
async def on_ready():
    while True:
        now_time = datetime.now() + timedelta(hours=9)
        if(((now_time.year > 2020) or ((now_time.year == 2020) and (now_time.month >= 6) and (now_time.day >= 22))) and (now_time.minute == 0) and (now_time.hour % 2 == 0)):
            get_information()
        check_schedule(now_time, broadcast_data)
        time.sleep(60)


bot.run(token)

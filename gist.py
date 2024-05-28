import os
import json
import sys
from dotenv import load_dotenv
from bilibili_api import Credential,user,sync 
from github.InputFileContent import InputFileContent
from github import Github

ENV_VAR_GIST_ID = "GIST_ID"
ENV_VAR_GITHUB_TOKEN = "GH_TOKEN"
ENV_VAR_BILI_SESSDATA = "BILI_SESSDATA"
REQUIRED_ENVS = [
    ENV_VAR_GIST_ID,
    ENV_VAR_GITHUB_TOKEN,
    ENV_VAR_BILI_SESSDATA
]
async def get_bili_video_list():
    global vist
    vist = await u.get_videos(ps=3)
    return 

async def get_bili_relation_info():
    relate = await u.get_relation_info()
    return relate

async def get_bili_user_info():
    sessdata= os.environ[ENV_VAR_BILI_SESSDATA]
    global cedential
    cedential = Credential(sessdata=sessdata)
    info= await user.get_self_info(credential=cedential)
    return info

def update_gist(title: str, content: str) -> bool:
    access_token = os.environ[ENV_VAR_GITHUB_TOKEN]
    gist_id = os.environ[ENV_VAR_GIST_ID]
    gist = Github(access_token).get_gist(gist_id)
    # Shouldn't necessarily work, keeping for case of single file made in hurry to get gist id.
    old_title = list(gist.files.keys())[0]
    gist.edit(title, {old_title: InputFileContent(content, title)})
    print(f"{title}\n{content}")

def getneededinfo(info: str,need: str):
    print(info[need])
    return info[need] 

def getvideoinfo(num: int,need: str):
    return vist["list"]["vlist"][num][need]

def getvideodate(num: int):
    import datetime
    from pytz import timezone
    tzc = timezone('Asia/Shanghai')
    date= getvideoinfo(num,"created")
    date_time = datetime.datetime.fromtimestamp(date,tz=tzc)
    formated_date = date_time.strftime("%Y年%m月%d日 %H:%M:%S %Z")
    return formated_date

def main():
    username= getneededinfo(i,"name")
    follower= getneededinfo(follows,"follower")
    following = getneededinfo(follows,"following")
    title1 = getvideoinfo(0,"title")
    date1 = getvideodate(0)
    title2 = getvideoinfo(1,"title")
    date2 = getvideodate(1)
    title3 = getvideoinfo(2,"title")
    date3 = getvideodate(2)
    print("info:用户名：",username,"粉丝数：",follower,"关注数：",following)
    print(title1,date1,"\n",title2,date2,"\n",title3,date3)
    contents = f"粉丝数: {follower} 关注数: {following} \n ▶️最近更新视频：\n {title1}  {date1} \n {title2}  {date2} \n {title3}  {date3}"
    update_gist(f"📺bilibili@{username} ",contents)



if __name__== "__main__":
    load_dotenv(dotenv_path="./.env")
    import time
    s = time.perf_counter()
    global i
    i = sync(get_bili_user_info())
    global u
    u= user.User(i["mid"],credential=cedential)
    global follows
    follows = sync(get_bili_relation_info())
    sync(get_bili_video_list())
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

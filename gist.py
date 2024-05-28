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
    u= user.User(i["mid"],credential=cedential)
    global vist
    vist = await u.get_videos(ps=3)
    return 

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

def getneededinfo(need: str):
    print(i[need])
    return i[need] 

def getvideoinfo(num: int,need: str):
    return vist["list"]["vlist"][num][need]

def main():
    username= getneededinfo("name")
    follower= getneededinfo("follower")
    following = getneededinfo("following")
    title1 = getvideoinfo(0,"title")
    title2 = getvideoinfo(1,"title")
    title3 = getvideoinfo(2,"title")
    print("info:用户名：",username,"粉丝数：",follower,"关注数：",following)
    print(title1,"\n",title2,"\n",title3)
    contents = f"粉丝数: {follower} 关注数: {following} \n 最近更新视频：\n {title1} \n {title2} \n {title3}"
    update_gist(f"bilibili@{username} ",contents)



if __name__== "__main__":
    load_dotenv(dotenv_path="./.env")
    import time
    s = time.perf_counter()
    global i
    i = sync(get_bili_user_info())
    sync(get_bili_video_list())
    # test with python gist.py test <gist> <github-token> <bili_sessdata>
    #if len(sys.argv) > 1:
    #    os.environ[ENV_VAR_GIST_ID] = sys.argv[2]
    #    os.environ[ENV_VAR_GITHUB_TOKEN] = sys.argv[3]
    #    os.environ[ENV_VAR_BILI_SESSDATA] = sys.argv[4]
    main()
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

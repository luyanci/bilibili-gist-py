import os
import sys
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

async def get_bili_user_info():
    sessdata= os.environ[ENV_VAR_BILI_SESSDATA]
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

def getneeded(infos: dict,need: str):
    print(infos[need])
    return infos[need] 


def main(inf: dict):
    username= getneeded(inf,"name")
    follower= getneeded(inf,"follower")
    following = getneeded(inf,"following")
    print("info:用户名：",username,"粉丝数：",follower,"关注数：",following)




if __name__== "__main__":
    import time
    i = sync(get_bili_user_info())
    s = time.perf_counter()
    # test with python gist.py test <gist> <github-token> <bili_sessdata>
    if len(sys.argv) > 1:
        os.environ[ENV_VAR_GIST_ID] = sys.argv[2]
        os.environ[ENV_VAR_GITHUB_TOKEN] = sys.argv[3]
        os.environ[ENV_VAR_BILI_SESSDATA] = sys.argv[4]
    main(i)
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

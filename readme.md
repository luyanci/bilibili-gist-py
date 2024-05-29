<div align="center">

![1000054481](https://github.com/luyanci/bili-gist/assets/68143180/98f8a656-921c-4545-a754-86fc93173b69)

# Bili Gist

📺将你的b站信息和近期投稿视频更新到你的pinned Gist📺

</div>

## 使用
### 准备工作
1. 创建一个公开的 GitHub Gist (https://gist.github.com/)

1. 创建一个拥有 gist 权限的 token 并复制. (https://github.com/settings/tokens/new)

1. 根据文档获取`SESSDATA`的值并复制(https://nemo2011.github.io/bilibili-api/#/get-credential)

### 部署

1. fork这个仓库

2. 编辑  `.github/workflows/main.yml` 中的**环境变量**

3. 前往仓库的 **Settings > Secrets**

4. 点击 **New repository secret** 并添加如下仓库秘密 (repository secrets) ：
   - **GH_TOKEN:** 刚才复制的 GitHub token
   - **BILI_SESSDATA:** 刚才复制的B站SESSDATA值

5. 前往仓库的 **Actions > Update gist** 并点击 `enable workflows`

## 本地测试



## 工作原理

 - 使用**bilibili-api-python**来获取相关信息

 - 利用**Github Actions**自动更新Gist

## 灵感&帮助
[bilibili-api-python](https://github.com/nemo2011/bilibili-api)

[bilibili-box](https://github.com/KeJunMao/bilibili-box)

[chess-com-box-py](https://github.com/sciencepal/chess-com-box-py)

## 许可

本仓库使用了`MIT`开源协议证书
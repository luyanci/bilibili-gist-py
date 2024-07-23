<div align="center">

![1000054481](https://github.com/luyanci/bili-gist/assets/68143180/98f8a656-921c-4545-a754-86fc93173b69)

# Bilibili Gist Python

📺将你的b站信息和近期投稿视频更新到你的pinned Gist📺

中文|[English](readme_en.md)

[![Update gist](https://github.com/luyanci/bilibili-gist-py/actions/workflows/main.yml/badge.svg)](https://github.com/luyanci/bilibili-gist-py/actions/workflows/main.yml)

</div>

---

> 📌✨ 更多像这样的 Pinned Gist 项目请访问：https://github.com/matchai/awesome-pinned-gists

---

## 使用
### 准备工作
1. 创建一个公开的 GitHub Gist (https://gist.github.com/)

1. 创建一个拥有 gist 权限的 token 并复制. (https://github.com/settings/tokens/new)

1. 根据文档获取`SESSDATA`的值并复制(https://nemo2011.github.io/bilibili-api/#/get-credential)

### 部署

#### 复刻使用

1. fork本仓库

2. 编辑  `.github/workflows/main.yml` 中的**环境变量**

3. 前往仓库的 **Settings > Secrets**

4. 点击 **New repository secret** 并添加如下仓库秘密 (repository secrets) ：
   - **GH_TOKEN:** 刚才复制的 GitHub token
   - **BILI_SESSDATA:** 刚才复制的B站SESSDATA值

5. 前往仓库的 **Actions > Update gist** 并点击 `enable workflows`

#### Action使用



## 本地测试

1. clone本仓库

2. 输入以下命令安装依赖

```
pip install -r requirements.txt
```

3. 复制`.env.example`文件，更名为`.env`，并按照文件内容填写即可

4. 输入以下命令，进行测试

```
py gist.py
```

## 工作原理

 - 使用**bilibili-api-python**来获取相关信息

 - 利用**Github Actions**自动更新Gist

## 灵感&帮助
[bilibili-api-python](https://github.com/nemo2011/bilibili-api)

[bilibili-box](https://github.com/KeJunMao/bilibili-box)

[chess-com-box-py](https://github.com/sciencepal/chess-com-box-py)

## 许可

本仓库使用了`MIT`开源协议证书
```
 The MIT License (MIT)
 Copyright (c) 2024 luyanci

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all
 copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
 OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
 OR OTHER DEALINGS IN THE SOFTWARE.
```
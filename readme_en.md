<div align="center">

![1000054481](https://github.com/luyanci/bili-gist/assets/68143180/98f8a656-921c-4545-a754-86fc93173b69)

# Bilibili Gist Python

📺Update a pinned gist to show your Bilibili stats and your latest videos.📺

[中文](readme.md)|English

[![Update gist](https://github.com/luyanci/bilibili-gist-py/actions/workflows/main.yml/badge.svg)](https://github.com/luyanci/bilibili-gist-py/actions/workflows/main.yml)

</div>

---

> 📌✨ For more pinned-gist projects like this one, check out: https://github.com/matchai/awesome-pinned-gists

---

## Usage
### Prepare
1. Create a public GitHub Gist. (https://gist.github.com/)

1. Create a has `gist` permissions token then copy it. (https://github.com/settings/tokens/new)

1. Follow the documents to get`SESSDATA`'s key then copy it.(https://nemo2011.github.io/bilibili-api/#/get-credential)

1. Find UID in Bilibili personal space link (https://space.bilibili.com/282873551)

### Deploy

#### By Forks

1. Fork this repository.

2. Edit the env in file `.github/workflows/main.yml`.

3. Go to **Settings > Secrets**.

4. Click **New repository secret** and add the repository secrets below ：
   - **GH_TOKEN:**  GitHub token
   - **BILI_SESSDATA:** SESSDATA

5. Go to **Actions > Update gist** then click `enable workflows`.

#### By Workflow

Use this sample to your workflow.

```yaml
        - name: Update gist
          uses: luyanci/bilibili-gist-py@master
          with:
            ghtoken: ${{ secrets.GH_TOKEN }}
            gistid: 181a99b82ae47d3a6fccbd126f9d93ef
            sessdata: ${{ secrets.BILI_SESSDATA }}
            biliuid: '282873551'
```

## Local test

1. Clone this repository.

2. Install the requirements by the command below.

```
pip install -r requirements.txt
```

3. Copy`.env.example`file,and rename to `.env`，then edit it.

4. Run the gist.py by the command below.

```
py gist.py
```

## How it works?

 - Use **bilibili-api-python** to get some details on bilibili.

 - Use **Github Actions** to Auto update the Gist.

## Helps
[bilibili-api-python](https://github.com/nemo2011/bilibili-api)

[bilibili-box](https://github.com/KeJunMao/bilibili-box)

[chess-com-box-py](https://github.com/sciencepal/chess-com-box-py)

## License

Used `MIT License` on this repository.
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
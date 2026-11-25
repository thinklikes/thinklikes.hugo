+++
date = '2026-11-23'
draft = false
title = 'AI 省時小工具（3） - 用 ChatGPT 串接 GitHub，做一個自己的個人網站'
description = '讓 ChatGPT 連上 GitHub，請它做好個人網站並直接寫進 Repository，放進自己的 github.io 就會自動上線，拿到一個可以分享的網址。'
tags = ['ChatGPT', 'GitHub', '個人網站']
topics = ['AI 省時小工具']
+++

## 前言

這篇要用 ChatGPT 做一個自己的個人網站，從版面、文字到程式都交給它寫，寫好之後由 ChatGPT 直接存進 GitHub，網站就會自動出現在網路上。整個過程不需要會寫程式，也不需要買主機或網域，順利的話大約半小時可以完成。

整個流程是這樣：

1. 在 GitHub 建立一個放網站的地方
2. 把 ChatGPT 連上 GitHub
3. 請 ChatGPT 做出個人網站
4. 請 ChatGPT 把網站寫進 GitHub
5. 打開網站網址，確認網站上線

【作者補：自己為什麼想做這個網站、做完放在哪裡用】

---

## 動手前

請先準備好：

- 一個 GitHub 帳號。還沒有的話，可以先照這篇（[AI 省時小工具（2） - 註冊 GitHub 帳號，順便把兩步驟驗證開起來]({{< ref "/posts/ai-tools/github-signup-2fa" >}})）註冊，並把兩步驟驗證開起來
- 一個 ChatGPT 帳號
- 一台電腦，建議使用電腦操作較為順暢

這篇會用到兩個工具：

| 工具 | 用途 |
| --- | --- |
| ChatGPT | 設計和製作網站 |
| GitHub | 存放網站的檔案，並免費把網站放上網路 |

先講幾個之後會看到的名詞，看過有印象就好：

- **Repository**：GitHub 上的一個專案資料夾，網站的所有檔案都放在裡面
- **Commit**：一次修改的紀錄，每改一次網站就會多一筆
- **Branch**：分支，這篇只會用到預設的 `main`

---

## 步驟一：在 GitHub 建立網站用的 Repository

ChatGPT 可以修改 Repository 裡的檔案，但沒辦法幫你建立新的 Repository，所以這一步要自己在 GitHub 網站上完成。

1. 登入 GitHub，點右上角的 **+**，選 **New repository**
2. **Repository name** 填 `你的帳號.github.io`，例如帳號是 `john123`，就填 `john123.github.io`
3. **Choose visibility** 選 **Public**。免費帳號要選公開，網站才會自動上線
4. 把 **Add README** 右邊的開關從 Off 打開
5. 按 **Create repository**

![github-new-repository.png](github-new-repository.png "建立新的 Repository")

![github-repository-visibility.png](github-repository-visibility.png "可見度選單裡選 Public")

Repository 用 `你的帳號.github.io` 這個名字，GitHub 會把它當成你的個人網站：之後放進去的網頁檔案會自動上線，網址就是 `https://你的帳號.github.io/`，不需要另外設定。一個帳號只能有一個這種 Repository。

{{< alert icon="triangle-exclamation" >}}
公開的 Repository 任何人都看得到裡面的檔案，不要把電話、住址、身分證字號這類個資寫進網站。
{{< /alert >}}

---

## 步驟二：讓 ChatGPT 連接 GitHub

1. 打開 ChatGPT，點帳號名稱，進入 **設定**
2. 在左側選單的「整合」區塊，點 **外掛程式**，再按右上角的 **瀏覽目錄**
3. 在外掛程式清單裡找到 **GitHub**，按右邊的 **+**
4. 畫面會跳到 GitHub，出現「ChatGPT Codex Connector by OpenAI」的授權頁面，確認是 OpenAI 的應用程式後，按 **Authorize**
5. 回到 ChatGPT 後，會跳出「授予 GitHub 程式碼庫存取權」的視窗，按 **選取 GitHub 程式碼庫**
6. 畫面會跳到 GitHub 的「Install & Authorize ChatGPT Codex Connector」頁面。在「for these repositories」選 **Only select repositories**，只勾剛剛建立的 `你的帳號.github.io`
7. 按 **Install & Authorize**

![chatgpt-settings-plugins.png](chatgpt-settings-plugins.png "設定裡的外掛程式頁面")

![chatgpt-plugins-github.png](chatgpt-plugins-github.png "在外掛程式目錄找到 GitHub，按 +")

![github-authorize-chatgpt.png](github-authorize-chatgpt.png "在 GitHub 授權 ChatGPT")

![chatgpt-github-repo-access.png](chatgpt-github-repo-access.png "授權後，選取 ChatGPT 可以存取的 Repository")

![github-install-authorize.png](github-install-authorize.png "選 Only select repositories，再按 Install & Authorize")

連接成功之後，ChatGPT 就能讀取並修改你授權的 Repository。之後想調整範圍或取消連接，回到 **設定** > **外掛程式**，點 **GitHub** 修改即可。

剛建立的 Repository 可能要等幾分鐘才會出現在 ChatGPT 裡。

---

## 步驟三：請 ChatGPT 做出個人網站

開一個新的對話，把下面的提示詞複製貼上，【】裡換成自己的資料：

```text
請幫我建立一個個人介紹網站。

我的資料：
- 姓名：【王小明】
- 職業：【平面設計師】
- 自我介紹：【喜歡設計與創作，擅長將想法轉化成視覺作品。】
- 作品：【平面設計、品牌識別、網站設計】
- 聯絡方式：【example@gmail.com】

網站需求：
1. 使用 HTML、CSS、JavaScript。
2. 採用響應式設計，手機也能正常瀏覽。
3. 設計簡潔、現代。
4. 包含個人介紹、作品展示、聯絡資訊。
5. 不使用需要付費的外部服務。
6. 網站入口使用 index.html。

請先規劃網站架構，再建立完整的網站檔案。
```

ChatGPT 會先列出網站的架構，再產生網站檔案。不需要一次就做到滿意，可以繼續在同一個對話裡請它調整，例如：

| 想調整的地方 | 複製這句貼給 ChatGPT |
| --- | --- |
| 顏色 | 請把網站的主色改成【墨綠色】，其他顏色跟著搭配。 |
| 字體 | 請把標題改成比較粗的字體，內文維持好閱讀的字體。 |
| 版面 | 請把作品展示改成一排三個的卡片，手機上改成一排一個。 |
| 作品圖片 | 我上傳了幾張作品圖，請放進作品展示區，並幫每張加上簡短說明。 |
| 自我介紹 | 請把自我介紹改寫得更口語一點，控制在三句話以內。 |

![chatgpt-website-preview.png](chatgpt-website-preview.png "用範例資料做出來的個人網站")

---

## 步驟四：請 ChatGPT 把網站寫進 GitHub

網站調整好之後，在同一個對話裡貼上：

```text
請幫我將剛剛完成的個人網站寫入我的 GitHub。

Repository：【你的帳號/你的帳號.github.io】
Branch：main

請依照以下步驟執行：
1. 確認 Repository 是否存在。
2. 檢查目前的檔案結構。
3. 建立或更新網站所需檔案。
4. 確認 index.html 位於最上層。
5. 建立一筆 Commit。
6. 更新 main 分支。

請不要刪除與本次網站無關的既有檔案。
完成後，請列出修改的檔案與 Commit 資訊。
```

ChatGPT 完成後，會列出新增或修改了哪些檔案。回到 GitHub 打開這個 Repository，就能看到 `index.html` 等檔案，以及剛剛那筆 Commit。

![chatgpt-commit-result.png](chatgpt-commit-result.png "ChatGPT 回報已推送到 GitHub，並列出修改的檔案與 Commit 資訊")

![github-repository-files.png](github-repository-files.png "GitHub Repository 裡的網站檔案與最新一筆 Commit")

如果出現以下狀況，可以這樣處理：

| 狀況 | 複製這句貼給 ChatGPT |
| --- | --- |
| ChatGPT 說找不到 Repository | 請列出你目前可以存取的 GitHub Repository。 |
| ChatGPT 說沒有寫入權限 | 請說明目前缺少哪些權限，以及我要在 GitHub 哪裡調整授權。 |
| ChatGPT 只給了檔案內容，沒有寫進 GitHub | 請直接把這些檔案寫入【你的帳號/你的帳號.github.io】的 main 分支，並建立一筆 Commit。 |

找不到 Repository 時，先確認步驟一已經自己建立好 `你的帳號.github.io`，再回到步驟二，確認授權時有勾選這個 Repository。如果 ChatGPT 回覆「無法建立 Repository」，代表這個 Repository 還不存在，回到步驟一建立即可，ChatGPT 本身沒辦法建立。

---

## 步驟五：打開網站網址

ChatGPT 把檔案寫進 GitHub 之後，網站會自動上線，通常幾分鐘內會完成，最久可能要等到 10 分鐘。

在瀏覽器打開以下網址，就能看到自己的網站：

```text
https://你的帳號.github.io/
```

![website-live.png](website-live.png "上線後的個人網站，網址就是 帳號.github.io")

如果等了 10 分鐘還是打不開，或看到 404 頁面，請確認：

- Repository 的名字和帳號完全一樣，例如帳號是 `john123`，名字就是 `john123.github.io`
- Repository 是 **Public**
- `index.html` 放在 Repository 的最上層

若還是找不到問題的話，可以直接讓 ChatGPT 檢查你的 Repository。

---

## 完成之後

這個網址任何人都打得開，可以放在名片、社群自介或履歷上。

之後想修改網站，不需要從頭做，回到 ChatGPT 說明想改的地方即可：

```text
請幫我修改 GitHub 上的個人網站，Repository 是【你的帳號/你的帳號.github.io】。

我想要：
1. 【將背景改成墨綠色】
2. 【增加一個新的作品展示區】
3. 【手機版的選單改成漢堡選單】

請先讀取目前 Repository 的程式碼，說明打算怎麼修改，等我確認後再執行。
完成後請建立 Commit 並更新 main 分支。
```

ChatGPT 更新之後，網站會自動跟著更新，過幾分鐘重新整理網頁就能看到新的內容。

【作者補：自己做完的網站長什麼樣子、用了哪些調整】

---

## 常見問題

**放網站要付費嗎？**

不用。免費帳號只要 Repository 是公開的，網站就能免費上線；想把 Repository 設成私人又要上線，才需要付費方案。

**可以做購物網站或會員系統嗎？**

不行。這種方式只能放靜態網站，也就是 HTML、CSS、JavaScript 這類檔案，不能執行 PHP 等後端程式，也沒有資料庫。需要會員登入、儲存資料或金流時，要另外搭配後端服務。

**一定要學 Git 指令嗎？**

不用。這篇的流程全部透過 ChatGPT 和 GitHub 網頁完成。有興趣的話，可以先從前面提到的 Repository、Commit、Branch 這幾個名詞開始認識。

---

### 參考資料

- [Connecting GitHub to ChatGPT](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt)
- [Quickstart for GitHub Pages](https://docs.github.com/en/pages/quickstart)
- [Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

---

*本文由 AI 輔助潤稿*

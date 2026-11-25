# 教學文發佈流程（AI 省時小工具／基礎教學）

依 2026-11-18～11-23「AI 省時小工具（2）註冊 GitHub 並開啟兩步驟驗證」實際走過的流程整理。草稿怎麼寫看 `.claude/skills/tutorial-draft/SKILL.md`，本文件管從草稿到粉絲團貼文的整條流程。

內部文件，不會被 Hugo 發布。

---

## 總覽

| 階段 | 誰做 | 產出 |
|---|---|---|
| 1. 題目評估 | Claude 提出，作者決定 | 保留／候補／刷掉 |
| 2. 草稿 | Claude | `index.md`（`draft = true`）＋ PR |
| 3. 截圖 | 作者截圖，Claude 處理 | 打馬賽克、加醒目框的圖片 |
| 4. 審稿 | Claude（抗性思辨）＋作者 | 修正後的文章 |
| 5. 封面 | Claude 用腳本產生 | `feature.png` |
| 6. 定稿與合併 | 作者 | `draft = false`，PR 合併上線 |
| 7. 粉絲團貼文 | Claude 寫，作者發 | 貼文文字 |
| 8. 成效紀錄 | 作者提供數字，Claude 記錄 | `post-log.md` 新增一列 |

---

## 1. 題目評估

- 依 skill 第一節做抗性思辨，結論給作者看，作者同意才動筆。

## 2. 草稿

- 在 feature branch 建立 `content/posts/<系列資料夾>/<slug>/index.md`，`draft = true`。
- 按鈕名稱、數量、規格一律查官方文件（docs.github.com 等），寫作當天查。
- 截圖先放固定檔名的圖片連結＋HTML 註解說明要截哪個畫面。
- 開 PR（不自動合併），PR 說明附截圖清單。之後每次修改都推到同一個 PR，Cloudflare Pages 會自動建置預覽頁。

## 3. 截圖處理

作者在對話裡直接上傳原始截圖，並說明要做什麼處理。

- **打馬賽克**：頭像、使用者名稱、Email、QR code、setup key、救援碼、驗證碼。用 PIL 裁切區塊、縮小再用 NEAREST 放大，馬賽克要夠粗，看不出原字。
- **醒目提示**：要按的按鈕或欄位加紅色圓角框（`(255, 59, 48)`，線寬 4）。
- **存放**：處理後的圖放進文章資料夾（和 `index.md` 同一層），另存一份到 `/mnt/project-files/<主題>/` 方便作者在對話裡看。
- **檔名**：不能含 `feature`、`cover`、`thumbnail`，包括 `recovery` 這種內含 `cover` 的字（Congo 會把它當封面）。救援碼畫面改用 `backup-codes`。
- **安全提醒**：原始截圖如果露出還有效的 QR code 或救援碼，要提醒作者到 GitHub 重新產生，並刪掉對話中的原圖。

作者不需要的截圖位置，直接從文中刪掉，不要留空的佔位。

## 4. 審稿

- **抗性思辨審查**：逐點列出問題（查證、順序、語氣、讀者會卡住的地方），編號讓作者挑要改哪幾點。
- **通順度檢查**：語氣中性、句子完整、沒有 AI 腔，標點全形。
- **前言、結尾**：給兩三個版本讓作者選，不代寫作者的動機和心得（留 `【作者補】` 或直接刪）。
- 結尾不寫明確的下集預告（CLAUDE.md 的條件預告規則）。

## 5. 封面

用 `scripts/make_cover.py` 產生 `feature.png`（1200×630）：

```bash
python3 scripts/make_cover.py --num <系列編號> \
  --title "<標題第一行>" --title "<標題第二行>" \
  --color 57606a --icon-color <工具品牌色> --icon <lock|sticker> \
  --out content/posts/<系列資料夾>/<slug>/feature.png
```

固定規則：

- 白底，系列標籤與左側色條用灰色 `57606a`，只有圖示和圖示背後的圓用工具的品牌色（例如 GitHub `1f883d`、LINE `06c755`）。整張圖都用主色會顯得太滿。
- 字型用 repo 內的思源黑體 Bold（`scripts/fonts/NotoSansTC-Bold.otf`）。
- 標題拆成兩行，每行要短，縮成小圖也看得清楚。
- 新題材需要新圖示時，加在腳本的 `ICONS`。
- 左下角頭像固定用網站目前的 icon（一個人使用電腦，`assets/img/avatar.png`，腳本讀的是同一張的副本 `scripts/cover-avatar.png`），與 favicon、首頁作者頭像一致。不要用戴耳機的卡通頭像；之後若換站台 icon，兩個檔案要一起換。

## 6. 定稿與合併

1. 作者確認內容後，把 front matter 的 `draft` 改成 `false`，`date` 改成發布日。
2. 更新 `CLAUDE.md` 的「目前進度」。
3. 作者在 GitHub 合併 PR（Claude 不合併）。合併進 `master` 後 Cloudflare Pages 自動部署。

## 7. 粉絲團貼文

文章上線後，為粉絲團（阿清師的 AI 軟體教學）寫推廣貼文。

- 先給短、中、長幾個版本讓作者挑。
- **語氣中立理性**：只陳述文章是什麼、能解決什麼、包含哪些步驟。不用「我建議」「不難」這類主觀說法，不用表情符號。
- 中版的結構：標題列【系列名（N）文章標題】→ 工具是什麼、什麼時候會用到 → 這篇解決的問題 → 編號列出步驟 → 附截圖說明 → 連結。
- 連結格式：`https://coder-adventure.pages.dev/posts/<系列資料夾>/<slug>/`，發文前請作者點一次確認。
- 配圖用文章封面。
- 草稿存在 `/mnt/project-files/drafts/fb-posts/<slug>-fb-posts.md`。

範例（GitHub 篇定稿）：

```text
【AI 省時小工具（2）註冊 GitHub 並開啟兩步驟驗證】

GitHub 是存放程式碼和網頁檔案的網站。使用 ChatGPT 製作網站，或將 AI 製作的小工具放上網路時，經常需要用到 GitHub 帳號。

開啟兩步驟驗證後，登入時除了密碼，還需要輸入手機驗證器 App 上的六位數驗證碼。即使密碼外流，沒有這支手機也無法登入。

本篇內容包含：
1. 註冊 GitHub 帳號
2. 安裝驗證器 App（Google Authenticator 或 Microsoft Authenticator）
3. 在 GitHub 開啟兩步驟驗證
4. 下載並保存救援碼，供手機遺失時登入使用

GitHub 介面為英文，文中標註了每個按鈕的原文，並附上操作截圖。

https://coder-adventure.pages.dev/posts/ai-tools/github-signup-2fa/
```

## 8. 成效紀錄

- 每則貼文給一個流水號（001、002……）。
- 作者貼上 FB 洞察報告的數字後，記到 `/mnt/project-files/social-metrics/post-log.md`。同一則貼文隔幾天再看，新增一列，不覆蓋舊數字。

---

## 檢查清單

- [ ] 題目評估作者已同意
- [ ] 按鈕名稱、數字都查過官方文件
- [ ] 截圖的個資都已打馬賽克，檔名不含 feature／cover／thumbnail
- [ ] 抗性思辨審查與通順度檢查都做過
- [ ] `feature.png` 用腳本產生，灰色標籤＋品牌色圖示，左下角是網站目前的電腦人像 icon
- [ ] `draft = false`、日期正確、`CLAUDE.md` 進度已更新
- [ ] PR 由作者合併
- [ ] 粉絲團貼文語氣中立，連結作者已確認
- [ ] 貼文編號與成效已記錄

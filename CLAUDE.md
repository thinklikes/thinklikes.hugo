# CLAUDE.md

本檔案供 Claude Code 在此 repo 工作時載入的專案記憶。進度或決策有變動時，請一併更新本檔的「目前進度」。

## 專案概觀

- Hugo 部落格「中年碼農的職場奇妙冒險」，主題 Congo，正體中文。
- 部署：merge 進 `master` 即由 Cloudflare Pages 自動建置發布（`hugo --gc --minify`，`HUGO_VERSION=0.145.0`）。
- 敘事主軸：**作者在公司內從零建立各種 AI 應用**的第一人稱紀錄。RAG 知識庫是第一個應用，不是全部；主題隨 side project 實際做到哪裡往外長。
- 這些應用同時是 side project——**專案是主，文章是副產品**，有料才寫，不趕進度；章節表當題目池看，不當承諾看。
- 站上另有**職場觀察**類的單篇文章（非系列），與 AI 應用系列並行。
- **不經營外部平台**（FB／IG／Threads／Substack 等），內容就放在自己的站上，不主動推廣——除非作者另外開口，不要再提平台策略。

## 教學文

寫給非工程師的操作教學（AI 省時小工具、基礎教學）時，依 `.claude/skills/tutorial-draft/SKILL.md` 的流程：題目抗性思辨 → 查官方文件 → 預留截圖位置 → PR 附截圖清單。從截圖處理、審稿、封面、合併到粉絲團貼文與成效紀錄的整條發佈流程，見 `docs/tutorial-publish-workflow.md`。

## 單一事實來源

系列規劃、章節狀態、各篇大綱、寫作原則與排版風格偏好，全部以 `docs/rag-series-plan.md` 為準（內部文件，不會被 Hugo 發布）。動筆或 review 前先讀它。

## 工作流程重點

1. 大綱與作者討論定稿 → 作者執筆（`draft = true`，開發於 feature branch）→ 交叉 review（Claude + ChatGPT）→ 作者定稿後 `draft = false` 開 PR。
2. **PR 一律由作者確認後才合併，不自動合併。**
3. 文章內不放系列規劃；**下集預告有條件允許**：僅在該篇內容寫不完、有未收尾的內容要留到下一篇時，才可在文中輕量帶過（只講未寫完的內容，不承諾題目與時程）。規劃文件的章節表不必照著做；文末固定加註「*本文由 AI 輔助潤稿*」。
4. 每篇檢查 `docs/rag-series-plan.md` 的「寫作原則」與「排版與風格偏好」清單。

## 目前進度（2026-11-23 更新）

- 第 1 篇已發布（2026-08-07）。
- **第 2 篇已發布（2026-11-12，`draft = false`，PR #8 已合併）**（故事篇「沒有珍珠的奶茶不是珍珠奶茶，沒有資料的知識庫不是知識庫」）：兩個惡夢（寫入被拒、搜不到）加小結已成稿；top-k 漏資訊與調降重複判斷門檻移出，留給下一篇。小結由作者改寫（結論：建立 RAG 需要公司上下齊心協力，末尾預告服務啟用前的其他障礙，屬「寫不完」條件下的預告），不加「學到一課」、不收加薪哏。
- **大綱一律視為待定**：章節表、各篇結構都可能在執筆時改掉，規劃文件只記素材與已完成段落，不預先規範走法。文章實際內容以 `content/posts/` 底下的檔案為準。
- 系列命名已統一為 `中年碼農的 AI 職場冒險記`：文章大標題前綴為 `中年碼農的 AI 職場冒險記（N）`，三篇文章的 `topics` 也已一併改為同名（blog 尚未公開，網址變動無影響）。站台 description 同步改為新的敘事定位。
- 原「先搞懂 RAG 是怎麼運作的」草稿（`content/posts/rag/rag-2-how-rag-works/`）已刪除；內容可從 git 歷史取回，素材（開書考試比喻、五步驟流程圖、技術選型）改記在規劃文件。
- PR #7（第 2 篇草稿、系列命名統一、規劃文件與 CLAUDE.md）已於 2026-11-09 合併；之後分支 `claude/new-session-syho52` 新增的 commit（刪除素材草稿、第 3 篇構想、本檔進度）由 PR #9 合併進 master，待作者確認合併。
- **下一篇構想（暫列第 3 篇，未動筆）**：無意中發現 SBE，整理出知識庫指引（A 篇）；QA 工作流（TARS）另開 B 篇。大綱草案與待補素材見規劃文件「第 3 篇（暫，構想中）」。第 2 篇小結的預告句與此篇的落差，作者決定先不處理。
- **新系列「AI 省時小工具」**（給不懂技術的讀者，`content/posts/ai-tools/`）：第 1 篇 LINE 貼圖上架教學已發布（2026-11-16，`draft = false`，PR #10 已合併）。2026-11-25 抗性思辨審查後補上：第一次登錄創作者、「使用 AI」設定與 AI 圖規定、退件常見原因、審查準則連結，步驟五拆成五、六兩步，並預留 9 張截圖位置（固定檔名，見 PR #16）。2026-11-26 作者補齊截圖：範例角色改為卡皮巴拉＋黑頭凱克鸚鵡，切圖到打包在同一個 ChatGPT 對話完成、只下載一次，上架改用電腦網頁（手機版網頁沒有新增功能），按鈕名稱依實際畫面（上傳壓縮檔、送出申請、是否使用AI 在販售資訊）。前言暫用九宮格圖（`line-sticker-sample.png`），貼圖上架後換成貼圖小舖畫面。兩篇封面（`feature.png`）都由 `scripts/make_cover.py` 產生（白底、灰色系列標籤、思源黑體 Bold、圖示用工具品牌色）。第 2 篇 GitHub 註冊與開啟 2FA 教學（`content/posts/ai-tools/github-signup-2fa/`）已發布（2026-11-23，`draft = false`，PR #11 已合併）。粉絲團推廣貼文（中立版）草稿在 `/mnt/project-files/drafts/fb-posts/`，貼文編號 002。第 3 篇「用 ChatGPT 串接 GitHub 做個人網站」（`content/posts/ai-tools/chatgpt-github-pages-website/`）`draft = false` 供 preview 站檢視，流程依作者提供的教學（預設 ChatGPT 可直接推送 commit），Repository 用 `帳號.github.io` 自動上線，文中不提 GitHub Pages 名詞，截圖齊全（作者實測 ChatGPT 可直接推送到 main）；封面新增 `web` 圖示（GitHub 藍 0969da）。
- **AI 省時小工具第 4 篇「不用寫程式：做一個能在 LINE 上報名的官方帳號」**（`content/posts/ai-tools/line-signup-bot/`，`draft = true`）：Make（LINE Watch Events → Router → 「我要報名」回覆格式／「報名」開頭寫入 Google Sheets 並回覆）＋圖文選單「我要報名」按鈕（文字動作）。取代已撤回的圖文選單單篇（PR #18 關閉）。錄影腳本在 `/mnt/project-files/line-signup-bot/recording-script.md`，截圖待作者補；封面新增 `chat` 圖示（LINE 綠 06c755）。
- **網站 icon 統一用「一個人使用電腦」那張**（`assets/img/avatar.png`）：favicon、apple-touch-icon、作者頭像、og:image、封面左下角頭像（`scripts/cover-avatar.png`）都用它，不用戴耳機的卡通頭像（PR #15）。
- side project 下一個里程碑：手刻 RAG 開工（Ollama + Chroma 跑起來）。

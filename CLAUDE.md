# CLAUDE.md

本檔案供 Claude Code 在此 repo 工作時載入的專案記憶。進度或決策有變動時，請一併更新本檔的「目前進度」。

## 專案概觀

- Hugo 部落格「中年碼農的職場奇妙冒險」，主題 Congo，正體中文。
- 部署：merge 進 `master` 即由 Cloudflare Pages 自動建置發布（`hugo --gc --minify`，`HUGO_VERSION=0.145.0`）。
- 目前主線：「新手小白自建 RAG」系列文章，同時把自建 RAG 的過程當 side project 進行——**專案是主，文章是副產品**，有料才寫，不趕進度。

## 單一事實來源

系列規劃、章節狀態、各篇大綱、寫作原則與排版風格偏好，全部以 `docs/rag-series-plan.md` 為準（內部文件，不會被 Hugo 發布）。動筆或 review 前先讀它。

## 工作流程重點

1. 大綱與作者討論定稿 → 作者執筆（`draft = true`，開發於 feature branch）→ 交叉 review（Claude + ChatGPT）→ 作者定稿後 `draft = false` 開 PR。
2. **PR 一律由作者確認後才合併，不自動合併。**
3. 文章內不放系列規劃或下集預告；文末固定加註「*本文由 AI 輔助潤稿*」。
4. 每篇檢查 `docs/rag-series-plan.md` 的「寫作原則」與「排版與風格偏好」清單。

## 目前進度（2026-08-29 更新）

- 第 1 篇已發布（2026-08-07）。
- **第 2 篇**定案為故事篇「沒有珍珠的奶茶不是珍珠奶茶，沒有資料的知識庫不是知識庫」：第一版知識庫（mcp-memory-service + 自寫 Slack bot，尚未接 AI）的四大惡夢。大綱 v3 已定稿（開場拆為「週五幻想／週一開工」兩段），**待作者執筆**，詳見規劃文件內「第 2 篇大綱」。
- 原「先搞懂 RAG 是怎麼運作的」草稿（`content/posts/rag/rag-2-how-rag-works/`）降為素材保留，維持 draft，視各篇需要拆併。
- PR #6（規劃文件更新，分支 `claude/new-session-syho52`）：base 已修正為 master、無衝突，待作者確認合併。
- 待定案兩件：(1) 第 2 篇結尾伏筆方向（接技術篇「為什麼找不到」或接「接上 AI」劇情，視 side project 下一步）；(2) 四大惡夢採目前的「表層→資料層→機制層」順序或改照實際發生順序。
- side project 下一個里程碑：手刻 RAG 開工（Ollama + Chroma 跑起來）。

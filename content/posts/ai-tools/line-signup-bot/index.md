+++
date = '2026-11-26'
draft = true
title = 'AI 省時小工具（4） - 不用寫程式：做一個能在 LINE 上報名的官方帳號'
description = '用 Make 串起 LINE 官方帳號和 Google 試算表，客人在聊天室按「我要報名」、回一句話，報名資料就自動存進試算表，官方帳號也會馬上回覆確認。'
tags = ['LINE 官方帳號', 'Make', 'Google 試算表', 'ChatGPT', '圖文選單']
topics = ['AI 省時小工具']
+++

![line-signup-bot-demo.gif](line-signup-bot-demo.gif "做好之後，客人在 LINE 上報名的樣子")
<!-- GIF：手機打開官方帳號聊天室 → 圖文選單跳出 → 點「我要報名」→ 官方帳號回覆報名格式 → 輸入「報名 王小明 0912345678 2位」→ 官方帳號回覆報名成功 →（切到 Google 試算表）看到新的一列（錄影腳本見 PR 說明） -->

## 前言

上面這段，就是這篇要做出來的東西：客人在 LINE 官方帳號的聊天室按下「我要報名」，官方帳號會告訴他要回什麼；客人照格式回一句話，報名資料就自動寫進 Google 試算表，官方帳號也會馬上回一句「報名成功」。從頭到尾不用寫程式，也不用租主機。

這種會自己回話的官方帳號，一般叫做「LINE Bot」（聊天機器人）。這篇會用一個叫 Make 的自動化工具，把 LINE 官方帳號和 Google 試算表串起來。適合辦課程、講座、團購、小聚，想讓客人直接在 LINE 上報名、自己不用一則一則抄名單的人。第一次做大約需要 1 小時。

【作者補：為什麼想寫這篇，例如自己或朋友辦活動時收報名的經驗】

---

## 動手前

請先準備好：

- 一個 LINE 官方帳號，而且你是管理員。還沒有的話，可以到 [LINE Official Account Manager](https://manager.line.biz/) 免費申請
- 一個 Google 帳號，用來建立試算表
- 一個 Make 帳號。到 [Make 官網](https://www.make.com/) 用 Google 帳號註冊就可以，免費方案就夠用
- 一個 ChatGPT 帳號，最後一步畫選單圖片時會用到
- 一台電腦，所有設定都建議使用電腦操作較為順暢

這篇會用到四個工具：

| 工具 | 在這篇的用途 | 費用 |
| --- | --- | --- |
| LINE 官方帳號 | 客人報名的地方 | 免費方案即可。回覆客人的訊息不算在每月訊息則數內 |
| Make | 收到 LINE 訊息後，判斷要做什麼、寫進試算表、回覆客人 | 免費方案每月 1,000 點（credits），大約可以處理三百多筆報名 |
| Google 試算表 | 存放報名名單 | 免費 |
| ChatGPT | 畫圖文選單的圖片 | 免費版即可 |

整個流程是這樣：

1. 客人按圖文選單的「我要報名」，聊天室送出「我要報名」這句話
2. LINE 把這句話轉給 Make，Make 回覆報名格式
3. 客人回「報名 姓名 電話 人數」
4. Make 把這句話寫進 Google 試算表，再回覆「報名成功」

先講幾個之後會看到的名詞，看過有印象就好：

- **Messaging API**：LINE 官方帳號開放給其他工具串接的功能。打開之後，Make 才收得到客人傳的訊息
- **Webhook**：一個網址。客人傳訊息時，LINE 會把訊息送到這個網址，這篇用的是 Make 產生的網址
- **情境（Scenario）**：Make 裡的一條自動化流程，由好幾個方塊（模組）串起來

---

## 步驟一：建立放報名名單的 Google 試算表

1. 打開 [Google 試算表](https://sheets.google.com/)，建立一個空白試算表，取名為「活動報名」
2. 在第一列依序填入三個欄位名稱：

| A1 | B1 | C1 |
| --- | --- | --- |
| 報名時間 | 報名內容 | LINE 使用者 ID |

「LINE 使用者 ID」是 LINE 給每位客人的一串代碼，不是客人的 LINE 名稱。現在用不到，先留著，之後想個別通知報名的人時會用到。

![google-sheets-signup-header.png](google-sheets-signup-header.png "準備好欄位名稱的試算表")
<!-- 截圖：Google 試算表，第一列已填好「報名時間、報名內容、LINE 使用者 ID」，檔名顯示「活動報名」 -->

---

## 步驟二：打開官方帳號的 Messaging API

這一步要讓官方帳號可以跟 Make 串接，會用到兩個後台：平常管理官方帳號的 LINE Official Account Manager，以及給開發者用的 LINE Developers。

1. 用電腦登入 [LINE Official Account Manager](https://manager.line.biz/)，選擇你的官方帳號
2. 點右上角的 **設定**，再點左側的 **Messaging API**
3. 點 **啟用 Messaging API**
4. 第一次啟用會請你填開發者的姓名和 Email，接著選擇「服務提供者」（Provider）。沒有的話就建立一個新的，名稱填自己或店家的名字

{{< alert >}}
服務提供者選定之後就不能更改，請確認名稱和選擇的是自己的帳號再按確定。
{{< /alert >}}

![line-oa-messaging-api-enable.png](line-oa-messaging-api-enable.png "啟用 Messaging API")
<!-- 截圖：LINE Official Account Manager → 設定 → Messaging API 頁面，用紅框標出「啟用 Messaging API」按鈕（帳號名稱與頭像請打馬賽克；按鈕名稱請對照實際畫面調整） -->

5. 啟用之後，用同一個 LINE 帳號登入 [LINE Developers](https://developers.line.biz/console/)，點剛剛選的服務提供者，再點你的官方帳號
6. 切到 **Messaging API** 分頁，拉到最下面的 **Channel access token**，點 **Issue**，畫面會出現一長串代碼，這就是串接用的「通行證」
7. 切到 **Basic settings** 分頁，拉到最下面找到 **Your user ID**

第 6 步的 Channel access token 和第 7 步的 Your user ID，步驟三都會用到，先不要關掉這個頁面。

![line-developers-channel-access-token.png](line-developers-channel-access-token.png "發行 Channel access token")
<!-- 截圖：LINE Developers → 官方帳號 → Messaging API 分頁最下方的 Channel access token 區塊，用紅框標出 Issue 按鈕（token 請打馬賽克） -->

{{< alert >}}
Channel access token 等於官方帳號的鑰匙，拿到的人就能用你的官方帳號發訊息。不要貼到群組、文章或截圖裡；不小心外流的話，回到同一個地方重新發行一組。
{{< /alert >}}

---

## 步驟三：在 Make 接收 LINE 的訊息

1. 登入 [Make](https://www.make.com/)，點左側的 **Scenarios**，再點右上角的 **Create a new scenario**
2. 點畫面中間的大加號，搜尋 **LINE**，選 **Watch Events**
3. 在 **Webhook** 旁邊點 **Add**，名稱填「LINE 報名」
4. 在 **Connection** 旁邊點 **Add**，貼上步驟二的 **Channel access token** 和 **User ID**，點 **Save**
5. 再點一次 **Save**，Make 會產生一個網址，點 **Copy address to clipboard** 複製起來

![make-line-watch-events.png](make-line-watch-events.png "Make 產生的 Webhook 網址")
<!-- 截圖：Make 的 Watch Events 設定視窗，顯示 Webhook 網址與「Copy address to clipboard」按鈕（網址請打馬賽克） -->

6. 回到 LINE Developers 的 **Messaging API** 分頁，找到 **Webhook settings**，在 **Webhook URL** 點 **Edit**，貼上剛剛複製的網址，點 **Update**
7. 把下方的 **Use webhook** 打開

![line-developers-webhook.png](line-developers-webhook.png "貼上 Webhook 網址並開啟 Use webhook")
<!-- 截圖：LINE Developers → Messaging API 分頁的 Webhook settings 區塊，標出 Webhook URL 與 Use webhook 開關（網址請打馬賽克） -->

8. 回到 Make，點左下角的 **Run once**，Make 會開始等待訊息
9. 用手機打開自己的官方帳號，隨便傳一句話，例如「你好」

Make 的 Watch Events 方塊右上角出現一個數字泡泡，就代表 LINE 的訊息已經送進 Make 了。點開泡泡，可以在 **Events** 裡看到剛剛傳的那句話。

---

## 步驟四：設定客人按「我要報名」時的回覆

接下來要讓 Make 依照客人傳的內容做不同的事：傳「我要報名」就回覆報名格式，傳「報名……」就寫進試算表。Make 裡負責分岔的方塊叫做 **Router**。

1. 在 Watch Events 方塊右邊點一下，加入 **Flow Control** 裡的 **Router**
2. 在 Router 右邊點一下，加入 **LINE** 的 **Send a Reply Message**
3. 填寫以下欄位，要對應的資料從彈出的清單裡點選：

| 欄位 | 填什麼 |
| --- | --- |
| Reply Token | 點選 Watch Events 底下 **Events[]** 裡的 **Reply Token** |
| Messages | 點 **Add item**，類型選 **Text**，貼上下面的文字 |

```text
感謝你報名【週末線上分享會】！
請直接回覆以下格式（中間用空格隔開）：

報名 姓名 電話 人數

例如：報名 王小明 0912345678 2位
```

4. 點 Router 和 Send a Reply Message 之間的連接線，設定篩選條件（Filter）：
   - **Label**：我要報名
   - **Condition**：點選 **Events[]** 裡的 **Message: Text**
   - 比較方式選 **Text operators** 裡的 **Equal to**
   - 下方填「我要報名」

![make-router-filter-equal.png](make-router-filter-equal.png "設定「我要報名」的篩選條件")
<!-- 截圖：Make 的 Filter 設定視窗，Condition 為 Message: Text、Equal to、我要報名（欄位名稱請對照實際畫面調整） -->

這樣只有客人傳的內容剛好是「我要報名」時，才會走這條路線。

---

## 步驟五：把報名資料寫進試算表並回覆

1. 在 Router 上再點一下，拉出第二條路線，加入 **Google Sheets** 的 **Add a Row**
2. 第一次使用時點 **Add** 連結 Google 帳號，依畫面指示登入並允許存取
3. 選擇步驟一建立的「活動報名」試算表和工作表，**Table contains headers** 選 **Yes**，下方就會出現三個欄位名稱
4. 依照下表填入：

| 欄位 | 填什麼 |
| --- | --- |
| 報名時間 | 貼上 `{{formatDate(now; "YYYY/MM/DD HH:mm")}}` |
| 報名內容 | 點選 **Events[]** 裡的 **Message: Text** |
| LINE 使用者 ID | 點選 **Events[]** 裡的 **Source: User ID** |

報名時間那一行是 Make 內建的「現在時間」，直接整段貼上就可以，Make 會自動轉成一個方塊。時間以 Make 帳號設定的時區為準，若和台灣時間差 8 小時，到 Make 右上角的個人設定把時區改成台北。

![make-google-sheets-add-row.png](make-google-sheets-add-row.png "設定要寫進試算表的內容")
<!-- 截圖：Make 的 Google Sheets Add a Row 設定視窗，三個欄位都已填好（Google 帳號 Email 請打馬賽克） -->

5. 在 Add a Row 右邊再加入一個 LINE 的 **Send a Reply Message**，Reply Token 一樣點選 **Events[]** 裡的 **Reply Token**，Messages 的 Text 填：

```text
報名成功！你填的資料是：
【這裡點選 Events[] 裡的 Message: Text】

有問題直接在這裡留言就可以。
```

6. 點 Router 和 Add a Row 之間的連接線，設定篩選條件：
   - **Label**：報名資料
   - **Condition**：點選 **Events[]** 裡的 **Message: Text**
   - 比較方式選 **Text operators** 裡的 **Starts with**
   - 下方填「報名」

完成後，整個情境會長這樣：

![make-scenario-overview.png](make-scenario-overview.png "完成後的 Make 情境")
<!-- 截圖：Make 情境全貌：Watch Events → Router → 上方路線 Send a Reply Message，下方路線 Add a Row → Send a Reply Message，兩條連接線上都有篩選圖示 -->

「我要報名」是「我要」開頭，不會被第二條路線誤判；客人傳其他聊天內容時，兩條路線都不會走，Make 不會回覆，你可以在官方帳號後台自己回。

---

## 步驟六：開啟情境，用手機測試

1. 在 Make 點左下角的 **Save**，再把 **Immediately as data arrives** 旁的開關打開。情境打開之後，Make 才會一直接收 LINE 的訊息
2. 回到 LINE Official Account Manager 的 **設定** → **回應設定**，確認 **Webhook** 是開啟的
3. 把 **自動回應訊息** 關掉，避免官方帳號和 Make 同時回覆。**聊天** 可以保持開啟，客人問其他問題時你還是能在後台手動回覆

![line-oa-response-settings.png](line-oa-response-settings.png "回應設定")
<!-- 截圖：LINE Official Account Manager → 設定 → 回應設定，標出 Webhook 與自動回應訊息的開關（項目名稱請對照實際畫面調整） -->

4. 用手機打開官方帳號，依序傳「我要報名」和「報名 王小明 0912345678 2位」
5. 打開 Google 試算表，確認多了一列報名資料

沒有反應時，可以照下表檢查：

| 狀況 | 檢查這裡 |
| --- | --- |
| 傳什麼都沒有回覆 | Make 的情境開關有沒有打開；LINE Developers 的 Use webhook 有沒有打開 |
| 官方帳號回了兩次 | 回應設定裡的自動回應訊息有沒有關掉 |
| 有回覆，但試算表沒有資料 | Add a Row 選的試算表和工作表對不對；第一列有沒有欄位名稱 |
| 傳「報名」開頭的內容沒反應 | 篩選條件是不是 Starts with，「報名」前面有沒有多打空格 |
| 想看哪裡出錯 | Make 情境頁面上方的 **History**，可以看到每一次執行的紀錄 |

---

## 步驟七：做一個有「我要報名」按鈕的圖文選單

最後在聊天室下方放一個按鈕，客人不用自己打字就能開始報名。按鈕的設定和選單圖片的做法，比照一般的圖文選單：

1. 打開 ChatGPT，把下面這段貼上，【】的地方換成你自己的內容：

```text
請幫我畫一張 LINE 官方帳號的圖文選單圖片。

- 帳號：【週末線上分享會，風格簡潔、親切】
- 版面：橫式，兩列兩欄，共四個大小相同的格子，格子之間用細線分開
- 每格放一個簡單的圖示，圖示下方放按鈕文字
- 按鈕文字（由左到右、由上到下）：
  【我要報名、活動介紹、常見問題、聯絡我們】
- 文字要大、清楚，使用正體中文，不要放其他文字

畫好之後，請把圖片調整成寬 2500 像素、高 1686 像素，
不要變形，邊緣不夠的地方用背景色補滿，
存成 JPG，檔案大小在 1MB 以內，並給我下載連結。
```

2. 下載前確認每一格的中文字沒有寫錯，下載後確認圖片尺寸是 2500 × 1686
3. 回到 LINE Official Account Manager，在 **主頁** 左側的 **聊天室相關** 點 **圖文選單**，再點 **建立圖文選單**
4. 填好 **標題**（客人看不到）和 **使用期間**
5. **版型** 選大型裡面兩列兩欄的四格版型，**圖片** 上傳剛剛下載的圖
6. 「我要報名」那一格的動作，類型選 **文字**，內容填「我要報名」。這裡的文字要和步驟四篩選條件填的一模一樣
7. 其他三格類型選 **連結**，填入活動介紹頁、常見問題頁的網址，或是你的聯絡方式
8. **選單列顯示文字** 填「點我報名」這類提示，**預設顯示** 選顯示，點 **儲存**

![line-oa-richmenu-signup-action.png](line-oa-richmenu-signup-action.png "「我要報名」按鈕設定成送出文字")
<!-- 截圖：圖文選單建立頁，已上傳選單圖片，「我要報名」那一格的動作類型為「文字」、內容為「我要報名」（類型名稱請對照實際畫面調整） -->

儲存之後用手機打開聊天室，點「我要報名」，官方帳號應該會回覆步驟四設定的報名格式。選單有時候要過幾分鐘才會出現，圖文選單也只會顯示在手機版 LINE，電腦版看不到。

---

## 常見問題

**免費方案夠用嗎？**

Make 免費方案每月有 1,000 點，每個方塊執行一次大約用 1 點。這篇的情境，客人傳一次「我要報名」大約用 2 點，送出一筆報名大約用 3 點，一般小型活動每月幾十到一兩百筆報名都夠用。LINE 這邊，回覆客人的訊息不算在官方帳號的每月訊息則數裡，所以也不會用到免費額度。

**可以把姓名、電話、人數分成不同欄位嗎？**

可以。最簡單的方式是在 Google 試算表選取「報名內容」那一欄，點上方的 **資料** → **將文字分割成欄**，分隔符選空格，就會自動拆成好幾欄。

**客人格式打錯怎麼辦？**

只要是「報名」開頭，內容就會原封不動存進試算表，你看名單時再確認就好。完全沒照格式的訊息不會觸發 Make，會留在官方帳號的聊天裡，可以手動回覆。

**可以控制名額，額滿就自動回覆嗎？**

可以，在 Make 裡先查試算表目前有幾列，再決定回「報名成功」還是「已額滿」，但步驟比較多，這篇先不寫。

---

## 小結

這個官方帳號用到的工具都有免費方案：LINE 負責跟客人對話，Google 試算表負責存名單，Make 在中間把兩邊接起來。之後辦新的活動，只要改回覆的文字和圖文選單，同一個情境就能繼續用。

如果你想做名額控管、活動前自動提醒，或是讓官方帳號用 AI 回答客人的問題，又不想自己動手，可以到[關於我]({{< ref "/about" >}})看看我能幫上什麼忙。

---

### 參考資料

- [Get started with the Messaging API｜LINE Developers](https://developers.line.biz/en/docs/messaging-api/getting-started/)
- [Messaging API pricing｜LINE Developers](https://developers.line.biz/en/docs/messaging-api/pricing/)
- [LINE｜Make Apps Documentation](https://apps.make.com/line)
- [Make Pricing](https://www.make.com/en/pricing)
- [Rich menus｜LINE Official Account Manager manual](https://linebiz.com/jp-en/manual/OfficialAccountManager/rich-menus)

---

*本文由 AI 輔助潤稿*

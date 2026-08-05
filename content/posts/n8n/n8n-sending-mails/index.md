---
title: "我在現實生活中用 n8n 開外掛(2) - 透過 Gmail SMTP server 寄信"
description: "教你申請 Google 應用程式密碼,在 n8n 設定 Gmail SMTP 憑證與 Send Email 節點,實現自動化寄信,新手也能快速上手。"
date: 2025-06-11
draft: false
tags: [ 'n8n', '自動化', 'Triggers' ]
topics: [ "我在現實生活中用 n8n 開外掛" ]
---

在現實生活中，無論是聯絡親友、報名課程，甚至是跟主管約定開會的時間，我們經常需要寄送信件來處理。
而`n8n`與多種第三方服務進行整合，於是我們在接下來的內容中，將學習如何透過`n8n`和`Gmail SMTP server`寄信來實現自動化寄信功能，在日常工作或個人專案中提升效率。  

## 申請 Google 應用程式密碼
在進入`n8n`之前，我們先申請`Google`應用程式密碼，以使用`Gmail SMTP server`：

{{< alert "circle-info" >}}
應用程式密碼是一個 16 位數密碼，可讓安全性較低的應用程式或裝置存取您的`Google`帳戶，進而使用一些`Google`的服務。
{{< /alert >}}

1. 確認您的`Google`帳戶已啟用[兩步驟驗證](https://support.google.com/accounts/answer/185839)。
2. 建立[應用程式密碼](https://support.google.com/accounts/answer/185833)。

## 編輯畫布

### **加入 Trigger Manually 節點**
1. 新建立一個工作流程後，點擊畫布上的`Add first step...`按鈕，在右側欄上找到`Trigger Manually`節點。或是在畫布上工作時，按下鍵盤上的
   `tab`按鍵，即可呼叫出右側欄，並在右側欄上搜尋`Trigger Manually`節點。
2. 點擊或拖曳節點到畫布上即可。

{{< alert "circle-info" >}}
手動觸發器 `Trigger Manually`，是手動啟動工作流程的節點，通常用於測試或開發階段。我們也可以輸入一些數據當作假資料或是初始資料，作為工作流程的輸入。
![trigger_manually.png](trigger_manually.png "手動觸發器 `Trigger Manually`")

當模板中有手動觸發器節點時，模板上會出現`Test workflow`按鈕。按下`Test workflow`按鈕，即可執行這個工作流程。
{{< /alert >}}

#### **輸出**

`Trigger Manually`預設沒有任何輸出值，但我們可以放一些假資料做為初始資料：

1. 在`Trigger Manually`上用滑鼠左鍵點兩下，即可檢視節點詳細資料。
2. 在`OUTPUT`區域中，點擊`set mock data`或右上角的編輯按鈕，開啟`OUTPUT`編輯視窗。
3. 這時編輯框中已經填入了一些資料，但我們依然可以填入一些自訂的資料，例如：
   ```json
   [
     {
       "email": "<test email address>",
       "subject": "Test Email",
       "body": "This is a test email sent from n8n."
     }
   ]
   ```

### **加入 Send Email 節點**

1. 在`Trigger Manually`節點右側的`+`點一下，搜尋並選擇`Send Email`節點，系統會自動要求輸入參數。
2. 在`Send Email`的編輯畫面中間版面中，`parameters`的`Credential to connect with`欄位中選擇`Create new credentials`。
   {{< figure src="create_new_credentials.png">}}
3. 在彈出的視窗中輸入`SMTP server`連線資訊，輸入完成後點擊`Save`按鈕，系統會自動為我們測試連線。
   - User: 輸入您的 Gmail 信箱
   - Password: 輸入剛剛建立的應用程式密碼
   - Host: smtp.gmail.com
   - Port: 465

   {{< figure src="smtp_connection.png">}}
4. 回到`parameters`，輸入其他欄位資料：
   - From Email: 信件上顯示的寄件人，例如：Nathan Doe \<nate@n8n.io\>
   - To Email: 收件人，例如：Jane Doe \<jane@n8n.io\>
   - Subject: 信件主旨
   - Email Format: 信件本文的格式，我們先使用 `Text`。
   - Text: 信件本文  
  
   上述資料也可以使用表達式來引用 `Trigger Manually` 節點的輸出資料，如下圖操作：
   {{< figure src="email_info.png">}}

5. 完成後點擊上方的`Test step` 按鈕，可單獨執行該節點，執行成功的話，`OUTPUT`版面會返回寄信的相關`meta`資料，其中的`response`欄位會有`OK`的文字。
   {{< figure src="send_successfully.png">}}
6. 最後您的畫布應該會長這樣：
   {{< figure src="completion.png">}}
   接著就可以去收信看看了。

## 小結
在這篇文章中，我們學習了如何透過`n8n`與`Gmail SMTP server`整合來實現自動化寄信，並且介紹了`n8n`中的手動觸發器節點 `Trigger Manually`，展示了如何手動啟動工作流程。希望這些內容能幫助你更加熟悉`n8n`的強大功能！未來我們還會帶來更多精彩教學，敬請期待！

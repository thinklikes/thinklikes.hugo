+++
lastmod = '2025-04-22'
date = '2025-04-18'
draft = true
title = 'Golang 新手村(1) - Golang 基本語法'
description = '以新手視角導讀 A Tour of Go,認識 package、import 與 main 函式等 Golang 基本語法結構,踏出成為 Go 冒險者的第一步。'
tags = ['golang']
categories = ['golang 新手村']
+++

## 前言
各位勇者，歡迎降臨 Golang 新手村！你是不是渴望著操控程式之力？這裡就是你的起點，讓我們一同修煉 Go 能力吧！

我們的第一個任務是要來了解 Golang 的基本語法，認識基本的語法結構。
{{< alert type=tip title="Tips" open=true >}}
這個系列的文章將會引用官網中 <<A Tour of Go>> 一系列的範例程式。  
出處：
[A Tour of Go" title="A Tour of Go](https://go.dev/tour/list)


{{< /alert>}}

## 新手村使用說明
1. 所有的教學任務會以一個新手的觀點來撰寫，從最基本的語法開始介紹，並且附上範例程式碼。
2. 範例程式碼大部分官網取得並僅止於引用，可從連結進入原始網頁中，按下`Run`按鈕測試。
ˇ範例程式碼若有附註，會使用下列幾種區塊來說明：

    {{< alert type=tip title="Tips" open=true >}}
    
用於提供一些建議或備註的區塊，讓使用者可以更加了解程式碼的使用方式或注意事項。
    
    {{< /alert>}}

    {{< alert type=warning title="Warnings" open=true >}}

用於告知有可能會引發錯誤或需要特別注意的區塊，讓使用者可以更加小心地使用。

    {{< /alert>}}

   {{< alert type=question title="Questions" open=true >}}

用於提供一些問題或疑問的區塊，讓使用者可以思考或討論。

   {{< /alert>}}

---

## 拿出你的鍵盤吧！
冒險者們，你不會這樣就慌張了吧？作為一位初心者，首先要做的是保持冷靜，先不要慌。

想像著我們轉生前就讀國小一年級時，看到課本上一大坨文字難免會慌張。而這時老師帶著我們一個字一個字讀完，並且講解文字的意思，我們就是用這樣的方式開始熟悉文字。

經過約十來年的訓練，我們才能夠毫不費力地閱讀文章。閱讀程式語言也是需要透過密集的練習才能夠熟悉的。  

---
這是[第一個任務](https://go.dev/tour/basics/1)，讓我們來看看這段程式碼：
```golang
package main

import (
    "fmt"
    "math/rand"
)

func main() {
    fmt.Println("My favorite number is", rand.Intn(10))
}

```
#### 說明
```golang
package main
```
Golang 開發規範中， `package main` 這一句宣告語句須放在第一行，代表當前的檔案屬於 `main` package。  
package 是一種組成程式碼的方式，把相關的函式、變數和資源組織在一起，以保持程式碼的整潔。  
你可以想像成一個資料夾，裡面放著許多相關的檔案。

***

```golang
import (
    "fmt"
    "math/rand"
)
```
目前的程式中引用了 packages `fmt` 與 `math/rand`。  
`fmt` 是一個內建的 package，在這裡我們用來印出指定的文字。  
`math/rand` 是另一個內建的 package，提供隨機數字的產生器，這裡我們用來產生 0 到 10 的隨機數字。


{{< alert type=tip title="Tips" open=true >}}
我們可以將 import 的 packages 放在一起，這樣可以讓程式碼更簡潔。
```golang
import (
    "fmt"
    "math/rand"
)
```

你也可以將它們分開來
```golang
import "fmt"
import "math/rand"
```
{{< /alert >}}

***

```golang
func main() {
    fmt.Println("My favorite number is", rand.Intn(10))
}
```
`func main()` 是目前這個程式的主函式，這是程式的進入點。意即執行該檔案時，會預設執行這個函式中的程式碼。  
`fmt.Println("My favorite number is", rand.Intn(10))` 是用來印出文字的指令，這裡我們印出了隨機數字的文句。
`rand.Intn(10)` 是產生隨機 1 到 10 的整數。

## 小結
冒險者們！幹得不錯，你已經通過了第一項考驗了！相信你已經開始熟悉 Golang 程式碼區塊是怎麼分佈的了，是不是已經隱隱約約知道怎麼操控 Golang 之力了呢？
想要細細品味其中原理，那就往下一個任務前進吧！

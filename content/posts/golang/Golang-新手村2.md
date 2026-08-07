+++
lastmod = '2025-04-22'
date = '2025-04-22'
draft = true
title = 'Golang 新手村(2) - 函式'
tags = ['golang']
categories = ['golang 新手村']
+++

## 前言
各位勇者，前一次的任務還順利嗎？
今天要連續做幾個任務，是包含了函式的介紹。什麼是函式呢？

## 拿出你的鍵盤吧！
[第二個任務](https://go.dev/tour/basics/6)在這裡，讓我們來看看這段程式碼：
```golang
package main

import "fmt"

func swap(x, y string) (string, string) {
	return y, x
}

func main() {
	a, b := swap("hi", "John")
	fmt.Println(a, b)
}
```

### 說明

```golang
func swap(x, y string) (string, string) {
	return y, x
}
```
Golang 的函式是由定義函式的關鍵字、函式名稱、參數類型和回傳值類型組成的。  
`func`是 Golang 中定義函式的關鍵字。 
其中`swap`是函式名稱，`x, y string`是參數。`x`與`y`是參數名稱，`string`是參數類型。
上述函式的功能是將輸入的兩個文字交換順序。

{{< alert "lightbulb" >}}
  1. 函式可以攜帶 0 個或多個參數，並且可以有 0 個或多個回傳值。
  2. `x, y string` 是 `x string, y string` 的簡寫。
{{< /alert >}}
{{< alert "triangle-exclamation" >}}
  參數類型或回傳值類型必須寫在名稱之後，例如：
  ```golang
  x, y int
  ```
{{< /alert >}}

## 小結

"""「AI 省時小工具」系列封面產生器（白底極簡、固定版型，每篇只換標題、主色、圖示）。

用法：
  python3 scripts/make_cover.py --num 2 --title "註冊 GitHub" --title "開啟兩步驟驗證" \
      --color 1f883d --icon lock --out content/posts/ai-tools/<slug>/feature.png

輸出 1200x630 PNG，檔名須為 feature.png，Congo 才會當成封面。
"""
import argparse
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630
FONT = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
AVATAR = os.path.join(os.path.dirname(__file__), "cover-avatar.png")
SERIES = "AI 省時小工具"
SITE = "中年碼農的職場奇妙冒險"
INK = (31, 35, 40)
MUTED = (101, 109, 118)
LINE = (216, 222, 228)


def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def tint(c, a):
    """主色與白色混合，a=0 為白、a=1 為主色。"""
    return tuple(round(255 + (x - 255) * a) for x in c)


def icon_lock(d, cx, cy, c):
    d.rounded_rectangle([cx - 52, cy - 105, cx + 52, cy + 10], 52, outline=c, width=26)
    d.rounded_rectangle([cx - 85, cy - 30, cx + 85, cy + 110], 22, fill=c)
    d.ellipse([cx - 17, cy + 10, cx + 17, cy + 44], fill="white")
    d.rectangle([cx - 7, cy + 30, cx + 7, cy + 75], fill="white")


def icon_sticker(d, cx, cy, c):
    d.rounded_rectangle([cx - 95, cy - 95, cx + 95, cy + 95], 36, fill=c)
    d.polygon([(cx + 95, cy + 25), (cx + 25, cy + 95), (cx + 95, cy + 95)], fill="white")
    d.polygon([(cx + 95, cy + 25), (cx + 25, cy + 95), (cx + 45, cy + 45)], fill=tint(c, 0.45))
    d.ellipse([cx - 50, cy - 40, cx - 22, cy - 12], fill="white")
    d.ellipse([cx + 10, cy - 40, cx + 38, cy - 12], fill="white")
    d.arc([cx - 55, cy - 20, cx + 45, cy + 50], 20, 160, fill="white", width=12)


ICONS = {"lock": icon_lock, "sticker": icon_sticker}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--num", required=True)
    p.add_argument("--title", action="append", required=True, help="標題，一行一個，最多兩行")
    p.add_argument("--color", required=True, help="主色 hex，例如 1f883d")
    p.add_argument("--icon", choices=ICONS, required=True)
    p.add_argument("--icon-color", help="圖示顏色 hex，預設同主色")
    p.add_argument("--gradient", action="store_true", help="圖示帶由上往下的白色漸層")
    p.add_argument("--gray-circle", action="store_true", help="圖示背後的圓用淺灰，不用主色")
    p.add_argument("--no-bar", action="store_true", help="不畫左側色條")
    p.add_argument("--font", default=FONT, help="標題與標籤的字型檔路徑")
    p.add_argument("--out", required=True)
    a = p.parse_args()
    c = hex2rgb(a.color)

    img = Image.new("RGB", (W, H), "white")
    d = ImageDraw.Draw(img)
    f = lambda s: ImageFont.truetype(a.font, s)

    # 左側主色條
    if not a.no_bar:
        d.rectangle([0, 0, 16, H], fill=c)

    # 系列標籤
    label = f"{SERIES}（{a.num}）"
    lf = f(30)
    lw = d.textlength(label, font=lf)
    d.rounded_rectangle([80, 90, 80 + lw + 44, 90 + 56], 28, fill=tint(c, 0.12))
    d.text((102, 118), label, font=lf, fill=c, anchor="lm")

    # 標題（字級依最長一行自動縮小）
    size = 84
    while max(d.textlength(t, font=f(size)) for t in a.title) > 640 and size > 48:
        size -= 2
    tf = f(size)
    y = 200
    for t in a.title:
        d.text((80, y), t, font=tf, fill=INK)
        y += int(size * 1.3)

    # 右側圖示：先畫純色，再把純色部分換成「上淺下深」的白色漸層
    ic = hex2rgb(a.icon_color) if a.icon_color else c
    cx, cy = 960, 290
    d.ellipse([cx - 160, cy - 160, cx + 160, cy + 160], fill=(242, 244, 246) if a.gray_circle else tint(ic, 0.1))
    box = (cx - 120, cy - 120, cx + 120, cy + 120)
    layer = Image.new("RGB", (W, H), (0, 0, 0))
    ICONS[a.icon](ImageDraw.Draw(layer), cx, cy, ic)
    mask = Image.new("L", (box[2] - box[0], box[3] - box[1]), 0)
    px, mp = layer.crop(box).load(), mask.load()
    bw, bh = box[2] - box[0], box[3] - box[1]
    grad = Image.new("RGB", (bw, bh))
    gp = grad.load()
    top = tint(ic, 0.45) if a.gradient else ic
    for yy in range(bh):
        t = yy / (bh - 1)
        col = tuple(round(top[i] + (ic[i] - top[i]) * t) for i in range(3))
        for xx in range(bw):
            gp[xx, yy] = col
            mp[xx, yy] = 255 if px[xx, yy] == ic else 0
    img.paste(grad, box[:2], mask)

    # 底部：分隔線＋頭像＋站名
    d.line([80, 500, W - 80, 500], fill=LINE, width=2)
    av = Image.open(AVATAR).convert("RGBA").resize((72, 72), Image.LANCZOS)
    mask = Image.new("L", (72, 72), 0)
    ImageDraw.Draw(mask).ellipse([0, 0, 71, 71], fill=255)
    img.paste(av, (80, 530), mask)
    d.text((172, 566), SITE, font=f(28), fill=MUTED, anchor="lm")

    img.save(a.out, optimize=True)


if __name__ == "__main__":
    main()

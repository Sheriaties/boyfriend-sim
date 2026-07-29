#!/usr/bin/env python3
"""
D3 大事件（商场逛街）素材生成脚本
========================================
用法:
  export OPENROUTER_API_KEY=sk-or-...
  python3 scripts/gen_d3_mall_assets.py [asset_name]

支持的 asset_name:
  bg_mall              商场横向长条背景
  sprite_plushie_stand 玩偶摊 sprite
  sprite_katsu_shop    炸猪排店 sprite
  cg_mall_pv           成功后的 PV（床上两玩偶亲密温馨）
  bg_bedroom_empty     卧室白天空床版（无玩偶）
  all                  一次性生成以上全部

角色一致性：cg_mall_pv 会自动带 heroine_idle.png 作为参考。
玩偶参考：会自动裁 bg_bedroom.png 中的兔+企鹅区域作为 ref。
"""

import os, sys, json, base64, urllib.request, pathlib

API_KEY = os.environ.get("OPENROUTER_API_KEY")
if not API_KEY:
    sys.exit("请先 export OPENROUTER_API_KEY")

ROOT   = pathlib.Path(__file__).parent.parent
ASSETS = ROOT / "assets"
CHARS  = ASSETS / "characters"

MODEL = "google/gemini-3.1-flash-lite-image"

def gen(prompt: str, out_path: pathlib.Path, refs: list[pathlib.Path] = None):
    """调 OpenRouter 生成一张图，保存到 out_path。"""
    print(f"→ 生成: {out_path.name}")
    content = [{"type":"text","text":prompt}]
    for r in (refs or []):
        if r.exists():
            b64 = base64.b64encode(r.read_bytes()).decode()
            content.append({"type":"image_url","image_url":{"url":f"data:image/png;base64,{b64}"}})
            print(f"    ref: {r.name}")
        else:
            print(f"    (ref missing: {r.name})")
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions", method="POST",
        headers={"Authorization": f"Bearer {API_KEY}",
                 "Content-Type": "application/json"},
        data=json.dumps({"model": MODEL,
            "messages":[{"role":"user","content":content}],
            "modalities":["image","text"]}).encode(),
    )
    with urllib.request.urlopen(req, timeout=180) as r:
        data = json.loads(r.read())
    url = data["choices"][0]["message"]["images"][0]["image_url"]["url"]
    out_path.write_bytes(base64.b64decode(url.split(",", 1)[1]))
    print(f"    ✓ 已保存: {out_path.relative_to(ROOT)}")

# --------- 各素材的 prompt & refs ---------

def gen_bg_mall():
    gen(
        prompt=(
            "A wide horizontal MODERN shopping mall interior background — "
            "clean bright atrium with WHITE POLISHED MARBLE FLOOR (glossy, reflective), "
            "high glass ceiling with soft daylight streaming down, "
            "sleek modern storefronts on both sides with large glass windows, "
            "subtle brand-neutral shop signage, glass railings and escalator hints in background, "
            "warm cool-toned lighting, potted decorative plants along the walkway, "
            "empty middle ground so shops can be placed on top later, "
            "pixel-art style similar to Stardew Valley precision but with a MODERN CONTEMPORARY urban look — "
            "NOT japanese, NOT retro, NOT wooden. "
            "Soft palette dominated by whites, light greys, glass reflections, warm accent lights. "
            "16:9 or wider banner, no people, flat front view, clean composition. "
            "Aspect ratio 21:9 recommended if possible."
        ),
        out_path=ASSETS / "bg_mall.png",
    )

def gen_sprite_plushie_stand():
    gen(
        prompt=(
            "A standalone kawaii plushie market stall SPRITE with FULLY TRANSPARENT BACKGROUND (alpha channel). "
            "IMPORTANT: NO bedroom, NO wall, NO floor, NO pillows behind the stall. "
            "Only draw the stall itself floating on transparency. "
            ""
            "The stall: a small wooden counter with a soft pastel pink-and-white striped canopy above, "
            "supported by two thin wooden posts. "
            ""
            "On top of the counter, TWO plushies sit side by side: "
            "LEFT — a plush lop-eared rabbit with a PURE WHITE BODY, long floppy ears whose INSIDES are SOFT PINK "
            "(only the ear-linings are pink, the rest of the rabbit is entirely white with subtle cream shading). "
            "Small blushing cheeks, big shiny eyes, sitting cutely. "
            "RIGHT — a chubby penguin plush, dark blue-grey back, white belly, small yellow beak, tiny grey scarf. "
            ""
            "In FRONT of the counter, two small wooden hand-written name tags: "
            "LEFT tag reads '卢米·紫水晶' (Chinese Simplified). "
            "RIGHT tag reads '大奥利' (Chinese Simplified). "
            "No English text anywhere. "
            ""
            "Pixel-art style, flat front view, drop shadow only under the stall itself, "
            "no environment, no scenery, just the stall as a game sprite with transparent background. "
            "Compact composition, aspect ratio around 4:3 or square."
        ),
        out_path=ASSETS / "sprite_plushie_stand.png",
        refs=[],
    )

def gen_sprite_katsu_shop():
    gen(
        prompt=(
            "A small Japanese tonkatsu (fried pork cutlet) food stall in pixel-art style, "
            "warm wooden counter, red-and-white striped awning, "
            "big glowing Japanese-style signage that reads 'とんかつ' or 'カツ', "
            "steam rising from a display plate of golden fried cutlets, "
            "inviting and mouth-watering, transparent background, flat front view, "
            "no people, no ground shadow."
        ),
        out_path=ASSETS / "sprite_katsu_shop.png",
    )

def gen_cg_mall_pv():
    gen(
        prompt=(
            "STRICTLY follow the art style of the FIRST reference image (soft cel-shaded modern anime, "
            "clean detailed line art, gentle rim lighting, warm blush tones, dreamy shallow depth of field). "
            "Do NOT use pixel art. Do NOT use flat kawaii illustration. Use detailed anime rendering. "
            ""
            "Scene: golden late afternoon light streaming diagonally through a bedroom window (off-frame). "
            "Composition: medium close-up focused on the head of a made-up bed with soft cream pillows and warm beige sheets. "
            "On the pillows, side by side and leaning gently against each other in a warm intimate pose: "
            ""
            "(A) LEFT plushie — a lop-eared rabbit. Its BODY IS PURE WHITE (creamy, snowy fluff). "
            "ONLY the INSIDES of its long floppy ears are SOFT PINK. "
            "The rest of the rabbit (head, body, arms, legs) is entirely WHITE. "
            "Big shiny eyes, small pink blushing cheeks. NOT a purple rabbit — WHITE with pink ear-linings. "
            ""
            "(B) RIGHT plushie — a chubby penguin, dark blue-grey back, white belly, small yellow beak, tiny grey scarf. "
            ""
            "Their heads slightly touching. Soft golden hour rim light on both plushies. "
            "Soft focus background, no humans in the frame at all, no text, no name tags. "
            "Aspect ratio 16:9. Anime PV cover-quality illustration."
        ),
        out_path=ASSETS / "cg_mall_pv.png",
        refs=[ASSETS / "cg_fireworks_pov_turn.png"],
    )

def gen_bg_bedroom_empty():
    gen(
        prompt=(
            "Reproduce the reference bedroom scene EXACTLY, preserving: same camera angle (front flat view), "
            "same room layout, same bed position and shape, same headboard, same nightstand and lamp, "
            "same wall art, same floor, same wall color, same lighting, same pixel-art rendering style. "
            "The ONLY difference: the two plushies that were sitting on the pillows must be REMOVED. "
            "The pillows should be bare, neatly plumped, nothing on top. "
            "Everything else IDENTICAL to the reference. No people. No text. "
            "Match the pixel-art precision of the reference image exactly."
        ),
        out_path=ASSETS / "bg_bedroom_empty.png",
        refs=[ASSETS / "bg_bedroom.png"],
    )

TARGETS = {
    "bg_mall":              gen_bg_mall,
    "sprite_plushie_stand": gen_sprite_plushie_stand,
    "sprite_katsu_shop":    gen_sprite_katsu_shop,
    "cg_mall_pv":           gen_cg_mall_pv,
    "bg_bedroom_empty":     gen_bg_bedroom_empty,
}

def main():
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    if which == "all":
        for name, fn in TARGETS.items():
            try:
                fn()
            except Exception as e:
                print(f"  ✗ {name} 失败: {e}")
    elif which in TARGETS:
        TARGETS[which]()
    else:
        sys.exit(f"未知素材: {which}\n可用: {', '.join(list(TARGETS) + ['all'])}")

if __name__ == "__main__":
    main()

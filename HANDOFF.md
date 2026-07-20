# HANDOFF — 项目交接文档

> 用于在多台电脑之间同步开发进度。**每次做完一件事都更新这个文件**，别的机器 pull 下来就知道现状。

**最后更新**: 2026-07-20
**仓库**: https://github.com/Sheriaties/boyfriend-sim

---

## 项目一句话

给女朋友玩的**横版点按恋爱养成小游戏**。同居情侣视角，Q版/像素/蜡笔混搭画风，AI 生成素材。目标游玩时长约 1 小时，多结局。

---

## 已完成 ✅

### 场景 & 素材
- **场景**：客厅（起点）⇄ 卧室（loft 夹层，上楼）⇄ 厕所（右下）；书房已废弃
- **背景图**：`bg_living.png`、`bg_bedroom.png`、`bg_bathroom.png`（细腻像素风，flat 正视角）
- **男主立绘**：`hero_idle`、`hero_computer`（坐姿）、`hero_sad/tired/angry/love/shy/horny`、`hero_sofa/bed/bunny/penguin/toilet/sink/shower`、`hero_fat`（Bad End 已弃用图）
- **女主立绘**：`heroine_idle`、`heroine_idle_glasses`（樱桃红tank+低马尾+黑裤，v5定稿）
- **物品 sprite**：`computer_desk` / `sofa` / `pendant_lamp` / `toilet` / `sink` / `shower` / `shelf`（含薯片袋）/ `chip_bag`
- **数值图标**：`icon_love`（爱心）/ `icon_passion`（烈焰）/ `icon_understanding`（灯泡）/ `icon_stress`（铁球锁链）
- **主线 CG**：`cg_argue.png`（涂鸦风+对话气泡山）、`cg_walk.png`（蜡笔风夜色散步）、`cg_walk_hold.png`（牵手特写）
- 所有 sprite 白底已后处理成透明

### 系统
- **顶部 HUD**：像素风分段进度条 + 4 个图标 + 时钟（`第N天 HH:MM`）
- **时间系统**：每次交互 +3 小时，>=22:00 男主自动说想睡觉 → 跳次日 07:00，压力-10 了解度+2
- **场景切换**：不消耗时间（`nav-arrow` 走 `data-nav`）
- **开场取名**：`heroName` 存 state，对话用 `showDialog('@bf', ...)` 自动替换
- **薯片 Bad End**：连喂 10 次，每次男主 scale ×1.05（≤ 1.65 封顶不出屏），第 10 次触发全屏黑幕 + BAD END 文字（无图）
- **点电脑弹三选项菜单**：玩游戏 / 看剧 / 工作，分别不同数值
- **吊灯开关灯**：点吊灯弹菜单，暗色 overlay
- **CG 播放系统**：`cgShow(img)` + `cgSay(speaker, text)` + `cgChoose(options, timeoutMs)`
- **散步剧情**：外出满 3 次自动触发，4 选项 + 4 秒不选自动牵手
- **争吵剧情**（`triggerArgueStory`）：写好但没自动触发钩子，需要通过开发者面板测试或加 gameTime>=7天判断
- **接吻剧情**：占位版（用 `cg_argue.png` + 台词）
- **开发者面板**：`~`键 或 右上 ⚙ 按钮打开

---

## 待办 📋 （按优先级）

### 高优
- [ ] **接吻 CG** 单独生成一张（Love Choice 蜡笔风，男主亲女主脸颊/嘴角）
- [ ] **争吵剧情自动触发**：加日期检查 `if (day >= 8 && !state.argueDone) triggerArgueStory()`，放在 `advanceTime()` 里
- [ ] **主界面**：新游戏 / 载入游戏（用户之前提过但参考图没附上，等他补图）
- [ ] **互动立绘挂钩**：点沙发/床/兔兔/企鹅/水槽/淋浴/马桶时，切换到对应 `hero_xxx.png` 姿势（跟坐电脑一样的机制）

### 中优
- [ ] **完整剧情线**：写一小时的剧情，含 3-5 章 + 5 个结局（True/Sweet/Bittersweet/Cold War/薯片）
- [ ] **数值可视化优化**：数值到 0/100 时给弹窗警告
- [ ] **音效**：至少加个 BGM 和几个点按音效

### 低优
- [ ] 存档/读档系统改造（现在只有一个 localStorage 槽）
- [ ] 手机竖屏适配（现在是 16:9 横版）
- [ ] 上线前删掉所有 `dev-toggle` / `dev-panel` / `dev_*` 函数（grep 一下就找到）

---

## 开发者面板用法 ⚙️

**打开**：游戏内按 `~` 或点右上齿轮 ⚙

**功能**：
- ▶ 触发散步剧情
- ▶ 触发争吵剧情
- ▶ 触发和好接吻
- 💀 触发薯片 Bad End
- 4 条数值滑块（0–100 直改）
- ⏩ +6 小时 / +1 天 / 跳到第 8 天
- 外出次数 +1、薯片次数 +1
- 🔲 显示所有热区框
- 🗑 重置存档

删除入口：搜 `dev-toggle` `dev-panel` `dev_` 全删。

---

## 目录结构

```
game/
  index.html                    # 唯一入口，包含所有 CSS/JS
  README.md
  HANDOFF.md                    # ← 你正在看的这个
  .gitignore
  assets/
    bg_living.png bg_bedroom.png bg_bathroom.png
    cg_argue.png cg_walk.png cg_walk_hold.png
    icon_love/passion/understanding/stress.png
    computer_desk sofa pendant_lamp toilet sink shower shelf chip_bag ...
    characters/
      hero_idle hero_computer hero_sad hero_tired hero_angry hero_love hero_shy hero_horny
      hero_sofa hero_bed hero_bunny hero_penguin hero_toilet hero_sink hero_shower
      hero_fat (Bad End 弃用图)
      heroine_idle heroine_idle_glasses
```

---

## 关键代码位置

**state 定义**：`DEFAULT_STATE`（存 stats/scene/lightsOn/atComputer/chipCount/outCount/walkDone/argueDone/kissDone/badEnd/heroName/gameTime）

**核心函数**：
- `changeStat(key, delta)` — 加减数值 + 浮动动画
- `renderStats()` — 更新进度条宽度
- `advanceTime(hours=3)` — 推进游戏时间，跨夜触发睡觉
- `switchScene(name)` — 场景切换（不消耗时间）
- `showDialog(speaker, text)` — 底部对话气泡（speaker 用 `'@bf'` 自动替换为男主名）
- `showMenu(anchorEl, items)` — 气泡菜单
- `cgShow / cgSay / cgChoose` — CG 播放系统
- `triggerWalkStory / triggerArgueStory / triggerKissStory / triggerBadEnd` — 剧情

**交互定义**：`INTERACTIONS` 对象，每个 `data-action` 对应一个函数（`hero/computer/sofa/bed/bunny/penguin/lamp/goOut/toilet/sink/shower/chip`）

**事件绑定**：`document.addEventListener('click')` 统一分发到 nav 或 action；`NO_TIME_ACTIONS` 白名单排除不消耗时间的动作

---

## 素材生成脚本模板

所有 AI 图生成都用 OpenRouter 的 `google/gemini-3.1-flash-lite-image`。模板：

```bash
python3 <<'PY'
import os, json, base64, urllib.request
prompt = "..."
refs = ["/path/to/ref.png"]  # 可选，用于角色一致性
content = [{"type":"text","text":prompt}]
for r in refs:
    b64 = base64.b64encode(open(r,"rb").read()).decode()
    content.append({"type":"image_url","image_url":{"url":f"data:image/png;base64,{b64}"}})
req = urllib.request.Request(
    "https://openrouter.ai/api/v1/chat/completions", method="POST",
    headers={"Authorization": f"Bearer {os.environ['OPENROUTER_API_KEY']}", "Content-Type":"application/json"},
    data=json.dumps({"model":"google/gemini-3.1-flash-lite-image",
        "messages":[{"role":"user","content":content}],
        "modalities":["image","text"]}).encode())
with urllib.request.urlopen(req, timeout=180) as r:
    d = json.loads(r.read())
    url = d["choices"][0]["message"]["images"][0]["image_url"]["url"]
    open("out.png","wb").write(base64.b64decode(url.split(",",1)[1]))
PY
```

**去白底**：Pillow 遍历像素，`r>245 and g>245 and b>245` 设为 (255,255,255,0)。**注意**：脚本调色容易误伤脸部/衣服，改颜色优先重新调 API 生成，别写脚本调色。

---

## 已定型的美术风格约定

- **场景背景**：细腻像素风（Stardew Valley 精度），flat front view，中央大片空地留给可交互物件
- **物件 sprite**：同风格像素风，透明底，投影在底部
- **主线 CG**：Love Choice 蜡笔/彩铅涂鸦风，Q版比例，白脸红腮红，简单五官但**女生要画得漂亮**（AI 容易把女生画丑，prompt 里要明确"大眼睛、瓜子脸、精致五官"）
- **色调统一**：白墙、浅木地板、蓝灰沙发、深蓝夜空 + 萤火虫，参考用户家 loft 户型

---

## 已确认的用户偏好 💡

- **不要**再用脚本调色改角色（脸会崩），必须改颜色就重新 API 生
- 女生**不戴**眼镜（除了 `heroine_idle_glasses` 变体）
- 女生 tank top 用**樱桃红**（不是酒红、不是亮红、不是紫红）
- 男主蓝连帽衣 + 黑裤 + 眼镜，锁死
- BAD END 用**纯文字**，不放图
- 男主 scale 涨到**贴屏幕高但不出屏**就够
- 剧情基调：现实矛盾 + 共同成长 + 多结局 + 日历式推进

---

## 下次开机做什么

1. `git pull` 拿最新代码
2. 读这个 HANDOFF.md 看进度
3. 挑一个待办开工
4. 做完更新这个文件 + push

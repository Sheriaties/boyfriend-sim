# HANDOFF — 项目交接文档

> 用于在多台电脑之间同步开发进度。**每次做完一件事都更新这个文件**，别的机器 pull 下来就知道现状。

**最后更新**: 2026-07-29（大更 v3 · 新增框架 v1 + D3 商场事件）
**仓库**: https://github.com/Sheriaties/boyfriend-sim

---

## 项目一句话

给女朋友玩的**横版点按恋爱养成小游戏**。同居情侣视角，Q版/像素/蜡笔混搭画风，AI 生成素材。目标游玩时长约 1 小时，多结局。

---

## ⭐ 顶层设计 · 框架 v1（2026-07-29 与用户对齐并锁定）

> 完整设计文档见 `.claude-internal/projects/-Users-jinlong-Desktop-recreation-game/memory/project_framework_v1.md`（用户本地 memory，不进 repo）。以下是简要概述。

### 定位
**类型融合**：我的汤姆猫（陪伴型宠物）× 拣爱（简笔画叙事恋爱）× 现有沙盒点按
**基调**：表面温馨治愈，底下藏情欲暗流 —— 越玩越发现"他一直在憋"
**唯一玩家**：用户女朋友，不做审核向

### 内容分三层

**Layer 1 · 陪伴日常台词库**（汤姆猫式，尚未实现）
- 男主大量随机台词散布在所有热区
- 分类：撒娇/发呆/逗你/关心/想她/情欲暗流/迁就（彩蛋伏笔）/记住她的偏好
- 每类 20 条起步，总计数百条
- 是"陪伴感"的核心

**Layer 2 · 觉察式彩蛋**（3-4 个，功能性顿悟）
玩家发现具体物件/动作 → 意识到"他一直在为我做 XX"。
- ✅ **1. 现有** — 2048 卷角 → 游戏机 → 一起玩她喜欢的游戏
- 🚧 **2. 计划** — 薯片旁边的书 = 日记本，男主睡着时才能打开（Task #9）
- ❓ **3. 待补**
- ❓ **4. 待补**

**Layer 3 · 大事件 PV**（4-5 天一个，全周期 6-7 个）
每 4-5 天一个大事件，采用"小游戏 + 察觉线索 + 黑屏对白 + 高画质 PV + 世界状态永久改变"的模式。

**PV 画风参考**：`assets/cg_fireworks_pov_turn.png`（细腻现代 anime 风、柔光、脸颊淡红晕）

### 情欲线（暗流，独立于剧情）

**触发**：无数值门槛，玩家随时可玩，走到夜晚场景点对应位置即可。

**3 场景 × 每场景 3 阶段**（阶段随重复次数解锁）：
| 场景 | 阶段 1 | 阶段 2 | 阶段 3 |
|---|---|---|---|
| 床（夜晚床菜单新增项） | 生疏紧张 | 熟练 | 她主动 |
| 淋浴（复用"要一起洗吗"） | 洗澡+暗示 | 不老实 | 直接开搞 |
| 沙发（白天/傍晚也可触发） | 蹭抱 | 隔着衣服 | 顺势倒下 |

**尺度递进（用户明确"越往后可以变态一点"）**：
- 阶段 1：委婉暗示 / 常规情境 / 平等或他略主导 / 轻微羞耻
- 阶段 2：直白 / 加小情境（打断、白天、刚洗完澡）/ 随机权力切换 / 中等羞耻
- 阶段 3：可放开 / 加小玩法（捆、堵嘴、镜子等）/ 随机权力（他强势 / 她支配 / 角色扮演）/ 强背德感

**统一规则**：
- 全程黑屏 + 文字对白，无视觉呈现
- 两人自愿，不做胁迫
- 权力关系随机切换

### 激情=100 三重坏结局改造（尚未实现，Task #11）

**原逻辑**：激情=100 直接跳 puppy/yandere/exhausted
**新逻辑**：激情=100 → 男主提出"想再来一次" → 玩家选**继续 / 拒绝**
- 拒绝 → 数值稍降，回归日常
- 继续 → 黑屏文字重复演出 → 按压力值分三个坏结局

**Why**：坏结局从"数值被动触发"变成"玩家主动选择进入"，情感冲击更大。

### 「细节察觉」系统 + 察觉笔记 HUD（用户设计）

**机制**：每个大事件带 **1 个小线索** → 指向该事件的好结局。
- 察觉到 = 该事件走好结局路径
- 没察觉 = 该事件走坏结局选项路径
- 累计察觉数 → 推高了解度，影响 W3 D18 危机与最终结局

**察觉笔记 HUD**：右下角小别针 icon，察觉一个线索 +1 条，未发现的显示 "？？？"

**触发模式**：
- 达成条件 → **直接进好结局演出**（没有选项菜单）
- 没达成 → 出现选项菜单让玩家在几个坏结局里选（"坏结局都是玩家主动选的"）

**线索内容由用户自己设计**，代码留好 `state.clues[clueId]` 接口即可。

---

## Layer 3 大事件时间轴（初拟，可打磨）

| 日 | 事件 | 状态 | 察觉线索 |
|---|---|---|---|
| **D3** | 🛍 商场逛街 · 玩偶店 vs 猪排店 | ✅ **已实现** | `mall_plushie`（用鼠标抗惯性停在玩偶摊） |
| D7 | 夜色散步（复用现有 cg_walk） | 🚧 待重新设计（现在是"外出3次"触发，改成 D7 自动） | ? |
| D11 | 争吵（复用现有 cg_argue） | 🚧 有 `triggerArgueStory` 但没接钩子 | ? |
| D14 | 便利贴 + 和好接吻 | 🚧 接吻 CG 仍是占位 | ? |
| D18 | 危机三选一（宿舍纠结 × 风言风语） | ❌ **核心大戏，未实现** | 累计所有线索 |
| D22 | W3 后果 | ❌ 未实现 | ? |
| D28 | 摊牌 + 结局（TrueEnd = 他写的信） | ❌ 未实现 | — |

**下一个电脑要接手 Layer 3 的话**，参考 D3 的实现模式（见 `index.html` 中 `triggerD3MallEvent` 起、`checkStoryBeats` 函数），依样画瓢做后 6 个即可。

---

## ✅ D3 商场事件（2026-07-29 完成）

**代码位置**：`index.html` 中 `triggerD3MallEvent`、`playMallMinigame`、`d3MallSuccessOutcome`、`d3MallFailPrompt`

**流程**：
1. D3 白天首次 `advanceTime` 自动触发（`checkStoryBeats` 检查）
2. 黑屏对白：男主邀请 + 两句"逛得很开心"旁白
3. 轻松商场 BGM 开始循环；小游戏中两人模型自动从右向左平移，玩家的判定圈被强制左飘，玩家要抗力拖住停在玩偶摊上
4. 关键判定：两人模型走到玩偶摊 x 位置时，判定圈是否仍在玩偶摊热区内
5. **✅ 成功**：黑屏对白 → PV（`cg_mall_pv.png`，兜底 `cg_walk_hold.png`） → 女主心声 → love+10 understanding+10 → `plushiesOwned=true` + `clues.mall_plushie=discovered` → 卧室出现玩偶
6. **❌ 失败**：走到猪排店 → 男主"还要再逛逛吗？" → 选"回家"永久失败（`d3PermanentFail=true`，卧室永远空床） / 选"再逛"完全重播

**新增 state 字段**：
- `plushiesOwned`（初始 false，D3 好结局后 true，卧室背景 + 玩偶热区都依赖此字段）
- `d3Done`（无论成功失败，事件走完 = true，不再自动触发）
- `d3PermanentFail`（选"回家"= true，永远没玩偶）
- `clues`（察觉线索表，`{ clueId: {discovered, unlockedAt} }`）

**存档兼容**：老存档 `plushiesOwned` 缺失 → 自动补 true + d3Done=true（不影响老玩家）

**卧室背景条件化**：
- 白天 + 有玩偶：`bg_bedroom.png`
- 白天 + 无玩偶：`bg_bedroom_empty.png`（fallback: `bg_bedroom.png`，素材还没生成时不会白屏）
- 夜晚（男主睡着）：`bg_bedroom_night.png`（男主睡着时玩偶本来就被隐藏，不需要空版）

**开发者面板**：`⚙ → 🛍 D3 商场事件` 直接触发，`🐰 切换 plushiesOwned` 切玩偶显隐

---

## 🎨 D3 素材（待生成）

用 `scripts/gen_d3_mall_assets.py` 生成。使用 OpenRouter + Gemini（同现有素材方案）。

```bash
export OPENROUTER_API_KEY=sk-or-...
python3 scripts/gen_d3_mall_assets.py all
# 或单个：
python3 scripts/gen_d3_mall_assets.py cg_mall_pv
```

需要的素材：
| 文件 | 用途 |
|---|---|
| `assets/bg_mall.png` | 商场横向长条背景（占位：纯色渐变） |
| `assets/sprite_plushie_stand.png` | 玩偶摊 sprite（占位：CSS 生成的粉色矩形+🐰🐧文字） |
| `assets/sprite_katsu_shop.png` | 炸猪排店 sprite（占位：CSS 生成的木色矩形+🍱文字） |
| `assets/cg_mall_pv.png` | 成功 PV（占位：`cg_walk_hold.png` 兜底） |
| `assets/bg_bedroom_empty.png` | 卧室白天空床版（占位：`bg_bedroom.png` 兜底，但卧室会一直有玩偶） |
| `assets/d3_mall_bgm.mp3` | D3 商场轻松循环 BGM（Happy Clappy Loop，CC0） |

**注意**：素材生成完之前，D3 事件也能完整跑通，只是视觉是占位的。

---

## 已完成 ✅（历史）

### 场景 & 素材
- **场景**：客厅（起点）⇄ 卧室（loft 夹层，上楼）⇄ 厕所（右下）
- **背景图**：`bg_living.png`、`bg_bedroom.png`（有玩偶）、`bg_bedroom_night.png`、`bg_bathroom.png`
- **男主立绘**：hero_idle / hero_gaming / hero_watching / hero_working / hero_sad/tired/angry/love/shy/horny / hero_sofa/bed/bunny/penguin/toilet/sink/shower / hero_fat
- **女主立绘**：heroine_idle / heroine_idle_glasses
- **物件 sprite**：computer_desk / sofa / pendant_lamp / toilet / sink / shower / shelf / chip_bag / window_day / window_night
- **数值图标**：icon_love / icon_passion / icon_understanding / icon_stress
- **主线 CG**：cg_walk / cg_walk_hold / cg_argue / cg_night_city / cg_hug_window / cg_fireworks / cg_fireworks_pov_turn / cg_kiss_fw / cg_birdsong / cg_coop_game

### 系统
- HUD、封面、回封面、通用确认弹窗、开场取名（heroName）
- 时间系统：每次交互 +3 小时；22:00 自动入睡；07:00 之后可"叫醒他"
- 昼夜系统：6-18 白天 / 18-22 傍晚 / 22-06 深夜
- 卧室背景条件化：`plushiesOwned` + `heroAsleep`
- 存档：localStorage `bf-sim-save-v1`，含老存档 lightsOn/plushiesOwned 兼容层
- CG 播放系统（`cgShow` / `cgSay` / `cgChoose`）
- 现有大事件：散步（外出满3次）/ 争吵（`triggerArgueStory` 未接钩）/ 接吻（占位）/ 夜晚窗边独白 + 烟花
- **D3 商场事件（本次新增）**
- 2048 迷你游戏 + 游戏机彩蛋（Layer 2 觉察彩蛋 #1）
- 小鸟接唱音游（旋律填空 Simon Says）
- 薯片 Bad End（连喂10次）
- 出去住 Bad End（累计 4 次）
- 13 个结局（6 立即死亡 / 5 结算 / 2 隐藏）
- 开发者面板（`~` / ⚙）

---

## 📋 待办（Task 列表见 Claude Code `TaskList`）

### 高优 · Layer 3 大事件（依样画瓢 D3 实现模式）
- [ ] D7 · 夜色散步（改成日期钩子触发，加察觉线索）
- [ ] D11 · 争吵（接钩子，触发条件仍可用"了解度<30 或 压力>60"）
- [ ] D14 · 便利贴 + 和好接吻正式版 CG
- [ ] **D18 · 危机三选一**（核心大戏，宿舍纠结+风言风语）
- [ ] D22 · W3 后果
- [ ] D28 · 摊牌 + TrueEnd（他写给她的信，逐句展开）

### 高优 · 系统
- [ ] 察觉笔记 HUD（右下角小别针）+ `state.clues` 面板可视化
- [ ] Layer 1 · 男主陪伴日常台词库（分类×分场景×数百条，依赖用户提供口头禅素材）
- [ ] 情欲线：床/淋浴/沙发 × 3阶段矩阵 + 黑屏对白系统
- [ ] 激情=100 坏结局改造（从数值触发改玩家选择）

### 中优 · 素材
- [ ] 跑 `scripts/gen_d3_mall_assets.py all` 生成 D3 5 张素材
- [ ] 接吻 CG 正式版（当前占位用 cg_argue）
- [ ] 察觉彩蛋 #3 #4 的方向（用户来定）
- [ ] 日记本彩蛋（薯片旁书，夜晚可打开，Layer 2 #2）

### 低优
- [ ] 音效 / BGM（部分已加，未全）
- [ ] 手机竖屏适配
- [ ] 上线前删所有 `dev-toggle` / `dev-panel` / `dev_*`

---

## 📁 关键代码位置速查

**state 定义**：`DEFAULT_STATE` @ index.html 顶层 script 开头
- `plushiesOwned` / `d3Done` / `d3PermanentFail` / `clues` — 本次新增

**核心函数**：
- `changeStat(key, delta)` — 加减数值 + 浮动动画
- `advanceTime(hours=3)` — 推进时间；末尾调 `checkStoryBeats`（**本次新增**）
- `switchScene(name)` — 场景切换
- `applyDayNight()` — 昼夜/卧室背景/立绘（本次改造：加了 plushiesOwned 分支）
- `showDialog(speaker, text)` — 场景内气泡对白
- `cgShow / cgSay / cgChoose` — CG 播放系统
- `triggerWalkStory / triggerArgueStory / triggerKissStory` — 现有剧情
- **`triggerD3MallEvent`** — D3 主入口
- **`playMallMinigame`** — 商场小游戏循环
- **`checkStoryBeats`** — 大事件调度器（未来 D7/D11/D14/D18 都往里加）
- **`isInCG`** — 检查是否有 CG/mall overlay 在显示

**交互定义**：`INTERACTIONS` 对象

**事件绑定**：`document.addEventListener('click')`；`NO_TIME_ACTIONS` 白名单

**HTML overlay**：
- `#cg-overlay` — 通用 CG 播放器（含 timer 圈）
- `#mall-overlay` — **D3 商场小游戏（本次新增）**
- `#dev-panel` — 开发者面板
- `#birdsong-overlay` — 小鸟音游
- `#mini-2048` — 2048 迷你游戏

---

## 素材生成脚本模板

见 `scripts/gen_d3_mall_assets.py`（本次新增，D3 专用）。通用模板还是 HANDOFF 老版本里那段 python。

**去白底**：Pillow 遍历像素 `r>245 and g>245 and b>245` 设为 (255,255,255,0)。**注意**：脚本调色容易误伤脸部，改颜色必须重新调 API 生。

---

## 已定型的美术风格约定

- **场景背景**：细腻像素风（Stardew Valley 精度），flat front view
- **物件 sprite**：同风格像素风，透明底
- **主线 CG · 大事件 PV**：**参考 `cg_fireworks_pov_turn.png` 的现代 anime 温柔风**（柔光/淡红晕/细腻线条）
- **主线 CG · 涂鸦风**：Love Choice 蜡笔风 Q版（现有 cg_walk / cg_argue 用这个，新的高浓度事件请优先用 anime 风）
- **色调**：白墙、浅木地板、蓝灰沙发、深蓝夜空

---

## 已确认的用户偏好 💡

- **不要**再用脚本调色改角色
- 女生不戴眼镜（除了 heroine_idle_glasses 变体）
- 女生 tank top 用**樱桃红**
- 男主：蓝连帽衣 + 黑裤 + 眼镜
- BAD END 用纯文字 or 图 + 半透明黑叠加
- **玩偶真名**：🐰 卢米·紫水晶 / 🐧 大奥利
- 剧情基调：**真实矛盾改编**、避免通用乙女套路、埋个人化细节

---

## 下次开机做什么

1. `git pull` 拿最新代码
2. 读这个 HANDOFF.md 看进度
3. **重点看** ⭐ 顶层设计 · 框架 v1 那一节
4. **重点看** ✅ D3 商场事件那一节（后续大事件依样画瓢）
5. 挑一个待办开工（推荐从"察觉笔记 HUD"或"D7 改造"入手）
6. 做完更新这个文件 + push

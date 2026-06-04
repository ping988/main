# Reference Product Ad Replication

参考产品广告复刻 Skill，用于拆解参考广告的视觉风格、镜头语言、叙事节奏、转场逻辑、音乐结构与真实动作音效，并将多个 AI 生成片段剪辑成一支连贯、完整的产品广告。

它不追求简单模仿单个画面，而是复刻参考片的广告导演逻辑，同时尽可能保持目标产品包装、品牌识别和使用方式不变。

## 适用场景

- 根据一支参考广告，为新产品制作同类风格广告
- 拆解参考视频的镜头、运镜、节奏和转场
- 规划并分批生成产品广告片段
- 修复成片中的硬拼接、重复产品展示和叙事断裂
- 为整支广告统一配乐，并添加与动作同步的真实音效
- 审查产品一致性、镜头顺序、音乐连续性和音效真实性

## 核心原则

1. **产品真实优先**：包装、Logo、颜色、结构和使用方式不能随意变化。
2. **先拆解再生成**：复刻镜头语言和叙事逻辑，而不只是模仿色调。
3. **先测试再批量制作**：先生成并审核一个测试片段，确认方向后再继续。
4. **按动作链剪辑**：每个镜头都要承接上一个动作，并为下一个镜头创造入口。
5. **使用一条连续发展的音乐**：不能让每个片段重新播放同一段音乐。
6. **音效必须有真实画面来源**：持续动作需要持续音效，不添加无来源的装饰音。
7. **交付前完整自查**：确认顺序、产品、转场、音乐、音效和技术规格均正确。

## 快速调用

在 Codex 中使用：

```text
Use $reference-product-ad-replication to replicate this reference product advertisement.
Preserve the supplied product exactly, generate one test clip first, and review it before continuing.
```

中文示例：

```text
使用 $reference-product-ad-replication，参考我提供的广告视频，为这个产品制作同风格广告。
保持产品包装完全不变，先拆解参考片并生成一个测试片段，我确认后再继续。
```

## 标准工作流

```text
确认产品真实信息
→ 拆解参考广告
→ 编写因果动作链
→ 生成并审核测试片段
→ 分批生成其余镜头
→ 按叙事和动作连续性剪辑
→ 统一整片音乐
→ 添加真实同步音效
→ 导出分轨并完成最终审查
```

## 推荐交付物

- 最终广告视频
- 音乐单独音轨
- 音效单独音轨
- 音效同步审查视频
- 镜头顺序与动作时间点说明
- 产品一致性、音频和技术规格检查结果

## 文件结构

```text
reference-product-ad-replication/
├── SKILL.md
├── README.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── audio-and-qa.md
│   └── replication-playbook.md
└── scripts/
    └── make_timeline_contact_sheet.py
```

## 时间线联系表工具

`scripts/make_timeline_contact_sheet.py` 可以按固定时间间隔提取视频帧，用于分析镜头、动作和转场。

依赖：

```text
opencv-python
Pillow
```

示例：

```bash
python scripts/make_timeline_contact_sheet.py reference.mp4 timeline.jpg --step 0.5 --cols 8
```

## 详细指南

- [Skill 执行规则](SKILL.md)
- [参考广告复刻方法](references/replication-playbook.md)
- [音乐、音效与最终审查](references/audio-and-qa.md)

## 使用限制

- AI 视频模型可能改变包装文字、Logo、人物手部或产品结构，需要逐镜审核。
- 如果现有生成方式无法保持目标产品真实，应暂停生成并更换方案。
- 生成片段通常不能直接完整使用，需要剪掉重复开场、空镜和多余产品定格。
- 音效必须根据最终剪辑逐帧同步，不能只依赖模型自动生成的音频。

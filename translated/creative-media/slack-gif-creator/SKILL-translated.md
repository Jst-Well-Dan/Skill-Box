<!--
本文件由智谱 AI 自动翻译生成
原文件: SKILL.md
翻译时间: 2025-12-12 16:12:27
翻译模型: glm-4-flash
原文大小: 17,056 字符
-->

---
name: slack-gif-creator
description: 用于创建针对 Slack 优化的动画 GIF 的工具包，包括对大小约束和可组合动画原语的有效性验证。当用户请求 Slack 的动画 GIF 或表情动画时，此技能适用，例如“为我制作一个 Slack 的 X 做 Y 的 GIF”。
license: 详细条款请参阅 LICENSE.txt
---

# Slack GIF Creator - 灵活的工具包

用于创建针对 Slack 优化的动画 GIF 的工具包。提供 Slack 约束的有效性验证器、可组合的动画原语和可选的辅助工具。**根据需要应用这些工具以实现创意愿景**。

## Slack 的要求

Slack 对 GIF 有特定的要求，基于其用途：

**消息 GIF：**
- 最大尺寸：约 2MB
- 最佳尺寸：480x480
- 典型 FPS：15-20
- 颜色限制：128-256
- 持续时间：2-5 秒

**表情 GIF：**
- 最大尺寸：64KB（严格限制）
- 最佳尺寸：128x128
- 典型 FPS：10-12
- 颜色限制：32-48
- 持续时间：1-2 秒

**表情 GIF 非常具有挑战性** - 64KB 的限制非常严格。以下策略可以帮助：
- 总帧数限制在 10-15 帧
- 最大颜色数限制在 32-48 种
- 保持设计简单
- 避免渐变
- 频繁验证文件大小

## 工具包结构

此技能提供三种类型的工具：

1. **验证器** - 检查 GIF 是否满足 Slack 的要求
2. **动画原语** - 可组合的运动构建块（摇晃、弹跳、移动、万花筒）
3. **辅助工具** - 用于常见需求的可选函数（文本、颜色、效果）

**在应用这些工具方面，完全的自由创作**。

## 核心验证器

为确保 GIF 满足 Slack 的约束，请使用以下验证器：

```python
from core.gif_builder import GIFBuilder

# 创建 GIF 后，检查其是否满足要求
builder = GIFBuilder(width=128, height=128, fps=10)
# ... 以您想要的方式添加帧 ...

# 保存并检查大小
info = builder.save('emoji.gif', num_colors=48, optimize_for_emoji=True)

# 保存方法会自动警告文件是否超出限制
# info 字典包含：size_kb, size_mb, frame_count, duration_seconds
```

**文件大小验证器**：
```python
from core.validators import check_slack_size

# 检查 GIF 是否满足大小限制
passes, info = check_slack_size('emoji.gif', is_emoji=True)
# 返回：True/False，包含大小详细信息的字典
```

**尺寸验证器**：
```python
from core.validators import validate_dimensions

# 检查尺寸
passes, info = validate_dimensions(128, 128, is_emoji=True)
# 返回：True/False，包含尺寸详细信息的字典
```

**完整验证**：
```python
from core.validators import validate_gif, is_slack_ready

# 运行所有验证
all_pass, results = validate_gif('emoji.gif', is_emoji=True)

# 或快速检查
if is_slack_ready('emoji.gif', is_emoji=True):
    print("准备上传！")
```

## 动画原语

这些是可组合的运动构建块。将这些应用于任何对象，以任何组合方式：

### 摇晃
```python
from templates.shake import create_shake_animation

# 摇晃一个表情
frames = create_shake_animation(
    object_type='emoji',
    object_data={'emoji': '😱', 'size': 80},
    num_frames=20,
    shake_intensity=15,
    direction='both'  # 或 'horizontal', 'vertical'
)
```

### 弹跳
```python
from templates.bounce import create_bounce_animation

# 弹跳一个圆形
frames = create_bounce_animation(
    object_type='circle',
    object_data={'radius': 40, 'color': (255, 100, 100)},
    num_frames=30,
    bounce_height=150
)
```

### 旋转 / 旋转
```python
from templates.spin import create_spin_animation, create_loading_spinner

# 顺时针旋转
frames = create_spin_animation(
    object_type='emoji',
    object_data={'emoji': '🔄', 'size': 100},
    rotation_type='clockwise',
    full_rotations=2
)

# 摇摆旋转
frames = create_spin_animation(rotation_type='wobble', full_rotations=3)

# 加载指示器
frames = create_loading_spinner(spinner_type='dots')
```

### 脉冲 / 心跳
```python
from templates.pulse import create_pulse_animation, create_attention_pulse

# 平滑脉冲
frames = create_pulse_animation(
    object_data={'emoji': '❤️', 'size': 100},
    pulse_type='smooth',
    scale_range=(0.8, 1.2)
)

# 心跳（双泵）
frames = create_pulse_animation(pulse_type='heartbeat')

# 注意力脉冲（用于表情 GIF）
frames = create_attention_pulse(emoji='⚠️', num_frames=20)
```

### 淡入
```python
from templates.fade import create_fade_animation, create_crossfade

# 淡入
frames = create_fade_animation(fade_type='in')

# 淡出
frames = create_fade_animation(fade_type='out')

# 两个表情之间的交叉淡入
frames = create_crossfade(
    object1_data={'emoji': '😊', 'size': 100},
    object2_data={'emoji': '😂', 'size': 100}
)
```

### 缩放
```python
from templates.zoom import create_zoom_animation, create_explosion_zoom

# 非常大的缩放
frames = create_zoom_animation(
    zoom_type='in',
    scale_range=(0.1, 2.0),
    add_motion_blur=True
)

# 缩放出
frames = create_zoom_animation(zoom_type='out')

# 爆炸缩放
frames = create_explosion_zoom(emoji='💥')
```

### 爆炸 / 粉碎
```python
from templates.explode import create_explode_animation, create_particle_burst

# 爆炸碎片
frames = create_explode_animation(
    explode_type='burst',
    num_pieces=25
)

# 粉碎效果
frames = create_explode_animation(explode_type='shatter')

# 溶解成粒子
frames = create_explode_animation(explode_type='dissolve')

# 粒子爆炸
frames = create_particle_burst(particle_count=30)
```

### 摇摆 / 振动
```python
from templates.wiggle import create_wiggle_animation, create_excited_wiggle

# 橡皮糖摇摆
frames = create_wiggle_animation(
    wiggle_type='jello',
    intensity=1.0,
    cycles=2
)

# 波动运动
frames = create_wiggle_animation(wiggle_type='wave')

# 激动的摇摆（用于表情 GIF）
frames = create_excited_wiggle(emoji='🎉')
```

### 滑动
```python
from templates.slide import create_slide_animation, create_multi_slide

# 从左侧滑入并超出
frames = create_slide_animation(
    direction='left',
    slide_type='in',
    overshoot=True
)

# 横向滑动
frames = create_slide_animation(direction='left', slide_type='across')

# 多个对象按顺序滑动
objects = [
    {'data': {'emoji': '🎯', 'size': 60}, 'direction': 'left', 'final_pos': (120, 240)},
    {'data': {'emoji': '🎪', 'size': 60}, 'direction': 'right', 'final_pos': (240, 240)}
]
frames = create_multi_slide(objects, stagger_delay=5)
```

### 翻转
```python
from templates.flip import create_flip_animation, create_quick_flip

# 两个表情之间的水平翻转
frames = create_flip_animation(
    object1_data={'emoji': '😊', 'size': 120},
    object2_data={'emoji': '😂', 'size': 120},
    flip_axis='horizontal'
)

# 垂直翻转
frames = create_flip_animation(flip_axis='vertical')

# 快速翻转（用于表情 GIF）
frames = create_quick_flip('👍', '👎')
```

### 变形 / 变换
```python
from templates.morph import create_morph_animation, create_reaction_morph

# 交叉淡入变形
frames = create_morph_animation(
    object1_data={'emoji': '😊', 'size': 100},
    object2_data={'emoji': '😂', 'size': 100},
    morph_type='crossfade'
)

# 缩放变形（一个缩小而另一个增长）
frames = create_morph_animation(morph_type='scale')

# 旋转变形（类似 3D 翻转）
frames = create_morph_animation(morph_type='spin_morph')
```

### 移动效果
```python
from templates.move import create_move_animation

# 线性运动
frames = create_move_animation(
    object_type='emoji',
    object_data={'emoji': '🚀', 'size': 60},
    start_pos=(50, 240),
    end_pos=(430, 240),
    motion_type='linear',
    easing='ease_out'
)

# 弧形运动（抛物线轨迹）
frames = create_move_animation(
    object_type='emoji',
    object_data={'emoji': '⚽', 'size': 60},
    start_pos=(50, 350),
    end_pos=(430, 350),
    motion_type='arc',
    motion_params={'arc_height': 150}
)

# 圆形运动
frames = create_move_animation(
    object_type='emoji',
    object_data={'emoji': '🌍', 'size': 50},
    motion_type='circle',
    motion_params={
        'center': (240, 240),
        'radius': 120,
        'angle_range': 360  # 全圆
    }
)

# 波动运动
frames = create_move_animation(
    motion_type='wave',
    motion_params={
        'wave_amplitude': 50,
        'wave_frequency': 2
    }
)

# 或使用低级缓动函数
from core.easing import interpolate, calculate_arc_motion

for i in range(num_frames):
    t = i / (num_frames - 1)
    x = interpolate(start_x, end_x, t, easing='ease_out')
    # 或：x, y = calculate_arc_motion(start, end, height, t)
```

### 万花筒效果
```python
from templates.kaleidoscope import apply_kaleidoscope, create_kaleidoscope_animation

# 应用到单个帧
kaleido_frame = apply_kaleidoscope(frame, segments=8)

# 或创建动画万花筒
frames = create_kaleidoscope_animation(
    base_frame=my_frame,  # 或 None 用于演示模式
    num_frames=30,
    segments=8,
    rotation_speed=1.0
)

# 简单镜像效果（更快）
from templates.kaleidoscope import apply_simple_mirror

mirrored = apply_simple_mirror(frame, mode='quad')  # 4 方镜像
# modes: 'horizontal', 'vertical', 'quad', 'radial'
```

**要自由组合原语，请遵循以下模式：**
```python
# 示例：弹跳 + 摇晃以产生冲击
for i in range(num_frames):
    frame = create_blank_frame(480, 480, bg_color)

    # 弹跳运动
    t_bounce = i / (num_frames - 1)
    y = interpolate(start_y, ground_y, t_bounce, 'bounce_out')

    # 在 y 达到地面时添加摇晃（当 y 达到地面）
    if y >= ground_y - 5:
        shake_x = math.sin(i * 2) * 10
        x = center_x + shake_x
    else:
        x = center_x

    draw_emoji(frame, '⚽', (x, y), size=60)
    builder.add_frame(frame)
```

## 辅助工具

这些是用于常见需求的可选辅助工具。**根据需要使用、修改或替换这些工具以自定义实现**。

### GIF 构建器（组装与优化）

```python
from core.gif_builder import GIFBuilder

# 使用您选择的设置创建构建器
builder = GIFBuilder(width=480, height=480, fps=20)

# 添加帧（以您创建的方式）
for frame in my_frames:
    builder.add_frame(frame)

# 保存并优化
builder.save('output.gif',
             num_colors=128,
             optimize_for_emoji=False)
```

主要功能：
- 自动颜色量化
- 重复帧删除
- Slack 限制的大小警告
- 表情模式（激进优化）

### 文本渲染

对于像表情这样的小 GIF，文本可读性具有挑战性。常见的解决方案是在文本周围添加轮廓：

```python
from core.typography import draw_text_with_outline, TYPOGRAPHY_SCALE

# 带轮廓的文本（有助于可读性）
draw_text_with_outline(
    frame, "BONK!",
    position=(240, 100),
    font_size=TYPOGRAPHY_SCALE['h1'],  # 60px
    text_color=(255, 68, 68),
    outline_color=(0, 0, 0),
    outline_width=4,
    centered=True
)
```

要实现自定义文本渲染，请使用 PIL 的 `ImageDraw.text()`，它对较大的 GIF 工作良好。

### 颜色管理

看起来专业的 GIF 常常使用协调的色彩调色板：

```python
from core.color_palettes import get_palette

# 获取预制的调色板
palette = get_palette('vibrant')  # 或 'pastel', 'dark', 'neon', 'professional'

bg_color = palette['background']
text_color = palette['primary']
accent_color = palette['accent']
```

要直接处理颜色，请使用 RGB 元组 - 适用于任何用例。

### 视觉效果

可选效果用于冲击时刻：

```python
from core.visual_effects import ParticleSystem, create_impact_flash, create_shockwave_rings

# 粒子系统
particles = ParticleSystem()
particles.emit_sparkles(x=240, y=200, count=15)
particles.emit_confetti(x=240, y=200, count=20)

# 更新并渲染每一帧
particles.update()
particles.render(frame)

# 闪光效果
frame = create_impact_flash(frame, position=(240, 200), radius=100)

# 冲浪环
frame = create_shockwave_rings(frame, position=(240, 200), radii=[30, 60, 90])
```

### 缓动函数

使用缓动代替线性插值以实现平滑的运动：

```python
from core.easing import interpolate

# 物体下落（加速）
y = interpolate(start=0, end=400, t=progress, easing='ease_in')

# 物体着陆（减速）
y = interpolate(start=0, end=400, t=progress, easing='ease_out')

# 弹跳
y = interpolate(start=0, end=400, t=progress, easing='bounce_out')

# 超出（弹性）
scale = interpolate(start=0.5, end=1.0, t=progress, easing='elastic_out')
```

可用的缓动：`linear`、`ease_in`、`ease_out`、`ease_in_out`、`bounce_out`、`elastic_out`、`back_out`（超出）以及更多在 `core/easing.py` 中。

### 帧组合

基本的绘图工具，如果您需要它们：

```python
from core.frame_composer import (
    create_gradient_background,  # 渐变背景
    draw_emoji_enhanced,         # 带可选阴影的表情
    draw_circle_with_shadow,     # 带阴影的形状
    draw_star                    # 5 点星
)

# 渐变背景
frame = create_gradient_background(480,
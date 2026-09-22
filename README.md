<h1 align="center">Coding Workflow · AI 编程工作流</h1>

<p align="center"><strong>把编程需求整理成明确目标，再完成范围可控的修改、验证和审查。</strong></p>

<p align="center">
  <img src="https://img.shields.io/badge/type-Agent%20Skill-2563EB" alt="Agent Skill">
  <img src="https://img.shields.io/badge/scripts-Python-3776AB" alt="Python scripts">
  <img src="https://img.shields.io/badge/license-MIT-2EA043" alt="MIT license">
</p>

这是一个供 Codex 使用的轻量编程 Skill。安装后，你可以用自然语言描述要修复的问题或新增的功能，让 Agent 先说明验收标准，再修改代码、检查结果，并在条件允许时安排独立审查。

适合个人项目、日常修复和小型脚本。工作量会随风险调整，改一个错别字通常只需要简短说明和检查；涉及认证、金额、数据迁移等改动时，需要更完整的验证。

## 📊 工作流程

```mermaid
flowchart LR
    A[描述编程需求] --> B[确认目标与验收标准]
    B --> C[按风险选择工作模式]
    C --> D[完成范围内的修改]
    D --> E[运行测试或其他检查]
    E --> F[按需独立审查]
    F --> G[修正问题并报告证据]
```

## ✨ 功能特性

| 能力 | 说明 |
| --- | --- |
| 明确任务边界 | 记录目标、不做的内容、完成条件、修改范围与验证方法 |
| 按风险调整流程 | Tiny、Standard、High-risk 三种模式，避免小改动承担过重流程 |
| 控制修改范围 | 遵守项目约定，保留用户已有修改，限制无关功能和依赖 |
| 用实际结果验收 | 完成前运行相关检查，报告命令、结果和无法验证的部分 |
| 独立只读审查 | 环境支持时交给独立审查者，按 Blocker、Important、Suggestion 分类 |
| 可选任务文件 | Python 脚本生成 `TASK.md`，已有文件会被保留 |

不会为每次编辑强制要求 TDD、Git worktree、提交、Pull Request 或长篇规格书。创建任务文件和安排审查的程度由任务复杂度决定。

## 🧱 技术与运行方式

| 部分 | 实现 |
| --- | --- |
| 工作流定义 | Markdown 格式的 `SKILL.md` 与参考文档 |
| Codex 展示配置 | `agents/openai.yaml` |
| 任务文件生成器 | Python 标准库，无额外第三方依赖 |
| 仓库测试 | Python `unittest` |
| 编程与审查执行 | 由宿主 Agent 及其可用工具完成 |

## 📁 目录结构

```text
coding-workflow/
├── SKILL.md                    # 工作流规则与使用条件
├── agents/openai.yaml          # Codex 名称与调用提示
├── references/
│   ├── task-brief.md           # 任务说明模板
│   ├── review-contract.md      # 审查输入、顺序与结论格式
│   └── provenance.md           # 设计来源与取舍
├── scripts/init_task.py        # TASK.md 生成器
├── tests/test_init_task.py     # 生成器测试
└── LICENSE
```

## 🚀 快速开始

### 1. 安装 Skill

以下命令使用默认的个人 Skill 目录，需要 Git 和支持 Skill 的 Codex 环境。

```bash
mkdir -p ~/.codex/skills
git clone https://github.com/RoourChen/coding-workflow.git ~/.codex/skills/coding-workflow
```

如果目标目录已存在，先检查已有安装，避免覆盖自己的修改。使用自定义 Skill 目录时，相应替换命令中的路径。

### 2. 在 Codex 中调用

让后续任务加载 Skill，然后输入具体需求。例如下面是一个虚构的功能请求。

```text
使用 $coding-workflow，为报表页增加 CSV 导出。
只修改导出相关逻辑，保留现有页面布局。
完成条件是导出的文件包含当前筛选后的全部记录，并正确处理中文和空值。
```

Agent 应说明修改范围、完成条件和验证结果。纯解释或纯代码审查任务不需要启动完整的实现流程。

### 3. 可选生成任务文件

脚本需要 Python 3，使用前可以查看参数。

```bash
python3 ~/.codex/skills/coding-workflow/scripts/init_task.py --help
```

在你的项目根目录执行下面的示例。请把目标和验证命令换成项目实际需要的内容。

```bash
python3 ~/.codex/skills/coding-workflow/scripts/init_task.py \
  --project . \
  --title "新增 CSV 导出" \
  --goal "用户可以导出当前筛选后的记录" \
  --non-goal "不修改页面布局" \
  --done "中文和空值能够正确导出" \
  --verify "python3 -m unittest discover -s tests -v" \
  --scope "报表导出逻辑及对应测试"
```

默认生成 `TASK.md`。可用 `--output` 指定项目内的相对路径；脚本拒绝覆盖已有文件，也拒绝写到项目目录之外。

## ⚙️ 模式与输出

| 模式 | 常见场景 | 预期产物 |
| --- | --- | --- |
| Tiny | 文案、明显且低风险的小改动 | 简短任务说明与相应检查 |
| Standard | 功能、缺陷修复、脚本 | 修改、验证证据，按需记录任务文件和审查结论 |
| High-risk | 认证、敏感数据、资金、迁移 | 详细边界、风险说明、相关回归检查与独立审查 |

仓库不需要配置 API Key。模型、文件访问、终端和独立审查能力由宿主环境提供；缺少独立审查工具时，应明确标注采用了自查。Skill 本身不授予部署、发布或额外数据访问权限。

## 🧪 开发与验证

在本仓库根目录运行。

```bash
python3 -m unittest discover -s tests -v
```

现有测试检查任务文件生成、拒绝覆盖和输出路径边界。它们验证辅助脚本，实际项目修改仍需运行该项目自身的检查。

若你的 Codex 环境安装了 `skill-creator` 的校验脚本，也可按该脚本的实际路径检查 Skill 元数据。

## 📚 更多文档与设计来源

- [完整工作流](SKILL.md)
- [任务说明模板](references/task-brief.md)
- [独立审查约定](references/review-contract.md)
- [设计来源、核查版本与取舍](references/provenance.md)

本项目独立实现了轻量流程，借鉴 `obra/superpowers` 和 `addyosmani/agent-skills` 的验证、审查与任务边界思想。`Macondooo/codex-research-examples` 在当时核查时未声明许可证，因此只参考概念，未复制文本或代码。

## 📄 许可证

[MIT](LICENSE)。

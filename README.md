# homework-review

用于批改作业、生成错题复习资料，以及为空白试卷生成全卷答案详解的 Codex 技能。

## 功能

- **作业批改**：保留原题号，逐题判定，生成完整批改报告、错题解析版 PDF 和无答案练习版 PDF。
- **空白试卷答案**：覆盖所有题目与小问，每题包含参考答案和详细解答过程，生成全卷答案详解 PDF 与可编辑 Markdown。
- **归档与核对**：按提交日期和科目保存，核对公式、图示与答案，标记不清晰或条件不足的题，保留修订版本。

## 安装

将仓库克隆到 Codex 的技能目录；如果同名目录已存在，请先比较内容，避免覆盖已有修改。

```sh
git clone https://github.com/escoffier/homework-review.git ~/.codex/skills/homework-review
```

也可以将本仓库完整目录复制到自定义 Codex 技能目录。

## 使用

在作业所在项目中提供照片、PDF 或文档，然后请求：

```text
$homework-review 批改今天的数学作业
```

```text
$homework-review 给这份空白试卷生成答案，每道题写详细解答过程，保存为PDF
```

输出遵循目标项目的 AGENTS.md 和已有目录约定；没有约定时，默认使用 assignments/、solutions/、review/、assets/，并更新项目 README.md 索引。技能安装目录不用于存放作业结果。

## 文件结构

- `SKILL.md`：技能入口、模式选择与工作流程。
- `agents/openai.yaml`：技能显示信息与默认调用示例。
- `references/output-contract.md`：输出、命名、归档和版本约定。
- `references/formula-verification.md`：易混公式核对流程。
- `scripts/inspect_formula.py`：原图局部裁切与放大工具。

## 环境与验证

生成 PDF 需要支持中文字体的 PDF 工具及渲染工具；执行时按当前环境可用能力选择，并逐页检查。局部公式核对工具需要 Python 3 和 Pillow：

```sh
python3 -m pip install Pillow
python3 scripts/inspect_formula.py --help
python3 scripts/inspect_formula.py INPUT.jpeg --box .08 .52 .49 .64 --output /tmp/formula-check
```

裁切坐标为经 EXIF 方向校正后的原图比例，输出目录须不存在，工具不会修改原图。无自动化测试套件；交付资料需核对题目、答案、过程及 PDF 排版，练习版还需检查答案泄漏。

+++
date = '2025-11-12T21:16:18+08:00'
draft = false
title = '删除-docx-空行工具脚本'
+++

本文介绍仓库内的脚本[源代码文件](./static/tools/dele_null_line.py)，它可以自动删除 `.docx` 文档中的空段落，并在非空段落中合并连续换行（将多个连续换行替换为一个）。脚本同时会处理表格单元格内的段落。

主要功能

- 删除文档正文中空的段落（完全没有可见字符的段落）。
- 在非空段落中把连续的 `\n` 合并为单个 `\n`，避免多余的空行或换行符导致格式混乱。
- 遍历文档内的表格，按单元格同样规则清理空段落并合并换行。
- 提供简单的 Tkinter GUI，交互选择输入/输出文件路径，适合非命令行用户。

依赖

- 使用 `python-docx`（包名 `python-docx`）来读写 Word 文档。仓库中的脚本示例使用 `from docx import Document`。

安装

    pip install python-docx

（如果要使用 live GUI，请确保当前 Python 环境包含 Tkinter。Windows 上自带标准 Python 通常包含 Tkinter。）

如何使用

- 图形界面（推荐，脚本默认行为）:

  - 运行脚本：

    python 原始内容文档/dele_null_line.py
  - 脚本会弹出文件选择对话框，请选择要处理的 `.docx` 文件，并指定输出文件名。
- 作为模块调用（在其他脚本中复用函数）:

  from 原始内容文档.dele_null_line import remove_empty_lines_from_docx
  remove_empty_lines_from_docx('input.docx', 'output.docx')

实现要点（供维护者参考）

- 段落处理：脚本先遍历 `doc.paragraphs`，把纯空的段落标记删除，非空段落使用正则 `re.sub(r"\n+","\n", text)` 合并连续换行。
- 表格处理：进入每个 `doc.tables`，对每个单元格的 `cell.paragraphs` 做同样的清理与合并。
- 删除操作：对要删除的段落或单元格段落，使用底层 XML 节点 `._element.getparent().remove(...)` 执行删除，避免改变段落集合时引发索引问题（通过反向索引删除）。

示例场景

- 批量格式化从其他来源复制粘贴到 Word 的内容，常见于论文、报告或网页复制导致的多余空行。
- 清理表格中因分行导致的冗余空段落，使单元格显示更整洁。

注意与限制

- 脚本基于 `python-docx` 的 API 操作，可能不会保留某些复杂样式或嵌入对象（图形/SmartArt 等）的精确格式。
- 删除空段落是以“纯文本为空”为判断标准；如果某些段落仅包含空白字符或不可见字符（特殊控制符），会被视为空并删除。
- 如果需要保留段落样式或分页断点，请在使用前备份原始文件。

改进建议

- 增加批处理（对目录下所有 `.docx` 文件递归处理）。
- 增加可选参数：是否保留段落样式、是否只处理正文不处理表格、备份原文件等。
- 在保存前增加简易的差异报告（列出删除的段落数、修改的单元格数），便于审计。

示例输出提示

脚本运行结束会打印：

    空行清理完成！输出文件：<output_path>

（UI 模式下会用弹窗告知完成情况。）

完整代码如下:

```
from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
import re

def remove_empty_lines_from_docx(input_path, output_path):
    doc = Document(input_path)

    # 段落：删除空段落，非空段落合并连续换行
    paragraphs = list(doc.paragraphs)
    to_delete = []
    for idx, p in enumerate(paragraphs):
        text = p.text or ""
        if text.strip() == "":
            to_delete.append(idx)
        else:
            p.text = re.sub(r"\n+", "\n", text)

    for idx in reversed(to_delete):
        paragraphs[idx]._element.getparent().remove(paragraphs[idx]._element)

    # 表格：删除单元格内空段落，非空段落合并连续换行
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                cell_paras = list(cell.paragraphs)
                del_idxs = []
                for i, cp in enumerate(cell_paras):
                    txt = cp.text or ""
                    if txt.strip() == "":
                        del_idxs.append(i)
                    else:
                        cp.text = re.sub(r"\n+", "\n", txt)
                for i in reversed(del_idxs):
                    cell_paras[i]._element.getparent().remove(cell_paras[i]._element)

    doc.save(output_path)
    print(f"空行清理完成！输出文件：{output_path}")

# ------------------- 调用示例 -------------------
import tkinter as tk
from tkinter import filedialog, messagebox


# 中文注释：通过图形界面选择输入与输出的 .docx 文件并执行清理
def main():
    try:
        root = tk.Tk()
        root.withdraw()

        input_path = filedialog.askopenfilename(
            title="选择输入 .docx 文件",
            filetypes=[("Word 文档", "*.docx")]
        )
        if not input_path:
            messagebox.showwarning("提示", "未选择输入文件，已取消。")
            return

        output_path = filedialog.asksaveasfilename(
            title="选择输出 .docx 文件",
            defaultextension=".docx",
            filetypes=[("Word 文档", "*.docx")]
        )
        if not output_path:
            messagebox.showwarning("提示", "未选择输出文件，已取消。")
            return

        remove_empty_lines_from_docx(input_path, output_path)
        messagebox.showinfo("完成", f"空行清理完成！\n输出文件：{output_path}")
    except Exception as e:
        try:
            messagebox.showerror("错误", f"处理失败：{e}")
        except Exception:
            print(f"处理失败：{e}")


if __name__ == "__main__":
    main()
```

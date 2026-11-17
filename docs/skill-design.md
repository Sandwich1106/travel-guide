# Skill 设计依据

2026-11-18 通过 GitHub API 查询的星数快照（会变化）：anthropics/skills 196601；vercel-labs/agent-skills 34325；obra/superpowers 319159。选取代表性项目，不声称全站排名，也不把星数当成质量证明。

| 一手参考 | 观察 | 本项目采用 |
| --- | --- | --- |
| [Anthropic skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) | 简短入口、按需资源、场景评估迭代 | 模式路由、保留专题、加入合成场景 |
| [Vercel web-design-guidelines](https://github.com/vercel-labs/agent-skills/blob/main/skills/web-design-guidelines/SKILL.md) | 精确触发、短执行流程、明确输出 | 精简 description，区分比较/规划/审查/文件模式 |
| [Superpowers writing-skills](https://github.com/obra/superpowers/blob/main/skills/writing-skills/SKILL.md) | 用真实失败改进规则，可机械检查则自动化 | 添加链接及结构验证；行为场景与静态验证分开 |

这是设计比较与独立重写，未复制第三方 Skill 正文，也未安装或执行第三方脚本。不引入与旅行无关的开发流程，不修改已有隐私、授权、预算与导图约束。行为评估目前仅提供可复用场景，未宣称完成基线对照实验。

目录：SKILL.md 为入口，references/ 为按需专题，agents/ 为现有界面元数据；根目录 scripts/ 维护验证，evals/ 保存无个人信息的评估请求。保留现有双语参考路径以避免破坏链接。

# 调研来源与采纳说明

调研日期为 2026-11-08。选取有代表性的公开来源，覆盖官方路线与风险、作者实测、中文游记和开源评测。这里记录方法如何进入 Skill，具体目的地的实时规则需要在实际规划时查。

| 来源 | 借鉴的方法 | 使用边界 |
| --- | --- | --- |
| [Nomadic Matt 的分阶段旅行规划](https://www.nomadicmatt.com/travel-blogs/how-to-plan-a-trip/) | 把预算、预订和出发准备拆进不同时间窗口，再整理成有依赖的任务清单 | 时间窗口随档期、退改和旅客条件调整 |
| [Earth Trekkers 的路线设计](https://www.earthtrekkers.com/how-to-design-around-the-world-itinerary/) | 地图先行，按季节筛选，避免每天高强度，把休息与灵活时间排进路线 | 长途经验按短途和同行者情况裁剪 |
| [The Travel Intern 的日本专题](https://thetravelintern.com/japan/) | 从首访、公共交通、自驾和预算等不同玩法发现候选，把攻略里的成本口径、时间和玩法一起记录 | 博主的历史花费、套票规则与促销价只作线索 |
| [携程旅行者的成都、乐山、重庆亲子实录](https://you.ctrip.com/travels/chengdu104/4152277.html) | 提取站内换乘、下车后步行、带孩子使用观光车等实际摩擦 | 车次、价格、预约及无障碍条件需要重新核验 |
| [日本国家旅游局主题路线](https://www.japan.travel/en/itineraries/) · [京都观光拥挤预测](https://global.kyoto.travel/en/comfort/) | 用主题串起片区，按时段处理拥挤和游玩顺序 | 预测用于安排时段，临近出发复查现场情况 |
| [中国领事服务网安全提醒](https://cs.mfa.gov.cn/aqtx/) · [日本外务省签证规则示例](https://www.mofa.go.jp/j_info/visit/visa/short/novisa.html) | 把旅行风险、入境与过境做成先行核验，并检查适用护照、日期及例外 | 每次按实际国籍、路线、停留及主管机关重新核验 |
| [TravelPlanner 开源仓库](https://github.com/OSU-NLP-Group/TravelPlanner) · [ICML 论文](https://proceedings.mlr.press/v235/xie24j.html) | 分开检查环境限制、用户硬约束和日程常识，再核对交通、夜数及总预算 | 借鉴评测框架。实际规划使用一手数据和实时查证 |

本项目自行编写 Skill 和模板。各来源承担不同角色：官方及经营方提供规则，实测帮助判断体验，开源研究帮助定义如何找出计划冲突。

## 多平台评价

[English sources](SOURCES.en.md) · [完整平台清单与比较方法](.agents/skills/travel-guide/references/community-evidence.md)

[Tripadvisor Forums](https://www.tripadvisor.com/ForumHome) 和 [Rick Steves Travel Forum](https://www.ricksteves.com/travel-forum) 用于查目的地和主题讨论。[Google 地图评价说明](https://support.google.com/maps/answer/6230175) 与 [Tabelog](https://tabelog.com/en/) 提供地点评价或当地餐饮线索。评价按地点、到访时段与旅客类型对照。根据当前可访问性替换来源。

## 出境实务补充来源

- 地图盲区：斐济旅游局、机场与长途巴士公司分别提供路线、上下车和时刻线索。适用日期仍需核对。[Tourism Fiji](https://www.fiji.travel/things-to-know/getting-around/land-airport-transfers) · [Fiji Airports](https://fijiairports.com/public-buses/) · [Pacific Transport](https://www.pacifictransport.com.fj/time-table.html)
- 低频接驳：水飞、塔纳岛国内航段与四驱接驳、汉密尔顿岛球车各有不同的销售渠道与条件。[Trans Maldivian Airways](https://www.transmaldivian.com/faq/) · [Vanuatu Tourism Office](https://www.vanuatu.travel/en/about-vanuatu/provinces/tafea/tanna) · [Hamilton Island Buggy Hire](https://www.hamiltonisland.com.au/getting-around-island/buggy-hire)
- 证件、通信、机票与健康的查询入口示例。[IATA Travel Centre](https://www.iata.org/en/travel-centre) · [Apple 国际旅行 eSIM](https://support.apple.com/en-gb/118227) · [Google Flights 价格洞察](https://support.google.com/travel/answer/6235879?hl=en) · [CDC 旅行健康](https://wwwnc.cdc.gov/travel/page/faq)

## 全球目的地排查

后续调研增加了地区差异和行程触发条件。各地案例帮助发现该查什么，具体规则仍按国家、城市、景区、出发日期和旅客条件确认。[分地区的一手入口与研究方法](.agents/skills/travel-guide/references/destination-discovery.md#简体中文)

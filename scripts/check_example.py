"""Validate a closed-world synthetic plan and render its daily cards."""
from pathlib import Path
import copy, json, html
ROOT=Path(__file__).resolve().parents[1]

def audit(d):
    errors=[]
    def check(ok,msg):
        if not ok: errors.append(msg)
    check(d['synthetic'] is True,'synthetic label')
    check([x['day'] for x in d['days']]==[1,2,3],'day coverage')
    check(d['lodging']['nights']==[1,2],'night coverage')
    check(d['lodging']['total']==d['lodging']['unit_price']*d['lodging']['units'],'lodging calculation')
    ids={};cost=d['lodging']['total']
    for day in d['days']:
        prev=0
        for e in day['events']:
            check(e['id'] not in ids,'unique IDs');ids[e['id']]=e
            check(prev<=e['start']<e['end']<=1440,'chronology')
            check(e['end']<=1200,'no late travel')
            check(e['source'] in d['sources'],'evidence reference')
            check(e['status']=='模拟数据，未预订','booking truthfulness')
            check(e['cost']>=0,'nonnegative cost')
            prev=e['end'];cost+=e['cost']
    b=d['booking'];e=ids[b['event']]
    check(e['start']==b['slot_start'] and e['end']==b['slot_end'],'booking slot')
    check(ids[b['arrival_event']]['end']<=e['start']-15,'booking arrival margin')
    check(cost+d['contingency']<=d['budget_cap'],'budget cap')
    check(d['paid']==0,'paid status')
    f=d['fallback'];old=ids[f['replaces']]
    check(f['start']==old['start'] and f['end']<=old['end'],'fallback downstream fit')
    check(f['decision_by']<f['start'],'fallback decision deadline')
    check(cost-old['cost']+f['cost']+d['contingency']<=d['budget_cap'],'fallback budget')
    return errors,cost

def run():
    d=json.loads((ROOT/'evals/fixtures/city-break.json').read_text());errors,cost=audit(d)
    assert not errors,errors
    negatives=[('overlap',lambda x:x['days'][0]['events'][1].update(start=550)),('budget',lambda x:x.update(budget_cap=1)),('missing night',lambda x:x['lodging'].update(nights=[1])),('invalid evidence',lambda x:x['days'][0]['events'][0].update(source='missing')),('late arrival',lambda x:x['booking'].update(arrival_event='D2E3')),('invalid fallback',lambda x:x['fallback'].update(end=800)),('false booking',lambda x:x['days'][0]['events'][0].update(status='已预订'))]
    for name,change in negatives:
        sample=copy.deepcopy(d);change(sample);assert audit(sample)[0],name
    md=['# '+d['title'],'','**模拟教学案例：不能用于真实订票。**','',f"2人，3天2晚；全部价格为虚构 TEST 单位。预算上限{d['budget_cap']}，消费{cost}，备用{d['contingency']}，余量{d['budget_cap']-cost-d['contingency']}；已付0，待付模拟消费全额。",'', '需求：建筑与慢游；不安排夜间长途移动。采用单一住宿基地，避免换酒店。备选方案为只玩街区、删除博物馆，可省160 TEST。']
    for day in d['days']:
        md+=['',f"## D{day['day']} {day['title']}",f"住宿：{day['overnight']}；强度：{day['effort']}"]
        for e in day['events']:
            clock=lambda n:f'{n//60:02}:{n%60:02}'
            md.append(f"- {clock(e['start'])}—{clock(e['end'])} {e['name']}｜{e['cost']} TEST/两人合计｜{e['status']}｜{e['id']}／S0")
    md+=['','## 住宿与生活安排','虚构中央旅舍：双人房300 TEST/间夜×2晚=600 TEST。选择依据为车站与活动区可公交抵达。模拟评价A认为方便，模拟评价B提示临街噪音，因此询问安静房；这些不是公开平台评价。备选住宿不采用，以免引入未核价订单。','餐饮为旅舍或活动片区简餐；未设过敏假设，真实旅客需询问。通信使用离线地址及地图；支付单位仅为测试，无真实汇率。','', '## 预订、备选与行前','博物馆：模拟提前30天09:00开售，提前24小时免费取消。到达比预约早15分钟。未发生任何交易。','关闭触发：D2 08:30决定改同片区免费公共建筑步行，10:00—12:00替代，午餐、回程、酒店不变，消费减少160 TEST。','行前核对车站、集合点、票据、通信和支付；备好步行鞋、雨具、饮水。真实紧急电话不在虚构案例中编造，应按实际所在地核验。','本例不跨境，不需要入境、国际航班、专项活动资格模块；不是把适用检查标为通过。','', '## 数据来源与适用范围','S0：evals/fixtures/city-break.json；2026-11-18整理，完全模拟。所有时刻、营业、条款、评价及价格仅为封闭测试条件。无现实安全、库存或经营方核验结论。']
    out=ROOT/'evals/outputs';out.mkdir(exist_ok=True)
    text='\n'.join(md)+'\n';(out/'city-break.md').write_text(text)
    (out/'city-break.html').write_text('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width"><title>虚构旅行自检案例</title><style>body{max-width:900px;margin:30px auto;padding:20px;font:17px/1.8 system-ui}pre{white-space:pre-wrap}</style><pre>'+html.escape(text)+'</pre>')
    report={'scope':'closed-world synthetic consistency only','cost':cost,'contingency':d['contingency'],'funding_total':cost+d['contingency'],'negative_cases_detected':[n for n,_ in negatives],'result':'PASS','not_claimed':['live operator verification','real-world safety or eligibility','independent model evaluation','editor roundtrip','PDF/spreadsheet/map output not requested in this case']}
    (out/'self-check.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':run()

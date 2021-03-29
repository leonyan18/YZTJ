# -*- coding: utf-8 -*-
"""
bz: "调剂特殊要求"
dwdm: "单位代码"
dwmc: "单位名称"
fbsjStr: "发布时间"
gxsj: "距离最后更新时间已过xx分钟"
hasit: "考生是否已经填报该志愿 true 或 false"
id: "余额信息ID"
qers: "余额人数"
sfmzyq: "是否满足要求，空为满足要求，非空其内容为不满足要求原因"
ssdm: "省市代码"
xxfs: "学习方式"
yjfxdm: "研究方向代码"
yjfxmc: "研究方向名称"
yxsdm: "院系所代码"
yxsmc: "院系所名称"
zt: "余额状态"
zydm: "专业代码"
zymc: "专业名称"
sfmzjybyq：是否符合
"""

import requests
import json
import csv as csvv

url = 'https://yz.chsi.com.cn/sytj/stu/sytjqexxcx.action'

headers = {
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://yz.chsi.com.cn',
    'Referer': 'https://yz.chsi.com.cn/sytj/tj/qecx.html',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36',
    'Cookie': 'JSESSIONID=52867175F3C5C1C72CD884147FE67F73; _ga=GA1.3.1252503280.1585280449; zg_did=%7B%22did%22%3A%20%221711a13fc2674f-0a6f62f5cd909a-f313f6d-100200-1711a13fc27576%22%7D; __utma=229973332.1252503280.1585280449.1600997311.1600997480.4; __utmz=65168252.1602730726.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); zg_90dc219b89ee40d99689b0ed4befbe51=%7B%22sid%22%3A%201607565320740%2C%22updated%22%3A%201607565320747%2C%22info%22%3A%201607565320745%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22vote.chsi.com.cn%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fxz.chsi.com.cn%2Fsurvey%2Findex.action%22%7D; zg_288ab1c4d4ac4d22b9a811f177cc6228=%7B%22sid%22%3A%201616677439253%2C%22updated%22%3A%201616677609352%2C%22info%22%3A%201616229785817%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22account.chsi.com.cn%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fbm.chsi.com.cn%2Fycms%2Fstu%2Fms%2Fhk%3Fpid%3Dmxsflz33060kw7zi%22%7D; zg_0d76434d9bb94abfaa16e1d5a3d82b52=%7B%22sid%22%3A%201616832746692%2C%22updated%22%3A%201616832790357%2C%22info%22%3A%201616832746698%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fmy.chsi.com.cn%2Farchive%2Findex.jsp%22%2C%22cuid%22%3A%20%22729ad9ad4cbdadc9c5df39bf5d3c6fb3%22%7D; zg_14e129856fe4458eb91a735923550aa6=%7B%22sid%22%3A%201616832671577%2C%22updated%22%3A%201616832793993%2C%22info%22%3A%201616832671582%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.chsi.com.cn%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fwww.chsi.com.cn%2F%22%7D; __utma=65168252.1252503280.1585280449.1602730726.1616832801.2; _gid=GA1.3.1567696842.1616986137; aliyungf_tc=cee07528fd4b84c7992b6f6edb85ad3cf42129a2ce2d3dec9f008e28841fb7c9; CHSICC_CLIENTFLAGYZ=8377e7254a41c376aa4cb1c508fb05fa; XSRF-CCKTOKEN=6ec5361c1e0cd2d3a0afaf49054c9e14; CHSICC_CLIENTFLAGSYTJ=adeca56df1908d8927ea5d9a609a31e2; acw_tc=707c9f7016169951093645531e3a6ade0c67d67c75fd68afa001be872c4a92; JSESSIONID=74F4F15AFCDEF875E0216CCB81FC0A97; zg_adfb574f9c54457db21741353c3b0aa7=%7B%22sid%22%3A%201616995113925%2C%22updated%22%3A%201616995865353%2C%22info%22%3A%201616821163344%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22%22%2C%22landHref%22%3A%20%22https%3A%2F%2Fyz.chsi.com.cn%2F%22%2C%22cuid%22%3A%20%22729ad9ad4cbdadc9c5df39bf5d3c6fb3%22%7D'
}
type_dict = {}
type_dict['1'] = "全日制"
type_dict['2'] = "非全日制"
content = ""
column = []
tag = []


def parse_one_page(content):
    for item in content:
        yield {
            'school': item['dwmc'],
            'academic': item['yxsmc'],
            'major': item['zymc'],
            'majorID': item['zydm'],
            'schoolID': item['dwdm'],
            'direction': item['yjfxmc'],
            'type': type_dict[str(item['xxfs'])],
            'remain': item['qers'],
            'publish': item['gxsj'],
            'ok': item['sfmzjybyq']
        }


# 为方便表格查看均用gbk
def write(flag, item):
    with open('tjinfo.csv', 'a', encoding='gbk') as csv:
        csv.write(flag + ',' + item['schoolID'] + ',' + item['school'] + ',' +
                  item['academic'] + ',' + item['major'] + ',' + item['majorID'] + ',' +
                  item['direction'] + ',' + str(item['type']) + ',' + str(item['remain']) + ',' + str(
            item['publish']) + ',' + str(item['ok']) + '\n')


# 读学校标签
with open("school.csv", encoding='gbk') as f:
    reader = csvv.reader(f)
    column = [row[2] for row in reader]
with open("school.csv", encoding='gbk') as f:
    reader = csvv.reader(f)
    tag = [row[0] for row in reader]
# 添加数据头
with open('tjinfo.csv', 'a', encoding='gbk') as csv:
    csv.seek(0)
    csv.truncate()
    csv.write('标记' + ',' + '学校编号' + ',' + '学校名称' + ',' + '所属学院' + ',' + '专业名称' + ','
              + '专业代码' + ',' + '研究方向' + ',' + '培养类型' + ','
              + '计划人数' + ',' + '距离最后更新时间已过分钟' + '\n')


# 关键词模糊查找
def doPost(keyword):
    para = {
        'pageSize': 20,
        'start': '',
        'orderBy': '',
        'mhcx': 1,
        'ssdm2': '',
        'xxfs2': '',
        'dwmc2': keyword,
        'data_type': 'json',
        'agent_from': 'wap',
        'pageid': ''
    }
    for i in range(0, 60):
        if i != 0:
            para['start'] = i * 20
        try:
            r = requests.post(url, headers=headers, timeout=30, data=para)
            r.raise_for_status()
            r.encoding = 'utf-8'
            # print (r.text)
            text = json.loads(r.text)
            content = text['data']['vo_list']['vos']
        except:
            continue

        for item in parse_one_page(content):
            try:
                pos = column.index(item['school'])
                write(tag[pos], item)
            except:
                write(' ', item)


doPost("计算机")
doPost("软件")
doPost("电子信息")
print("存入csv文件完成")

import requests
import json


url = "https://www.staples.com/searchux/api/productTileProxy/getProductTileData"

payload = {
    "serviceContext": {
        "tenant": "StaplesDotCom",
        "legacyTenant": 10001,
        "locale": "en-US",
        "channelId": "WEB",
        "siteId": "US",
        "zipCode": "92101",
        "langId": -1,
        "langCd": "en",
        "storeId": "10001",
        "user": {},
        "cisResponse": {}
    },
    "query": {
        "skus": ["2632689", "24394929", "24503030", "2632700", "24395072", "24424440", "2093839", "2093833"],
        "inputs": {
            "brandTransformationSwitch": True,
            "sparq": True,
            "pageType": "search"
        }
    }
}
headers = {
    "cookie": "STE=1; SMIDENTITY=yzeIsg0Q+PY+xTo17IvK/TUn2D56A4Ka2ebEBb7Hf38+MD4dzqeC+06glh/n7Bvb3EMCCpHdx0WVIgXWm8kOazWB2q4hHrdToHZwcFfwVF0jaNzyDGEKiwebtniMtAfQOoiEzFZ6cljvfHt65eNQd1sC7j45XnmOtGXogU4pxxjMg/Vf6qXy8MiX6P7a3S9XSrZaxqjr0HGYQC0uMk+qWo7WB1sthb+rvCHT16+QT89W8jkjVrOlWkFVBKKeDtNQJjP7xWR6tV2bV26CcdKECVRqiRQLwOaydWtN/vWSWa5LENNqb8hjirGugElQessHpCglBX39z7GbUV5x4aFXl3srZEsZzGCar0tpCyNTy0bx3LEBBh5w9La7x7XUVh4rRkpYVMBm251BgVXgGgIW32QN50axuTyZi2O/0MRsbWrPhU28eK9gcpijCCuHmCp+rv3WTINKNWC5op//+sJNGiHtSDYgIHJDygLfdkGo7JM5kJLmfq6YfiIWvP6a05iz0fEet1S4gI8FMQ3EnaOEXxapcHGof593flyiS9k25Kcdo/vcO3hnrtpGPhqcOY5B53ancbrdobNcRWqJKrKTnqThw2oz+3cVE+2MwA1cu11jXcon+3rer2q25VgmzQKHUf6Uk1WFGsc4J5c2HvolzSxlwu5r5Mgo3tyMSHVwt9U=; xdeviceid=ee3e583e29b7f84752a97746f21dd95f; ctx-token=97eb817ead2472ccc36d9c0f07cc8eacba84278d34ba84c598429becf087cf1e76f3cb9e00a5136b0149ceef92c93ecd76471b98de54a609ff660978f358f8ce92ffed; CSEG=1_UNIDENTIFIED; JSESSIONID=38f813da48a184d39258538a0582e7c6; SPAY=1; INT=0; zipcode=92101; geocode=32.7253,-117.1721; STE=1; akacd_EUF_PR=1725645616~rv=67~id=2cf339355838fcf3d26b1b040f2c3b2b; at_check=true; AMCVS_6822771A519160C10A490D4C%40AdobeOrg=1; s_ecid=MCMID%7C25009819866409995721829042176466417803; _blka_ruab=132; _blka_a=hijack_shopper-on; _blka_engage=%7B%7D; PTALTSD=Y; ATSEARCHC=Y; ECUF_SESSION_ID=eb5aca; notice_behavior=implied,us; salsify_session_id=9d6c2722-809c-44f7-9c9e-b000c856d9f7; _svsid=788ce1e8539381423ef3feda28c5954f; _svsidss=788ce1e8539381423ef3feda28c5954f; c_m=Googlewww.google.com; s_campaign=seo%3AGoogle; s_v47_persist=No%20S_VI%20Cookie; s_cc=true; _gcl_au=1.1.2096077335.1715277625; __attentive_id=e1afe62025d64ab3a0ea4ad976b8b818; _attn_=eyJ1Ijoie1wiY29cIjoxNzE1Mjc3NjI0OTIzLFwidW9cIjoxNzE1Mjc3NjI0OTIzLFwibWFcIjoyMTkwMCxcImluXCI6ZmFsc2UsXCJ2YWxcIjpcImUxYWZlNjIwMjVkNjRhYjNhMGVhNGFkOTc2YjhiODE4XCJ9In0=; __attentive_cco=1715277624926; cjConsent=MHxOfDB8Tnww; cjUser=c29c16cc-6df1-4fae-9b7e-a36602f919f6; cjLiveRampLastCall=2024-05-09T18:00:25.404Z; RoktRecogniser=650eb60e-19f3-406f-99e0-c04ab9cb0f7f; __exponea_etc__=a6302fb5-1907-43de-9da7-5687bd779d48; _fbp=fb.1.1715277625988.1360935417; _pin_unauth=dWlkPU1tVmpOV1k0TkdNdE5qVXhZaTAwTldFNExXRTBNVGd0TkdZeVl6STFNamRrTldJeA; _mkto_trk=id:896-JNU-907&token:_mch-staples.com-1715277626398-65136; cvp_cha=%5B%5B%27Natural%2520Search%27%2C%271715277668998%27%5D%5D; ev1=mounts; productnum=1; _taggstar_vid=1e01af7c-0e2e-11ef-b788-fbb0d10011a9; mboxEdgeCluster=35; s_cpc=0; s_sq=%5B%5BB%5D%5D; _abck=5979763FA1FB352FC0AD2EAC18E4D004~0~YAAQiXfZF/yweGyPAQAAXF+6cgu8CvqVZhJT5NjlZzkbEKsg41EEb1+nPLTevyeUQJw75kXLnQ+sfTWevpOxxjJ+w+Mv0HY+1yCwBdAq2vNIXcgCcBW1uUVbgrP+X2DnQJqThgw/KHDNrhXDWFSEhfmHtUMgTaNBZvoaG2cE/Yz6b/TveDWEwCtsbW5F0bIyPhweeWOBg8AcMYoSlbSaUxjZg+nubqpeJBsxN1IQfrWM897md8daYsuB/+ra5PLwzqQrtERRGKlUeW5dprQMM3amnN4bBHiTe0nfDJDXbP1G1VaSGdCk3ljFnnxeBG0acyuffW1WmtkXYD+ZZsWNx3stLkuYdCpgrNWJtCElw9Emi6NOVkzjicyu5VKKH8GPIKiwUMyYC8IJuvwqKX3Gnq/3IqywSaAoew==~-1~-1~-1; AMCV_6822771A519160C10A490D4C%40AdobeOrg=1585540135%7CMCIDTS%7C19857%7CMCMID%7C25009819866409995721829042176466417803%7CMCAAMLH-1716221569%7C9%7CMCAAMB-1716221569%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1715623969s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.4.0; _taggstar_exp_grp=treatment-v5; _svidobj={'mid':null,'dcn':null,'rewards_number':null,'email_addr':null,'confidence_score':null}; kndctr_6822771A519160C10A490D4C_AdobeOrg_identity=CiYyNTAwOTgxOTg2NjQwOTk5NTcyMTgyOTA0MjE3NjQ2NjQxNzgwM1IQCPrUjfT1MRgBKgNPUjIwA%5FAB6Ybqlfcx; _gid=GA1.2.104848214.1715616780; __attentive_dv=1; __gads=ID=41057aa774551032:T=1715277636:RT=1715620661:S=ALNI_MZLUXsBPpFSDrErbogLof5YnPtniA; __gpi=UID=00000e0542facbf3:T=1715277636:RT=1715620661:S=ALNI_MYv4Od4gwILRC4gC_62-6hq2j8AWw; __eoi=ID=89d225be2a69ef8d:T=1715277636:RT=1715620661:S=AA-Afjbu0zT5B1wylibMSI_KmOwc; SBKT=nc4; AKA_A2=A; __blka_ts=1715622493348; FCNEC=%5B%5B%22AKsRol-xyObUrlf1FNsUzxFYHzy0DELeEtuf_kBSAoLJLPiSDJNd610SfiK_4DhRKl5LbdYMZW_7qrozzl2sq-srLYQ9iUmAxkLbRAq_EaoP4beZ9RdVk5djgD88xi_CLO9rlNtny0tHu5dBvieLGiBfyv2rOha2JA%3D%3D%22%5D%5D; TAsessionID=8e09c58d-757d-4649-b308-20894dc3aa31|NEW; s_tp=10975; kndctr_6822771A519160C10A490D4C_AdobeOrg_cluster=or2; s_nr30=1715620701862-Repeat; s_tslv=1715620701863; s_inv=3923; s_dur=1715620701863; s_vncm=1717225199300%26vn%3D6; s_ivc=true; gpv_c51=https%3A%2F%2Fwww.staples.com%2Fmounts%2Fdirectory_mounts%3Fpn%3D1; gpv_dlo_pn=search; _br_uid_2=uid%3D7624773744221%3Av%3D11.8%3Ats%3D1715277625733%3Ahc%3D25; _uetsid=ab486180114311efad2f233726567670; _uetvid=033e57e00e2e11efb7a7d73b0dd7e993; __exponea_time2__=-0.2792658805847168; _ga=GA1.2.1817253174.1715277625; __attentive_creativeFilter=1_UNIDENTIFIED; __attentive_pv=1; __attentive_ss_referrer=ORGANIC; inside-stp=1043368466-c124170c44619b572e81380caca30c193081041194fa8e52d284064705c75ddf-0-0; _taggstar_ses=ce4d46d5-114c-11ef-a595-b5b1454f25d7; gpv_pn=Search%20Results; s_ips=1128.3999938964844; s_ppv=Search%2520Results%2C42%2C10%2C5032%2C6%2C16; bm_sz=646C1380EE9B8DBC16857D3958EFFAF1~YAAQiXfZF+SjjmyPAQAAkuv7checQmOmUqMxL8qdlhYnGTTf/aSPu7Uf8c5H3GNhoMtSUNFhG+pPL4DnSjzOLZA+bskSvUV6Sk8ONj2XJ7mSqyIIcu8r3nA4wN2ddrdMiGF+MPzitfZqkHnrVSW8wyHqWV5LHRjNM5KIHTTTM3Rf40G+EfTQOZNvAMZgYHvh5krnkdov0lvLAUvsDP34qhStMhuunct8HWo6tuy/kCAVRksLRXK/ujKtCd/mKZo6WGqNxbUjMsStu4PGicWSBQgM4Aq/LS4mvzsPm2Kvicf1qqnYLX2XIZxefaC5RHT+Ig5ZYcQboQCl6HGEnnPSofZZ2RtUdo/CBO+p0lMJVyomcATolkpx6brUgCPZhNawsxzgo0+EKsehhf7Ek7/G4IOKVSMvxzEEfqvgaNtb~4599858~4339764; _ga_GJ9W4FPBWL=GS1.1.1715620691.6.1.1715621064.60.0.0; RT='z=1&dm=www.staples.com&si=6c45d72a-140d-4eef-a104-8a7aa6fedc34&ss=lw589gx3&sl=1&tt=4x4&rl=1'; mbox=session#cbddcf20877b4490b10b7195f9bd2d74#1715622926|PC#cfd3338e98524fddad5390da5c6c192d.35_0#1778865866; akavpau_vp1=1715621365~id=022f7fc18de5eebaad9c5a06027ce707; fs_lua=1.1715621065963; fs_uid=#PPE96#390d1af8-9698-4d3c-a55a-2be5018ac25f:0bd36667-ddd9-439a-b2b6-f56c89a26227:1715620662345::3#/1746813644",
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "content-type": "application/json;charset=UTF-8",
    "newrelic": "eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjE5ODk3NTQiLCJhcCI6Ijc4MTkyNDYxNiIsImlkIjoiNTNkMGE1MGYzN2QzZmRhMiIsInRyIjoiOTk2NTUyZmM5ZjZjZDIyYmE3Y2I0OWQ4ZjMxMTYwNGUiLCJ0aSI6MTcxNTYyMTA2NjAwMiwidGsiOiIxODg3OTgyIn19",
    "origin": "https://www.staples.com",
    "priority": "u=1, i",
    "referer": "https://www.staples.com/mounts/directory_mounts?pn=1",
    "sec-ch-ua": '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "traceparent": "00-996552fc9f6cd22ba7cb49d8f311604e-53d0a50f37d3fda2-01",
    "tracestate": "1887982@nr=0-1-1989754-781924616-53d0a50f37d3fda2----1715621066002",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "x-http-encode": "true"
}

response = requests.request("POST", url, json=payload, headers=headers)

content = response.text

data = json.loads(content)

for model in data:
    print(model['model']+ ",", model['priceValue'])
    

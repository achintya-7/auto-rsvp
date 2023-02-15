import requests
import json

cookies = {
    'MEETUP_BROWSER_ID': 'id=524e5c16-f6c5-48ab-b768-54cc5af392d9',
    'SIFT_SESSION_ID': '41546715-29f8-4c7a-9bcb-3ec423c37dda',
    '_rm': 'c9097662-0f30-4eee-b65a-ab3b8efdfd3e',
    '_gcl_au': '1.1.1665618594.1676434103',
    '_scid': 'e798c00c-8e40-44be-b23d-0ad5319d5e76',
    'cjConsent': 'MHxOfDB8Tnww',
    '_gid': 'GA1.2.1224783358.1676434103',
    'cjCountry': 'IN',
    'cjUser': 'c7a69bfd%2D6859%2D48b5%2D9b32%2D27c414760dee',
    '_fbp': 'fb.1.1676434104105.1612997418',
    '_schn': '_lxi87w',
    '_sctr': '1|1676399400000',
    '___uLangPref': 'en_US',
    'MEETUP_LANGUAGE': 'language=en&country=US',
    'enable_fundraising_pledge_banner_show': 'true',
    'ab.storage.deviceId.4e505175-14eb-44b5-b07f-b0edb6050714': '%7B%22g%22%3A%22057e659f-a1e1-41bf-e2b4-648cd9a1ab35%22%2C%22c%22%3A1676434156503%2C%22l%22%3A1676434156885%7D',
    'ab.storage.userId.4e505175-14eb-44b5-b07f-b0edb6050714': '%7B%22g%22%3A%22384413740%22%2C%22c%22%3A1676434156882%2C%22l%22%3A1676434156886%7D',
    'fs.bot.check': 'true',
    'fs.session.id': 'b9fb37ca-9b7f-4105-acd3-09d2f4344c03',
    'MEETUP_MEMBER_LOCATION': '{%22__typename%22:%22Location%22%2C%22city%22:%22Delhi%22%2C%22country%22:%22in%22%2C%22localized_country_name%22:%22in%22%2C%22state%22:%22%22%2C%22name_string%22:%22Delhi%2C%20India%2C%20meetup2%22%2C%22lat%22:28.670000076293945%2C%22lon%22:77.20999908447266%2C%22zip%22:%22meetup2%22%2C%22borough%22:%22%22%2C%22neighborhood%22:%22%22}',
    'ab.storage.sessionId.4e505175-14eb-44b5-b07f-b0edb6050714': '%7B%22g%22%3A%2282c6db73-dd9c-550d-a655-93f2ead6bf22%22%2C%22e%22%3A1676436285804%2C%22c%22%3A1676434156884%2C%22l%22%3A1676434485804%7D',
    '_dc_gtm_UA-3226337-19': '1',
    '__Host-NEXT_MEETUP_CSRF': 'f72d45a4-aa39-4d17-a895-25cd32e67984',
    'MEETUP_TRACK': 'id=3e019f35-1122-4103-b10f-659a32408e89&l=1&s=19565b5fa713629f1afffacbe93d82f63a143ab0',
    'MEETUP_SEGMENT': 'member',
    'MEETUP_MEMBER': '""',
    'MEETUP_SESSION': '""',
    'MF_fbconnect_clear': 'm=1&s=28dc982ec2cda8da3a5f5adbd27a94012924d65a',
    '_uetsid': '63ba72d0ace611ed98423f2745e904ed',
    '_uetvid': '63baadf0ace611edaf6943549c543b72',
    'OptanonConsent': 'isGpcEnabled=0&datestamp=Wed+Feb+15+2023+09%3A44%3A59+GMT%2B0530+(India+Standard+Time)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=26157bc6-59ed-4ee6-8be2-ab7415699a06&interactionCount=0&landingPath=NotLandingPage&groups=C0002%3A1%2CC0001%3A1%2CC0004%3A1%2CC0003%3A1&AwaitingReconsent=false',
    '_ga': 'GA1.2.691906353.1676434103',
    '_ga_NP82XMKW0P': 'GS1.1.1676434103.1.1.1676434506.41.0.0',
}

headers = {
    'authority': 'www.meetup.com',
    'accept': '*/*',
    'accept-language': 'en-US',
    'apollographql-client-name': 'nextjs-web',
    'content-type': 'application/json',
    # 'cookie': 'MEETUP_BROWSER_ID=id=524e5c16-f6c5-48ab-b768-54cc5af392d9; SIFT_SESSION_ID=41546715-29f8-4c7a-9bcb-3ec423c37dda; _rm=c9097662-0f30-4eee-b65a-ab3b8efdfd3e; _gcl_au=1.1.1665618594.1676434103; _scid=e798c00c-8e40-44be-b23d-0ad5319d5e76; cjConsent=MHxOfDB8Tnww; _gid=GA1.2.1224783358.1676434103; cjCountry=IN; cjUser=c7a69bfd%2D6859%2D48b5%2D9b32%2D27c414760dee; _fbp=fb.1.1676434104105.1612997418; _schn=_lxi87w; _sctr=1|1676399400000; ___uLangPref=en_US; MEETUP_LANGUAGE=language=en&country=US; enable_fundraising_pledge_banner_show=true; ab.storage.deviceId.4e505175-14eb-44b5-b07f-b0edb6050714=%7B%22g%22%3A%22057e659f-a1e1-41bf-e2b4-648cd9a1ab35%22%2C%22c%22%3A1676434156503%2C%22l%22%3A1676434156885%7D; ab.storage.userId.4e505175-14eb-44b5-b07f-b0edb6050714=%7B%22g%22%3A%22384413740%22%2C%22c%22%3A1676434156882%2C%22l%22%3A1676434156886%7D; fs.bot.check=true; fs.session.id=b9fb37ca-9b7f-4105-acd3-09d2f4344c03; MEETUP_MEMBER_LOCATION={%22__typename%22:%22Location%22%2C%22city%22:%22Delhi%22%2C%22country%22:%22in%22%2C%22localized_country_name%22:%22in%22%2C%22state%22:%22%22%2C%22name_string%22:%22Delhi%2C%20India%2C%20meetup2%22%2C%22lat%22:28.670000076293945%2C%22lon%22:77.20999908447266%2C%22zip%22:%22meetup2%22%2C%22borough%22:%22%22%2C%22neighborhood%22:%22%22}; ab.storage.sessionId.4e505175-14eb-44b5-b07f-b0edb6050714=%7B%22g%22%3A%2282c6db73-dd9c-550d-a655-93f2ead6bf22%22%2C%22e%22%3A1676436285804%2C%22c%22%3A1676434156884%2C%22l%22%3A1676434485804%7D; _dc_gtm_UA-3226337-19=1; __Host-NEXT_MEETUP_CSRF=f72d45a4-aa39-4d17-a895-25cd32e67984; MEETUP_TRACK=id=3e019f35-1122-4103-b10f-659a32408e89&l=1&s=19565b5fa713629f1afffacbe93d82f63a143ab0; MEETUP_SEGMENT=member; MEETUP_MEMBER=""; MEETUP_SESSION=""; MF_fbconnect_clear=m=1&s=28dc982ec2cda8da3a5f5adbd27a94012924d65a; _uetsid=63ba72d0ace611ed98423f2745e904ed; _uetvid=63baadf0ace611edaf6943549c543b72; OptanonConsent=isGpcEnabled=0&datestamp=Wed+Feb+15+2023+09%3A44%3A59+GMT%2B0530+(India+Standard+Time)&version=202211.2.0&isIABGlobal=false&hosts=&consentId=26157bc6-59ed-4ee6-8be2-ab7415699a06&interactionCount=0&landingPath=NotLandingPage&groups=C0002%3A1%2CC0001%3A1%2CC0004%3A1%2CC0003%3A1&AwaitingReconsent=false; _ga=GA1.2.691906353.1676434103; _ga_NP82XMKW0P=GS1.1.1676434103.1.1.1676434506.41.0.0',
    'next_csrf': '41293dbb-6694-4f9d-b558-1e4d7ed9e37a',
    'origin': 'https://www.meetup.com',
    'referer': 'https://www.meetup.com/',
    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
    'x-meetup-view-id': '2b8d0939-8b54-4a10-89fe-1283370804cb',
    'x-tracking-request-id': 'efbad6c2-529d-4182-a6ca-cb30fe819d74',
}

json_data = {
    'operationName': 'login',
    'variables': {
        'input': {
            'email': 'achintya.x7.2@gmail.com',
            'password': '@Achintya2205@',
            'rememberMe': True,
        },
    },
    'extensions': {
        'persistedQuery': {
            'version': 1,
            'sha256Hash': '27c2dcd3fe18741b545abf6918eb37aee203463028503aa8b2b959dc1c7aa007',
        },
    },
}

response = requests.post('https://www.meetup.com/gql', cookies=cookies, headers=headers, json=json_data)
json_resp = response.json()
print(json_resp['data']['login']['memberId'])
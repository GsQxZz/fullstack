# __author: Administrator
# date:  2020/7/15

menu = {
    '北京': {
        '朝阳': {
            '国贸': {
                'CICC': {},
                'HP': {},
                '渣打银行': {},
                'CCTV': {}
            },
            '望京': {
                '陌陌': {},
                '奔驰': {},
                '360': {}
            },
            '三里屯': {
                '优衣库': {},
                'apple': {}
            }
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '阿泰包子': {}
            },
            '天通苑': {
                '链家': {},
                '我爱我家': {}
            },
            '回龙观': {}
        },
        '海淀': {
            '五道口': {
                '谷歌': {},
                '网易': {},
                'Sohu': {},
                'Sogo': {},
                '快手': {}
            },
            '中关村': {
                'youku': {},
                'Iqiyi': {},
                '汽车之家': {},
                '新东方': {},
                'QQ': {}
            }
        },
    },
    '上海': {
        '浦东': {
            '陆家嘴': {
                'CICC': {},
                '高盛': {},
                '摩根': {}
            },
            '外滩': {}
        },
        '闵行': {},
        '静安': {}
    },
    '山东': {
        '济南': {},
        '德州': {
            '乐陵': {
                '丁乌镇': {},
                '城区': {}
            },
            '平原': {}
        },
        '青岛': {}
    }
}

current_layer = menu
prev_layer = []

while True:
    for key in current_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0:continue
    if choice in current_layer:
        # prev_layer = current_layer
        prev_layer.append(current_layer)
        current_layer = current_layer[choice]
    elif choice.lower() == 'b':
        # current_layer = prev_layer
        if prev_layer:
            current_layer = prev_layer.pop()
    elif choice.lower() == 'q':
        break
    else:
        print("无此项")
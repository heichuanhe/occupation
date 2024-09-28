import random
import json
from collections import Counter

#将所有职业放入到一个集合中
occuptions = ['死亡骑士','恶魔猎手','法师','术士','战士',
              '圣骑士','猎人','牧师','德鲁伊','武僧','萨满','唤魔师','盗贼']
file_path = 'occuption.json'



#按照值将字典排序
def sort_dict(dictionary):
    return dict(sorted(dictionary.items(),key=lambda item:item[1],reverse=True))



#将roll到的数据转化为json格式存储到json文件中
def json_occuption(sorted_dict):
    with open(file_path,'a',encoding='utf-8') as f:
        json.dump(sorted_dict,f,ensure_ascii=False)
        f.write('\n')




#清空json文件
def clear_json():
    with open(file_path,'w',encoding='utf-8') as f:
        f.truncate()



#roll一次职业（创建一个字典，职业为键，
#1-100的随机数为值，根据值的大小按降序排列字典，值最大的天命职业）
def roll_occuption_1():
    #构造职业：随机数 的字典
    occuption_dict = {occuption:random.randint(1,100) for occuption in occuptions}
    #按照值将字典排序
    sorted_dict = sort_dict(occuption_dict)
    occuption = list(sorted_dict.keys())
    sorted_dict.update({'你的天命职业是':occuption[0]})
    json_occuption(sorted_dict)
    print(occuption_dict)
    print('-----------------')
    print(sorted_dict)
    print(f'重活一世，您将以\'{occuption[0]}\'的身份降临艾泽拉斯大陆！')



#roll100次
def roll_occuption_100():
    counter = 1
    while counter<=100:
        counter += 1
        roll_occuption_1()
    occpution_analyze()



#解析json文件，将所有json数据中'天命职业'
def occpution_analyze():
    mandant_list = []   #将json中所有 键为’你的天命职业是‘的值放入该集合
    with open(file_path,'r',encoding='utf-8')as f:
        for line in f:
            try:
                data = json.loads(line)
                mandant_list.append(data.get('你的天命职业是'))



            except json.decoder.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")
    mandant_dict = Counter(mandant_list)
    sorted_dict = sort_dict(mandant_dict)
    occuption = list(sorted_dict.keys())
    print(f'经过数百个轮回，现您已在艾泽拉斯大陆重生为：{occuption[0]}')
    print(sorted_dict)
    clear_json()






def main():
    roll_occuption_1()




if __name__  == '__main__':
    main()


    
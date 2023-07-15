#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "当前时间:" + time.asctime(t)
 
print(str);



CREATE TABLE herbs (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  pinyin VARCHAR(100) NOT NULL,
  category VARCHAR(100) NOT NULL,
  channel VARCHAR(100) NOT NULL,
  function VARCHAR(200) NOT NULL
);

INSERT INTO herbs (name, pinyin, category, channel, function) VALUES
('当归', 'dang gui', '补血', '肝经', '滋补、调经'),
('川芎', 'chuan xiong', '活血', '肝经', '活血、行气'),
('桂枝', 'gui zhi', '汗剂', '手太阴肺经、足阳明胃经', '发汗、温通'),
('白芍', 'bai shao', '补血', '肝经', '补肝、调经'),
('黄芪', 'huang qi', '益气', '脾经、肺经', '益气、升阳'),
('天麻', 'tian ma', '止风', '肝经', '平肝、止风'),
('白术', 'bai shu', '健脾', '脾经', '健脾、止泻'),
('陈皮', 'chen pi', '理气', '胃经、脾经', '理气、燥湿'),
('枸杞', 'gou qi', '滋阴', '肝经、肾经', '益肝、肾、明目'),
('茯苓', 'fu ling', '利水', '心经、肺经、脾经、肾经', '利水、健脾');

CREATE TABLE prescriptions (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  pinyin VARCHAR(100) NOT NULL,
  category VARCHAR(100) NOT NULL,
  ingredients TEXT NOT NULL,
  preparation TEXT NOT NULL,
  usage TEXT NOT NULL,
  function TEXT NOT NULL
);

INSERT INTO prescriptions (name, pinyin, category, ingredients, preparation, usage, function) VALUES
('四物汤', 'si wu tang', '补血', '当归9g、熟地9g、白芍12g、川芎6g', '将药物水煎后代茶服', '用于女子补血、调经', '补气养血、调和营血'),
('桂枝汤', 'gui zhi tang', '汗剂', '桂枝6g、生姜3g、大枣3枚、甘草3g', '将药物水煎后代茶服', '用于解表、温通阳气', '解表、温通'),
('理中丸', 'li zhong wan', '健脾', '人参4g、白术4g、茯苓4g、炙甘草2g、大枣4枚', '将药物研末下丸，用水送服', '用于养脾健胃', '健脾和胃、益气生津'),
('加减柴芩汤', 'jia jian chai qin tang', '清热利湿', '柴胡10-12g、黄芩5-10g、赤茯苓10-15g、栀子10-12g、车前草15-20g、苦参10g、茯苓10g、玄参10g、泽泻10g、甘草3g', '将柴胡、黄芩、赤茯苓、栀子、车前草入凉水中共煎，去渣后加入苦参、茯苓、玄参、泽泻及甘草再煎一次，去渣取汁，再加入第一次煎剩下的甜水中调匀，煮沸即成', '用于湿热泻痢、黄疸、小便不利等', '清热利湿、化痰、止血、解毒'),
('十全大补汤', 'shi quan da bu tang', '益气补血', '人参10g、黄芪30g、当归10g、白术10g、茯苓10g、党参10g、熟地10g、巴戟天10g、桂枝6g、甘草5g', '将药物加水煎煮，去渣取汁', '用于气血两虚', '补气、益血、和营、消癥、温经'),
('麻杏石甘汤', 'ma xing shi gan tang', '止咳平喘', '麻黄6g、杏仁6g、石膏30g、甘草6g', '将药物煎煮，去渣取汁', '用于感冒、咳嗽、气喘', '清热化痰、平喘、解毒'),
('益肺汤', 'yi fei tang', '养阴清热', '知母10g、石斛12g、罗汉果9g、百合20g、天门冬15g、川贝母10g、杏仁10g、栀子10g、黄芩10g、甘草6g', '将药物加水煎煮，去渣取汁', '用于肺热咳嗽、咳痰等', '清热润肺、化痰止咳、祛瘀止痛、祛湿通窍'),
('逍遥散', 'xiao yao san', '理气', '柴胡6g、白芍9g、熟地6g、川芎6g、当归6g、茯苓6g、香附6g、木香6g、生姜3g、甘草3g', '将药物加水煎煮，去渣取汁', '用于胸胁胀痛、月经不调等', '舒肝健脾、调和气血、止痛解郁、调节免疫'),
('牛黄清胆丸', 'niu huang qing dan wan', '清热解毒', '黄连3g、黄芩3g、栀子3g、黄柏3g、丹皮3g、生石膏5g、水牛黄1g', '将药物研末后用蜜汁调制成丸', '用于热毒疮疡、急性化脓性扁桃体炎等', '清热解毒、凉血止血、杀菌消炎'),
('十味珍珠丸', 'shi wei zhen zhu wan', '平肝安神', '珍珠粉6g、首乌藤15g、枸杞子6g、麦冬10g、菟丝子6g、山茱萸10g、巴戟天12g、熟地黄12g、五味子6g、丹皮10g', '将药物研末后用蜂蜜调制成丸', '用于肝肾不足、失眠多梦等', '平肝安神、养肝补肾、抗衰安眠'),
('苓桂术甘汤', 'ling gui shu gan tang', '温经散寒', '白术9g、茯苓9g、桂枝9g、甘草6g', '将药物水煎后代茶服', '用于胃脘冷痛、白带清稀等', '温经散寒、健脾和胃、除湿化痰'),
('加味逍遥散', 'jia wei xiao yao san', '理气', '柴胡6g、白芍9g、熟地6g、川芎6g、当归6g、茯苓6g、香附6g、木香6g、生姜3g、甘草3g、乌骨6g、厚朴9g、枳实9g', '将药物加水煎煮，去渣取汁', '用于胸胁胀痛、月经不调等', '舒肝健脾、调和气血、止痛解郁、调节免疫'),
('石膏汤', 'shi gao tang', '解表', '石膏45g、桂枝9g、芍药9g、甘草6g、生姜9g', '将药物水煎后代茶服', '用于表热、高热等', '解表、清热、生津、止渴'),
('茵陈蒿汤', 'yin chen hao tang', '清热泻黄', '茵陈8g、蒿本8g、大黄4g、麻黄根4g、芒硝6g、决明6g', '将药物水煎后代茶服', '用于黄疸病，脾胃不和，泻吐腹痛等', '清热泻火、燥湿泻黄、消肿宽中'),
('桃仁承气汤', 'tao ren cheng qi tang', '下气通便', '桃仁10g、白芍12g、大枣12枚、厚朴9g、枳壳6g、甘草6g、生姜2片', '将药物水煎后代茶服', '用于肠燥便秘，大腹痛等', '泻实消积、通利下行'),
('六君子汤', 'liu jun zi tang', '健脾消食', '人参9g、黄芪12g、白术9g、炙甘草6g、干姜3g、大枣四枚', '将药物水煎后代茶服', '用于脾胃虚弱，纳呆腹胀等', '健脾和胃、升阳固脱'),
('麻黄汤', 'ma huang tang', '祛风散寒', '麻黄9g、桂枝9g、杏仁9g、甘草6g', '将药物水煎后代茶服', '用于感冒头痛、发热等', '祛风散寒、宣肺解毒、祛湿透疹'),
('温胆汤', 'wen dan tang', '和胆通便', '大黄15g、白芍6g、泽泻6g、木香6g、黄芩6g、生姜6g、厚朴6g、花椒6g、甘草6g、干草果6g', '将药物水煎后代茶服', '用于胆道蛔虫，胆道积水，胆囊炎等', '疏利胆道、通便腹痛、解毒泻肠、杀虫消积'),
('阳和汤', 'yang he tang', '升阳固脱', '人参6g、白术6g、茯苓6g、炙甘草3g、干姜3g、半夏3g、黄芪6g、熟地6g、制附子半个', '将药物加水煎煮，去渣取汁', '用于虚寒脱肛，脱肾等', '益气固脱、

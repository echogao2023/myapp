#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "当前时间:" + time.asctime(t)
 
print(str);
import os
import jieba
import numpy as np
import tensorflow as tf
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel

# 准备训练数据并进行分词
data_path = "zhongyi_data.txt"
with open(data_path, "r", encoding="utf-8") as f:
    data = f.readlines()

jieba.setLogLevel(20)
texts = []
for text in data:
    words = [w for w in jieba.cut(text.strip()) if w]
    texts.append(" ".join(words))

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

# 将所有样本编码到输入张量中
input_ids_list = []
for text in texts:
    input_ids = tokenizer.encode(text, add_special_tokens=True, return_tensors="tf")
    if len(input_ids[0]) > 1024:   # 忽略超长文本
        continue
    input_ids_list.append(input_ids)

max_length = max(len(ids[0]) for ids in input_ids_list)
inputs = tf.stack([tf.pad(ids, [[0, 0], [0, max_length - len(ids[0])]], mode='CONSTANT') for ids in input_ids_list])

# 创建attention mask张量
mask = tf.where(inputs != 0, 1, 0)

# 初始化GPT-2模型，并调用compile函数编译
model = TFGPT2LMHeadModel.from_pretrained("gpt2")
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=5e-5),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))

# 模型微调
model.fit(inputs, inputs, epochs=3, batch_size=8)

# 保存微调后的模型
model_path = "./my_model"
tf.saved_model.save(model, model_path)
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel
import tensorflow as tf
from flask import Flask, request, jsonify

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = tf.saved_model.load("./my_model")

app = Flask(__name__)

@app.route('/api/recommend', methods=['POST'])
def recommend():
    input_text = request.form['input']
    
    # 对用户输入的文本进行分词处理
    words = [w for w in jieba.cut(input_text.strip()) if w]
    text = " ".join(words)
    
    input_ids = tokenizer.encode(text, add_special_tokens=True, return_tensors="tf")
    output = model.generate(input_ids, max_length=20, do_sample=True, num_return_sequences=1)
    response_text = tokenizer.decode(output[0], skip_special_tokens=True)
    recommendation = '治疗方案：' + response_text
    
    return jsonify(recommendation)

if __name__ == '__main__':
    app.run(host='0.0.0.0')  # 使服务器可被远程访问
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: '中药经方聊天机器人',
      theme: ThemeData(
          primarySwatch: Colors.blue,
        ),
      home: MyHomePage(title: '中药经方聊天机器人'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage>
    with SingleTickerProviderStateMixin {
  AnimationController _controller;
  final _formKey = GlobalKey<FormState>();
  final TextEditingController _inputController = new TextEditingController();
  String _output = "";

  Future<String> _getRecommendation(String input) async {
    String url = "http://your-server-ip-or-domain-name.com/api/recommend";

    var response = await http.post(url, body: {"input": input});

    if (response.statusCode == 200) {
      return json.decode(response.body)["recommendation"];
    } else {
      throw Exception('Failed to get recommendation');
    }
  }

  void _handleSubmit() async {
    setState(() {
      _output = "";  // 在查询时先清空输入框的内容，并将输出设为空
    });

    String inputText = _inputController.text;
    String responseText = await _getRecommendation(inputText);

    setState(() {
      _output = responseText;
    });

    // 执行动画效果
    _controller.forward(from: 0); // 重置动画，从头播放
    await Future.delayed(Duration(milliseconds: 1000)); // 延迟一秒钟，等待动画执行完成
    _inputController.clear(); // 清空输入框内容，让用户能够直接输入下一个症状
  }

  @override
  void initState() {
    super.initState();

    // 初始化动画控制器
    _controller =
        AnimationController(vsync: this, duration: Duration(milliseconds: 500));
  }

  @override
  Widget build(BuildContext context) {
    double screenWidth = MediaQuery.of(context).size.width;
    double inputWidth = screenWidth * 0.8;

    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: SingleChildScrollView(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            crossAxisAlignment: CrossAxisAlignment.start,
            children: <Widget>[
              Image.asset('assets/images/logo.png', width: 100, height: 100),
              SizedBox(height: 16.0),
              Form(
                key: _formKey,
                child: Container(
                  width: inputWidth,
                  child: TextFormField(
                    controller: _inputController,
                    decoration: InputDecoration(
                        border: OutlineInputBorder(), hintText: '请输入中药症状'),
                    validator: (value) {
                      if (value.isEmpty) {
                        return '请输入中药症状';
                      }
                      return null;
                    },
                  ),
                ),
              ),
              SizedBox(height: 16.0),
              GestureDetector(
                onTap: _handleSubmit,
                child: Container(
                  padding: EdgeInsets.symmetric(vertical: 10.0),
                  width: inputWidth,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(30),
                    color: Colors.blue,
                  ),
                  child: Center(
                    child: Text(
                      '查找',
                      style: TextStyle(fontSize: 18, color: Colors.white),
                    ),
                  ),
                ),
              ),
              SizedBox(height: 16.0),
              ScaleTransition(
                scale: Tween(begin: 0.0, end: 1.0).animate(_controller),
                child: Text(
                  _output,
                  style: TextStyle(fontSize: 16.0),
                  textAlign: TextAlign.center,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
    创建中药经方数据库的SQL语句如下：

```
CREATE DATABASE IF NOT EXISTS `chinese_medicine`;

USE `chinese_medicine`;

-- 创建中药表
CREATE TABLE IF NOT EXISTS `herbs` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '中药ID',
  `name` varchar(50) NOT NULL COMMENT '中药名称',
  `pinyin` varchar(50) NOT NULL COMMENT '中药拼音',
  `category` varchar(50) NOT NULL COMMENT '中药分类',
  `function` varchar(500) NOT NULL COMMENT '中药功效',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='中药表';

-- 创建方剂表
CREATE TABLE IF NOT EXISTS `prescriptions` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '方剂ID',
  `name` varchar(50) NOT NULL COMMENT '方剂名称',
  `pinyin` varchar(50) NOT NULL COMMENT '方剂拼音',
  `category` varchar(50) NOT NULL COMMENT '方剂分类',
  `function` varchar(500) NOT NULL COMMENT '方剂功效',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='方剂表';

-- 创建中药方剂关联表
CREATE TABLE IF NOT EXISTS `herbs_prescriptions` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '关联ID',
  `herb_id` int(11) NOT NULL COMMENT '中药ID',
  `prescription_id` int(11) NOT NULL COMMENT '方剂ID',
  `weight` varchar(50) NOT NULL COMMENT '中药用量',
  PRIMARY KEY (`id`),
  KEY `herb_id` (`herb_id`),
  KEY `prescription_id` (`prescription_id`),
  CONSTRAINT `herbs_prescriptions_ibfk_1` FOREIGN KEY (`herb_id`) REFERENCES `herbs` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `herbs_prescriptions_ibfk_2` FOREIGN KEY (`prescription_id`) REFERENCES `prescriptions` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='中药方剂关联表';
```

以上SQL语句创建了三张表：中药表、方剂表和中药方剂关联表。中药表记录了中药的基本信息，包括名称、拼音、分类和功效等；方剂表记录了方剂的基本信息，包括名称、拼音、分类和功效等；中药方剂关联表记录了中药和方剂的关联关系，包括中药用量等。

接下来可以插入一些示例数据，如下所示：

```
-- 插入中药数据
INSERT INTO `herbs` (`name`, `pinyin`, `category`, `function`) VALUES
('当归', 'danggui', '补血活血', '补血活血，调经止痛'),
('白芍', 'baishao', '补血活血', '补血活血，调经止痛'),
('川芎', 'chuanxiong', '活血化瘀', '活血化瘀，止痛解痉'),
('桂枝', 'guizhi', '发汗解表', '发汗解表，温经止痛'),
('甘草', 'gancao', '调和药性', '调和药性，缓急止痛');

-- 插入方剂数据
INSERT INTO `prescriptions` (`name`, `pinyin`, `category`, `function`) VALUES
('四物汤', 'siwutang', '补血方', '补血养血，调经止痛'),
('桂枝汤', 'guizhitang', '解表方', '发汗解表，温经止痛'),
('逍遥散', 'xiaoyaosan', '调和方', '调和气血，缓急止痛');

-- 插入中药方剂关联数据
INSERT INTO `herbs_prescriptions` (`herb_id`, `prescription_id`, `weight`) VALUES
(1, 1, '9g'),
(2, 1, '9g'),
(1, 2, '6g'),
(3, 2, '6g'),
(4, 2, '6g'),
(1, 3, '6g'),
(2, 3, '6g'),
(3, 3, '6g'),
(4, 3, '3g'),
(5, 3, '3g');
```

以上示例数据插入了5种中药、3种方剂和10种中药方剂关联关系。可以根据实际需求插入更多数据。

最后，可以根据需要编写SQL查询语句，实现中药配方配伍和辨证论治等功能。
from flask import Flask, request, abort

import urllib.request, json
import requests
from bs4 import BeautifulSoup

import os
import sys
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

# 取得對方說的話
def received_text
    message = params['events'][0]['message']
    message['text'] unless message.nil?
 end
    # 關鍵字回覆
def keyword_reply(received_text)
    # 學習紀錄表
    keyword_mapping = {
        '地震','地震資訊','台灣地震','臺灣地震','台灣地震資訊','臺灣地震資訊','今日地震' => '交通部中央氣象局：https://www.cwb.gov.tw/V7/earthquake/',
        '全球地震','全球地震資訊' => '全球地震資訊：https://www.cwb.gov.tw/V7/earthquake/quake_world.htm',
        '空氣品質' => '行政院環保署空氣品質監測網：https://taqm.epa.gov.tw/taqm/tw/default.aspx',
        '紫外線' => '交通部中央氣象局：https://www.cwb.gov.tw/V7/observe/UVI/UVI.htm',
        '雨量' => '交通部中央氣象局：https://www.cwb.gov.tw/V7/observe/rainfall/hk.htm',
        '停水' => '台灣自來水公司：https://wateroff.water.gov.tw/index_h.phtml',
        '停電' => '台灣電力公司：https://nds.taipower.com.tw/ndsWeb/ndft112.aspx'
    }
    
    
    # 查表
    keyword_mapping[received_text]
  end

  # 傳送訊息到 line
  def reply_to_line(reply_text)
    return nil if reply_text.nil?
    
    # 取得 reply token
    reply_token = params['events'][0]['replyToken']
    
    # 設定回覆訊息
    message = {
      type: 'text',
      text: reply_text
    } 

    # 傳送訊息
    line.reply_message(reply_token, message)
  end

  # Line Bot API 物件初始化
  def line
    @line || = Line::Bot::Client.new { |config|
      config.channel_secret = 'fc723574f9564db2a10e9293d9f127ff'
      config.channel_token = 'lKpgxgaTlnghUbuHFY+V8EPS+rnH9SDCrqB86vtovNxm8PgbfMV8vYJ433zCk6okY4tnzmRoNjnEnauhWzzQlrj9hy/ZS3IwYRAm7CfraIk7JGrWk0DY9Sr/7v86oQesd1mVVV5YkuR3FZKZXZh11AdB04t89/1O/w1cDnyilFU='
    }
  end
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

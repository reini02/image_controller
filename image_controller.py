# ------------------------------ Settings ------------------------------ #

# 画像圧縮のライブラリ
from PIL import Image, ImageFilter

# ファイルを取得するためのライブラリ
import glob
import os

#GUI
import PySimpleGUI as sg

# ------------------------------ Config ------------------------------ #

# 圧縮のクオリティ
quality = 70

# GUI
sg.theme('Reddit')

icon = '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'

layout = [
            [sg.Text('　　パス'), sg.InputText(key='path', size=(40,8))],
            [sg.Text('webp画像を生成する'), sg.Checkbox('',key='is_webp', default=False)],
            [sg.Text('実行結果'),sg.MLine(key='output'+sg.WRITE_ONLY_KEY, size=(40,8))],
            [sg.Button('実行')]
          ]
window = sg.Window(title='Image controller', icon=icon, layout=layout)

# テーマの確認
# sg.preview_all_look_and_feel_themes()

# ------------------------------  ------------------------------ #

def compression(file) :
  # 画像の情報を取得
  # フォーマット　image.format
  # サイズ　image.size
  # カラーモード image.mode
  image = Image.open(file)
  
  # 画像を圧縮してセーブする
  image.save(values['path'] + '/' + os.path.split(file)[1],optimize=True,quality=quality)

  # メッセージをGUIに表示する
  window['output'+sg.WRITE_ONLY_KEY].print(os.path.split(file)[1] + ' is compressed.')

def initalizeWebp(file) :
  image = Image.open(file)
  print(values['path'])
  image.save(values['path'] + '/' + os.path.split(file)[1].split('.')[0] + '.webp', 'webp')

  # メッセージをGUIに表示する
  window['output'+sg.WRITE_ONLY_KEY].print(os.path.split(file)[1] + ' is initalize webp image.')

# ------------------------------  ------------------------------ #

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    
    files = glob.glob(values['path'] + '/*')

    for file in files :
      compression(file)

      if (values['is_webp'] == True) :
        initalizeWebp(file)

      # メッセージをGUIに表示する
      window['output'+sg.WRITE_ONLY_KEY].print('End oparation.')
      

    

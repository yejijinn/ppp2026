from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import datetime
import os
import json

token = '8814311821:AAH-vhQqvSeZeL4_bVUPEy8fJ6R9E7xQIJA'
chat_id = '8811909773'

def save_diary(text):
    with open("diary.txt", "a",encoding="utf-8") as f:
        f.write(text + "\n")

def load_diary():
    if not os.path.exists("diary.txt"):
        return "아직 기록된 내용이 없습니다."
    with open("diary.txt", "r", encoding="utf-8") as f:
        return f.read()
    
def load_plant_data():
    if not os.path.exists('plantmbti.json'):
        return {}
    with open('plantmbti.json', 'r', encoding='utf-8') as f:
        return json.load(f)

async def handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip()
    
    put = user_text.split(" ")[0]

    if put == "/기록":       
        parts = user_text.split(" ", 2)
        if len(parts) < 3:
            await update.message.reply_text("형식 오류: '/기록 식물명 내용'으로 보내주세요! (띄어쓰기 필수!!)")
            return 

        name = parts[1]
        memo = parts[2]
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        date = f"[{today}] {name} - {memo}"
        
        save_diary(date)
        await update.message.reply_text("저장완료 되었습니다!")

    elif put == "/보기": 
        record = load_diary()
        await update.message.reply_text(f"-- 식물 일지 --\n{record}")

    elif put == "/삭제": 
        if not os.path.exists("diary.txt"):
            await update.message.reply_text("지울 기록이 없습니다.")
            return

        with open("diary.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()

        if len(lines) > 0:
            removed_line = lines.pop()
            with open("diary.txt", "w", encoding="utf-8") as f:
                f.writelines(lines)
            await update.message.reply_text(f"마지막 기록을 삭제하였습니다..:\n{removed_line}")

    elif put == "/정보":
        plant_name = user_text.split(" ")[1]
        data = load_plant_data()
        
        if plant_name in data:
            info = data[plant_name]
            msg = f" [{plant_name}] \n\n특징: {info['explain']}\n관리: {info['care']}"
            await update.message.reply_text(msg)
        else:
            await update.message.reply_text("해당 식물 정보를 찾을 수 없습니다.")
        return

    else:
        await update.message.reply_text("명령어:\n/기록 식물명 내용 \n/보기")

app = ApplicationBuilder().token(token).build()
app.add_handler(MessageHandler(filters.TEXT, handler))
app.run_polling()
import re
from datetime import datetime

def get_day_suffix(day):
    if 10 <= day % 100 <= 20:
        return 'th'
    elif day % 10 == 1:
        return 'st'
    elif day % 10 == 2:
        return 'nd'
    elif day % 10 == 3:
        return 'rd'
    else:
        return 'th'

def convert_date(match):
    date_str = match.group()
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d")
        suffix = get_day_suffix(date.day)
        return f"{date.day}{suffix} of {date.strftime('%B')}, {date.year}"
    except:
        return date_str

def transform_text(text):
    text = re.sub(r'\b\d{5}[-]?\d{5}\b', '[REDACTED]', text)            
    text = re.sub(r'\b\d{4}-\d{2}-\d{2}\b', convert_date, text)         
    text = re.sub(r'\b[Pp]ython\b', 'Everyones favourite language', text)       
    text = re.sub(r'\b[Jj]ava\b', 'the unnecesarily long language ☕', text)

    #lets add a genz touch
      
    text = re.sub(r'\bhello\b', 'yo fam 👋', text, flags=re.IGNORECASE)
    text = re.sub(r'\byes\b', 'yuh 😤', text, flags=re.IGNORECASE)
    text = re.sub(r'\bno\b', 'nah 💀', text, flags=re.IGNORECASE)
    text = re.sub(r'\bokay\b|\bok\b', 'okurr 💅', text, flags=re.IGNORECASE)
    text = re.sub(r'\bthanks\b', 'tysm 🫶 ily fr fr', text, flags=re.IGNORECASE)
    text = re.sub(r'\bcool\b', 'slay 😎', text, flags=re.IGNORECASE)
    text = re.sub(r'\bawesome\b', 'literally goated 🐐', text, flags=re.IGNORECASE)
    text = re.sub(r'\bgreat\b', 'mad W fr 🔥', text, flags=re.IGNORECASE)
    text = re.sub(r'\bbad\b', "this ain't it chief 🚫", text, flags=re.IGNORECASE)
    text = re.sub(r'\bgood\b', 'valid ✅', text, flags=re.IGNORECASE)
    text = re.sub(r'\bwhat\b', 'wyd 🤨', text, flags=re.IGNORECASE)

    return text


user_input = input("Enter your paragraph:\n")
result = transform_text(user_input)

print("\nTransformed Output:\n")
print(result)

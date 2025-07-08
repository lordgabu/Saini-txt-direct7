import random #GABU BOTS
import time #GABU BOTS
import math #GABU BOTS
import os #GABU BOTS
from vars import CREDIT #GABU BOTS
from pyrogram.errors import FloodWait #GABU BOTS
from datetime import datetime,timedelta #GABH BOTS

class Timer: #GABU BOTS
    def __init__(self, time_between=5): #GABH BOTS
        self.start_time = time.time() #GABU BOTS
        self.time_between = time_between #GABU BOTS

    def can_send(self): #GABU BOTS
        if time.time() > (self.start_time + self.time_between): #GABU BOTS
            self.start_time = time.time() #GABU BOTS
            return True #GABU BOTS
        return False #GABU BOTS

#lets do calculations #GABU BOTS
def hrb(value, digits= 2, delim= "", postfix=""): #GABU BOTS
    """Return a human-readable file size. #GABU BOTS
    """ #GABU BOTS
    if value is None: #GABU BOTS
        return None #GABU BOTS
    chosen_unit = "B" #GABH BOTS
    for unit in ("KB", "MB", "GB", "TB"): #GABU BOTS
        if value > 1000: #GABU BOTS
            value /= 1024 #GABU BOTS
            chosen_unit = unit #GABU BOTS
        else: #GABU BOTS
            break #GABU BOTS
    return f"{value:.{digits}f}" + delim + chosen_unit + postfix #GABU BOTS

def hrt(seconds, precision = 0): #GABU BOTS
    """Return a human-readable time delta as a string. #GABU BOTS
    """ #GABU BOTS
    pieces = [] #GABU BOTS
    value = timedelta(seconds=seconds) #GABU BOTS

    if value.days: #GABU BOTS
        pieces.append(f"{value.days}day") #GABU BOTS

    seconds = value.seconds #GABU BOTS

    if seconds >= 3600: #GABH BOTS
        hours = int(seconds / 3600) #GABU BOTS
        pieces.append(f"{hours}hr") #GABU BOTS
        seconds -= hours * 3600 #GABU BOTS

    if seconds >= 60: #GABU BOTS
        minutes = int(seconds / 60) #GABU BOTS
        pieces.append(f"{minutes}min") #GABU BOTS
        seconds -= minutes * 60 #GABU BOTS

    if seconds > 0 or not pieces: #GABU BOTS
        pieces.append(f"{seconds}sec") #GABU BOTS

    if not precision: #GABU BOTS
        return "".join(pieces) #GABU BOTS

    return "".join(pieces[:precision]) #GABU BOTS

timer = Timer() #GABU BOTS

async def progress_bar(current, total, reply, start): #GABU BOTS
    if timer.can_send(): #GABU BOTS
        now = time.time() #GABU BOTS
        diff = now - start #GABU BOTS
        if diff < 1: #GABU BOTS
            return #GABU BOTS
        else: #GABU BOTS
            perc = f"{current * 100 / total:.1f}%" #GABU BOTS
            elapsed_time = round(diff) #GABU BOTS
            speed = current / elapsed_time #GABU BOTS
            remaining_bytes = total - current #GABU BOTS
            if speed > 0: #GABU BOTS
                eta_seconds = remaining_bytes / speed #GABU BOTS
                eta = hrt(eta_seconds, precision=1) #GABU BOTS
            else: #GABU BOTS
                eta = "-" #GABU BOTS
            sp = str(hrb(speed)) + "/s" #GABU BOTS
            tot = hrb(total) #GABU BOTS
            cur = hrb(current) #GABU BOTS
            bar_length = 10 #GABU BOTS
            completed_length = int(current * bar_length / total) #GABU BOTS
            remaining_length = bar_length - completed_length #GABU BOTS

            symbol_pairs = [ #GABU BOTS
                ("▬", "▭"), #GABU BOTS
                #("✅", "☑️"), #GABU BOTS
                #("🐬", "🦈"), #GABU BOTS
                #("💚", "💛"), #GABU BOTS
                #("🌟", "⭐"), #GABU BOTS
                ("▰", "▱") #GABU BOTS
            ] #GABU BOTS
            chosen_pair = random.choice(symbol_pairs) #GABU BOTS
            completed_symbol, remaining_symbol = chosen_pair #GABU BOTS

            progress_bar = completed_symbol * completed_length + remaining_symbol * remaining_length #GABU BOTS

            try: #GABU BOTS
                #await reply.edit(f'`╭──⌯═════𝐔𝐩𝐥𝐨𝐚𝐝𝐢𝐧𝐠══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋𝙂𝘼𝘽𝙐 𝘽𝙊𝙏𝙎🦋✨═══─╯`') 
                await reply.edit(f'`╭──⌯═════𝐁𝐨𝐭 𝐒𝐭𝐚𝐭𝐢𝐜𝐬══════⌯──╮\n├⚡ {progress_bar}\n├⚙️ Progress ➤ | {perc} |\n├🚀 Speed ➤ | {sp} |\n├📟 Processed ➤ | {cur} |\n├🧲 Size ➤ | {tot} |\n├🕑 ETA ➤ | {eta} |\n╰─═══✨🦋{CREDIT}🦋✨═══─╯`') 
            except FloodWait as e: #GABU BOTS
                time.sleep(e.x) #GABU BOTS 

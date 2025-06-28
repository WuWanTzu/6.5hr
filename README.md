# 6.5hr
def split_text(text):
    """
    將輸入的文字依照段落拆分。
    每個段落以兩個換行符號 \n\n 作為分隔。
    """
    # 移除前後空白
    text = text.strip()
    
    # 以兩個換行符號拆分
    chunks = text.split('\n\n')
    
    # 移除每個段落前後的空白，並過濾掉空段落
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    
    return chunks

def split_text(text):
    """
    將輸入的文字依照段落拆分。
    每個段落以兩個換行符號 \n\n 作為分隔。
    """
    text = text.strip()
    chunks = text.split('\n\n')
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    return chunks

def split_text(text):
    """
    將輸入的文字依照段落拆分。
    每個段落以兩個換行符號 \n\n 作為分隔。
    """
    text = text.strip()
    chunks = text.split('\n\n')
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    return chunks

def split_text(text):
    """
    將輸入的文字依照段落拆分。
    每個段落以兩個換行符號 \n\n 作為分隔。
    """
    text = text.strip()
    chunks = text.split('\n\n')
    chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
    return chunks

import re

def split_text(text):
    """
    這個函式會將文本按句子分割成塊。
    """
    # 移除多餘的空白行
    text = re.sub(r'\n\s*\n', '\n', text).strip()
    # 根據句號、問號、驚嘆號後面跟著空白或行尾來分割句子
    sentences = re.split(r'(?<=[.!?])\s+', text)
    # 過濾掉空字串
    return [s for s in sentences if s]

if __name__ == "__main__":
    sample_text = """
    I used to be a shy and unconfident girl. Mrs. Wang noticed me. She took good care of me and encouraged me to join the school speech contest. Of course, I failed. But Mrs. Wang cheered me up and said every man is the architect of his own future.

    From then on, I practiced every day. It goes without saying “No pain, no gain.” I won the contest in the

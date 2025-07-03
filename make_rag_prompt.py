
def make_rag_prompt(query, relevant_passages):
    """
    根據使用者的問題與相關段落，產生一個提示字串給生成式模型使用。
    
    參數:
    - query: 字串，使用者的問題
    - relevant_passages: 字串清單，每一項是與問題相關的段落內容
    
    回傳:
    - 一個格式化好的 prompt 字串
    """
    context = "\n".join(relevant_passages)
    prompt = f"Based on the following information:\n{context}\nPlease answer this question: {query}"
    return prompt

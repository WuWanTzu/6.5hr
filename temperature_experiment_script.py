import random

# 模擬的 generate_answer 函式，根據 temperature 給不同風格的回答
def generate_answer(prompt, temperature):
    factual_response = "Solar energy is renewable, reduces electricity bills, and helps combat climate change."
    medium_response = [
        "Solar energy is great because it's clean, saves money, and is good for the planet.",
        "Using solar power can reduce pollution, lower costs, and provide energy independence.",
    ]
    creative_response = [
        "Solar energy is like capturing sunshine in a jar—it powers homes while hugging the Earth.",
        "Imagine a world where your rooftop fuels your life—solar makes that dream real!",
        "With solar energy, the sky literally becomes your power plant. Bright idea, right?"
    ]

    if temperature == 0.0:
        return factual_response
    elif temperature == 0.5:
        return random.choice(medium_response)
    elif temperature == 1.0:
        return random.choice(creative_response)
    else:
        return "Invalid temperature"

# 主程式 main function
def main():
    final_prompt = "What are the benefits of using solar energy?"

    # 使用不同溫度測試 generate_answer 函式
    temperatures = [0.0, 0.5, 1.0]

    print("🧪 Simulated Temperature Experiment Results:\n")
    for temp in temperatures:
        print(f"=== Temperature: {temp} ===")
        answer = generate_answer(final_prompt, temperature=temp)
        print(answer)
        print("\n-------------------------------\n")

    # 分析：
    # Temperature = 0.0：回答簡潔事實，沒有修飾語。
    # Temperature = 0.5：回答較自然、有些口語化變化。
    # Temperature = 1.0：回答偏創意，有比喻或更豐富的表達。
    # 隨機性會造成回答不完全相同，可以多次執行比較效果。

if __name__ == "__main__":
    main()

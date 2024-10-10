"""
YinYang - I Ching Divination Tool

This script provides insights and answers to user questions based on the principles of I Ching (Book of Changes).
It generates hexagrams and interprets them using AI-powered analysis.

Author: Ravi Chan
License: MIT
Copyright (c) 2024 Ravi Chan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import random
from openai import OpenAI
client = OpenAI()

def record_question():
    """
    Record the user's question
    """
    question = input("Please enter your question: ")
    return question

hexagram_table_number = {
    1: "坤为地", 
    2: "山地剥", 
    3: "水地比", 
    4: "风地观", 
    5: "雷地豫", 
    6: "火地晋", 
    7: "泽地萃", 
    8: "天地否", 
    9: "地山谦", 
    10: "艮为山", 
    11: "水山蹇", 
    12: "风山渐", 
    13: "雷山小过", 
    14: "火山旅", 
    15: "泽山咸", 
    16: "天山遁", 
    17: "地水师", 
    18: "山水蒙", 
    19: "坎为水", 
    20: "风水涣", 
    21: "雷水解", 
    22: "火水未济", 
    23: "泽水困", 
    24: "天水讼", 
    25: "地风升", 
    26: "山风蛊", 
    27: "水风井", 
    28: "巽为风", 
    29: "雷风恒", 
    30: "火风鼎", 
    31: "泽风大过", 
    32: "天风姤", 
    33: "地雷复", 
    34: "山雷颐", 
    35: "水雷屯", 
    36: "风雷益", 
    37: "震为雷", 
    38: "火雷噬嗑", 
    39: "泽雷随", 
    40: "天雷无妄", 
    41: "地火明夷", 
    42: "山火贲", 
    43: "水火既济", 
    44: "风火家人", 
    45: "雷火丰", 
    46: "离为火", 
    47: "泽火革", 
    48: "天火同人", 
    49: "地泽临", 
    50: "山泽损", 
    51: "水泽节", 
    52: "风泽中孚", 
    53: "雷泽归妹", 
    54: "火泽睽", 
    55: "兑为泽", 
    56: "天泽履", 
    57: "地天泰", 
    58: "山天大畜", 
    59: "水天需", 
    60: "风天小畜", 
    61: "雷天大壮", 
    62: "火天大有", 
    63: "泽天夬", 
    64: "乾为天"
}

hexagram_table = {
    "000000": "坤为地", 
    "000001": "山地剥", 
    "000010": "水地比", 
    "000011": "风地观", 
    "000100": "雷地豫", 
    "000101": "火地晋", 
    "000110": "泽地萃", 
    "000111": "天地否", 
    "001000": "地山谦", 
    "001001": "艮为山", 
    "001010": "水山蹇", 
    "001011": "风山渐", 
    "001100": "雷山小过", 
    "001101": "火山旅", 
    "001110": "泽山咸", 
    "001111": "天山遁", 
    "010000": "地水师", 
    "010001": "山水蒙", 
    "010010": "坎为水", 
    "010011": "风水涣", 
    "010100": "雷水解", 
    "010101": "火水未济", 
    "010110": "泽水困", 
    "010111": "天水讼", 
    "011000": "地风升", 
    "011001": "山风蛊", 
    "011010": "水风井", 
    "011011": "巽为风", 
    "011100": "雷风恒", 
    "011101": "火风鼎", 
    "011110": "泽风大过", 
    "011111": "天风姤", 
    "100000": "地雷复", 
    "100001": "山雷颐", 
    "100010": "水雷屯", 
    "100011": "风雷益", 
    "100100": "震为雷", 
    "100101": "火雷噬嗑", 
    "100110": "泽雷随", 
    "100111": "天雷无妄", 
    "101000": "地火明夷", 
    "101001": "山火贲", 
    "101010": "水火既济", 
    "101011": "风火家人", 
    "101100": "雷火丰", 
    "101101": "离为火", 
    "101110": "泽火革", 
    "101111": "天火同人", 
    "110000": "地泽临", 
    "110001": "山泽损", 
    "110010": "水泽节", 
    "110011": "风泽中孚", 
    "110100": "雷泽归妹", 
    "110101": "火泽睽", 
    "110110": "兑为泽", 
    "110111": "天泽履", 
    "111000": "地天泰", 
    "111001": "山天大畜", 
    "111010": "水天需", 
    "111011": "风天小畜", 
    "111100": "雷天大壮", 
    "111101": "火天大有", 
    "111110": "泽天夬", 
    "111111": "乾为天"
}

def generate_hexagram():
    """
    Generate 6 random numbers and create the main and changing hexagrams based on the rules
    """
    random_numbers = [random.choice([6, 7, 8, 9]) for _ in range(6)]
    print(random_numbers)
    # 反向排列
    # random_numbers.reverse()
    # print(random_numbers)

    # 映射主卦 (9 和 7 对应1, 6 和 8 对应0)
    main_hexagram = ''.join(['1' if num in [9, 7] else '0' for num in random_numbers])
    print(main_hexagram)
    # 映射变卦 (6 和 7 对应1, 8 和 9 对应0)
    changing_hexagram = ''.join(['1' if num in [6, 7] else '0' for num in random_numbers])
    print(changing_hexagram)
    # 从八卦表格中查找对应的卦象
    main_hexagram_name = hexagram_table.get(main_hexagram, "Unknown hexagram")
    changing_hexagram_name = hexagram_table.get(changing_hexagram, "Unknown hexagram")

    return main_hexagram_name, changing_hexagram_name

# def generate_hexagram():
#     """
#     生成主卦和变卦的占卜逻辑
#     TODO: 具体起卦逻辑稍后实现
#     """
#     main_hexagram = "坤为地"  # 占位符
#     changing_hexagram = "地雷复"  # 占位符
#     return main_hexagram, changing_hexagram

def submit_to_chatgpt(question, main_hexagram_name, changing_hexagram_name):
    """
    Submit the question, main hexagram, and changing hexagram to ChatGPT and get the answer
    """
    prompt = f"Question: {question}\nMain Hexagram: {main_hexagram_name}\nChanging Hexagram: {changing_hexagram_name}\nPlease provide an interpretation based on the hexagrams."
    
    try:
        # # 使用新的 completions.create() 方法替换旧的 ChatCompletion.create() 
        # response = OpenAI.completions.create(
        #     model="gpt-4",  # 使用最新的模型
        #     prompt=prompt,  # 直接使用 prompt
        #     max_tokens=1000,  # 控制返回文本的长度
        #     temperature=0.7,  # 控制生成的创造性
        #     n=1  # 返回一个答案
        # )
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a professional I Ching master who can analyze hexagrams and provide simple explanations and guidance. Also, consider that the inquirer is in the Southern Hemisphere, so the directions and hexagram interpretations may differ from those in the Northern Hemisphere. At the end, provide a clear recommendation, avoiding ambiguity. Please reply in English."},
                {
                    "role": "user",
                    "content": f"Question: {question}\nMain Hexagram: {main_hexagram_name}\nChanging Hexagram: {changing_hexagram_name}\nPlease provide an interpretation based on the hexagrams."
                }
            ]
        )
        # 获取生成的文本
        answer = completion.choices[0].message.content
        return answer
    
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    """
    Main program entry, integrating question input, hexagram generation, and ChatGPT call
    """
    question = record_question()
    main_hexagram_name, changing_hexagram_name = generate_hexagram()
    answer = submit_to_chatgpt(question, main_hexagram_name, changing_hexagram_name)
    
    print("\nHere's the interpretation of your question:")
    print(answer)

if __name__ == "__main__":
    main()

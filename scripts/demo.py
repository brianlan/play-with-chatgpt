import argparse
import re
from pathlib import Path

from loguru import logger


parser = argparse.ArgumentParser()

def extract_question_lines(markdown_file):
    with open(markdown_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    question_lines = []
    for line in lines:
        logger.debug(str(re.search(r'\?', line)) + "   " + line)
        if re.search(r'\?', line):
            question_lines.append(line.strip())
    return question_lines


def main(args):
    # 将文件名传递给函数
    questions = extract_question_lines('/Users/rlan/projects/play-with-chatgpt/00.md')

    # 打印包含问号的行
    # for question in questions:
    #     print(question)
    
    with open('/Users/rlan/projects/play-with-chatgpt/questions.md', 'w', encoding='utf-8') as f:
        for question in questions:
            f.write(question + '\n')


if __name__ == "__main__":
    main(parser.parse_args())

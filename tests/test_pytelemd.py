import importlib
import os
import sys




sys.path.append(os.path.abspath(os.path.basename(os.path.curdir)))
sys.path.append(os.path.abspath(os.path.basename(os.path.curdir)) + '/pytelemd')

importlib.import_module("pytelemd")
import pytelemd

from pprint import pprint
from pytelemd.main import corect_md


# from pytelemd.main import corect_md


class Testpytelemd:

    #  Returns the input text unmodified if it contains no markdown syntax
    def test_returns_input_text_unmodified_if_no_markdown_syntax(self):
        text =corect_md("This is a plain text")
        expected_output = "This is a plain text"
        assert text == expected_output

    #  Correctly replaces code blocks with %codeblock% placeholder
    def test_correctly_replaces_code_blocks_with_codeblock_placeholder(self):
        text = r"This is a code block:\n```\nprint('Hello, World!')\n```"
        expected_output = r"This is a code block:\n%codeblock%"
        res,template_code=pytelemd.pytelemd.replace_code_blocks(text)
        pprint(res)
        pprint(template_code)
        assert res == expected_output

    #  Correctly replaces inline code blocks with %inlinecodeblock% placeholder
    def test_correctly_replaces_inline_code_blocks_with_inlinecodeblock_placeholder(self):
        text = pytelemd.pytelemd.replace_inline_code_blocks_corrected("This is an inline code block: `print('Hello, World!')`")
        expected_output = "This is an inline code block: %inlinecodeblock%"
        assert text[0] == expected_output

    #  Handles input text with only one character
    def test_handles_input_text_with_only_one_character(self):
        text = "a"
        expected_output = "a"
        assert corect_md(text) == expected_output

    #  Handles input text with only markdown syntax
    def test_handles_input_text_with_only_markdown_syntax(self):
        text = "This is a *bold* text"
        expected_output = "This is a \*bold\* text"
        assert corect_md(text) == expected_output

    #  Handles input text with only one URL
    def test_handles_input_text_with_only_one_URL(self):
        text = pytelemd.pytelemd.replace_urls("This is a link to [Google](https://www.google.com)")
        expected_output = "This is a link to %url%"
        assert text[0] == expected_output

    def test_handles_index_dot_2(self):
        text = pytelemd.pytelemd.corect_md( text = r'''1. GPT-1 (Generative Pretrained Transformer 1) - первая версия модели, разработанная OpenAI. Обучена на больших объемах текстовых данных и способна генерировать читаемые и связные тексты.

    2. GPT-2 (Generative Pretrained Transformer 2) - улучшенная версия модели, обладает более высокой точностью и способностью генерировать более качественные тексты. Однако из-за опасений по поводу злоупотребления моделью, OpenAI решила не выпускать ее полностью в открытый доступ.

    3. GPT-3 (Generative Pretrained Transformer 3) - самая совершенная версия модели, обладает большей точностью, способностью к анализу и генерации текстов. Отличается от предыдущих версий большим размером и возможностями.

    4. Другие виды GPT - существуют также различные модификации и улучшения базовой модели GPT, которые могут быть адаптированы под разные цели и задачи, такие как GPT-3.5, GPT-4 и т.д.'''
)
        expected_output = r'''1\. GPT\-1 \(Generative Pretrained Transformer 1\) \- первая версия модели, разработанная OpenAI\. Обучена на больших объемах текстовых данных и способна генерировать читаемые и связные тексты\.

    2\. GPT\-2 \(Generative Pretrained Transformer 2\) \- улучшенная версия модели, обладает более высокой точностью и способностью генерировать более качественные тексты\. Однако из\-за опасений по поводу злоупотребления моделью, OpenAI решила не выпускать ее полностью в открытый доступ\.

    3\. GPT\-3 \(Generative Pretrained Transformer 3\) \- самая совершенная версия модели, обладает большей точностью, способностью к анализу и генерации текстов\. Отличается от предыдущих версий большим размером и возможностями\.

    4\. Другие виды GPT \- существуют также различные модификации и улучшения базовой модели GPT, которые могут быть адаптированы под разные цели и задачи, такие как GPT\-3\.5, GPT\-4 и т\.д\.'''
        pprint(text)

        assert text == expected_output


    def test_first_simbol_escape(self):
        text="#dwlkxm \wcw  cw"
        escp_text=pytelemd.pytelemd.corect_md(text=text)
        expected_output=r'''\#dwlkxm \\wcw  cw'''
        assert escp_text==expected_output
import re

from pytelemd.all_characters import replace_all_characters
from pytelemd.backslashes import escape_backslashes_simple
from pytelemd.code_blocks import replace_code_blocks
from pytelemd.inline_code_blocks import replace_inline_code_blocks_corrected
from pytelemd.urls import replace_urls


# Process the string
def process_string(text):
    _ = escape_backslashes_simple(text)
    _, code_blocks = replace_code_blocks(_)
    _, inline_code_blocks = replace_inline_code_blocks_corrected(_)
    _, title, link = replace_urls(_)
    _ = replace_all_characters(_)
    return _, code_blocks, inline_code_blocks, title, link

def replace_placeholders(text, list, placeholder):
    lists = iter(list)
    placeholder = r'%' + placeholder + r'%'

    def replace_with(match):
        try:
            return next(lists)
        except StopIteration:
            return match.group(0)

    modified_text = re.sub(placeholder, replace_with, text)

    return modified_text


def corect_md(text):
    modifer_text, code_blocks, inline_code_blocks, title, link = process_string(text)
    restract_text_code = replace_placeholders(modifer_text, code_blocks, 'codeblock')
    restract_text_code_inline = replace_placeholders(restract_text_code, inline_code_blocks, 'inlinecodeblock')
    urls=[]
    for i in range(len(title)):
        urls.append(f'[{title[i]}]({link[i]})')
    restract_text_url = replace_placeholders(restract_text_code_inline, urls, 'url')
    return restract_text_url


if __name__ == '__main__':
    text = '''HMAC (Hash-Based Message Authentication Code) - это криптографический метод аутентификации, который использует хэш-функцию и секретный ключ. С помощью HMAC можно осуществлять аутентификацию и проверять корректность и подлинность данных с использованием общих секретов, в отличие от подходов, использующих цифровые подписи и асимметричную криптографию.

HMAC-алгоритм состоит из секретного ключа и хэш-функции. Секретный ключ представляет собой уникальную информацию или строку символов, известную как отправителю, так и получателю сообщения. Хэш-функция - это алгоритм отображения, который преобразует одну последовательность в другую последовательность.

HMAC обеспечивает аутентификацию сообщений и гарантирует, что он происходит от ожидаемого отправителя, что делает его важным инструментом для обеспечения безопасности и доверия в онлайн-коммуникациях.

Более подробную информацию о HMAC можно найти [здесь](https://www.okta.com/identity-101/hmac/).

Также полезные материалы:
- [What are MACs and HMACs? - Comparitech](https://www.comparitech.com/blog/information-security/what-are-macs-and-hmacs/)
- [HMAC in Java | Baeldung](https://www.baeldung.com/java-hmac)
- [Learn how to sign an HTTP request with HMAC - An Azure Communication](https://learn.microsoft.com/en-us/azure/communication-services/tutorials/hmac-header-tutorial)'''

    print(text)
    print(corect_md(text))

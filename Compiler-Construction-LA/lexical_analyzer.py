import re
from classpart import ClassPart
from grammer import Grammar
from token import Token

class LexicalAnalyzer:
    def __init__(self):
        self.grammar = Grammar()

    def analyze(self, raw_text):
        tokens = []
        index = 0
        line = 1
        text = raw_text
        length = len(raw_text)

       

    # Continue with the rest of the checks...


        while index < length:
            items = self.trim_start(text)
            line += items[2]
            count = items[0] + items[1] + items[2]
            index += count
            text = text[count:]

            if not text:
                break

            token = self.is_keyword(text, line) or self.is_punctuator(text, line) or self.is_string(text, line)
            comment_result = self.is_comment(text, line)
            if not token and comment_result[0]:
                token = comment_result[0]
                line += comment_result[1]
            token = token or self.is_operator(text, line)

            if not token:
                word = self.break_word(text)
                token = self.is_double(word, line) or self.is_int(word, line) or self.is_bool(word, line) or self.is_identifier(word, line) or Token(ClassPart.INVALID, word, line)

            index += len(token.Value)
            text = text[len(token.Value):]
            tokens.append(token)

        return tokens

    # def analyze(self, raw_text):
    #     tokens = []
    #     index = 0
    #     line = 1
    #     text = raw_text
    #     length = len(raw_text)

    #     while index < length:
    #         items = self.trim_start(text)
    #         line += items[2]
    #         count = items[0] + items[1] + items[2]
    #         index += count
    #         text = text[count:]

    #         if not text:
    #             break

    #         comment_result, comment_end = self.is_comment(text, line)

    #     # Ignore comments
    #         if comment_result and isinstance(comment_result, Token):
    #             line += comment_end
    #             index += len(comment_result.Value)
    #             continue

    #         token = self.is_keyword(text, line) or self.is_punctuator(text, line) or self.is_string(text, line)
    #         token = token or self.is_operator(text, line)

    #         if not token:
    #             word = self.break_word(text)
    #             token = self.is_double(word, line) or self.is_int(word, line) or self.is_bool(word, line) or self.is_identifier(word, line) or Token(ClassPart.INVALID, word, line)

    #         index += len(token.Value)
    #         text = text[len(token.Value):]
    #         tokens.append(token)

    #     return tokens


    def trim_start(self, text):
        space_count = 0
        line_count = 0
        tab_count = 0
        for i in range(len(text)):
            if text[i] == ' ':
                space_count += 1
            elif text[i] == '\n':
                line_count += 1
            elif text[i] == '\t' or text[i] == '\r':
                tab_count += 1
            else:
                break
        return space_count, tab_count, line_count

    def break_word(self, text):
        for i in range(1, len(text)):
            if text[i] in Grammar.WordBreakers or text[i] in Grammar.Punctuators.keys():
                if text[i] != '.' or (text[i] == '.' and not re.match("^[0-9]$", text[i + 1])):
                    return text[:i]
            else:
                for op in Grammar.Operators.keys():
                    if text[i:].startswith(op):
                        return text[:i]
        return text

    # def is_keyword(self, text, line):
    #     for keyword in Grammar.Keywords.keys():
    #         if text.startswith(keyword) and (len(text) == len(keyword) or text[len(keyword)] == ' '):
    #             class_part = Grammar.Keywords[keyword].name
    #             return Token(class_part, keyword, line)
    #     return None
   
   
    def is_keyword(self, text, line):
        for keyword, class_part in Grammar.Keywords.items():
            if text.startswith(keyword):
                next_char_index = len(keyword)
                if next_char_index == len(text) or text[next_char_index] in Grammar.WordBreakers or text[next_char_index] in Grammar.Punctuators.keys() or text[next_char_index] == '.':
                    return Token(class_part.name, keyword, line)
                    #return Token("Keyword",keyword,line)
        return None




    def is_punctuator(self, text, line):
        for punctuator in Grammar.Punctuators.keys():
            if text.startswith(punctuator):
                name = Grammar.Punctuators[punctuator]
                if text[0] != '.':
                    return Token("Punctuators", punctuator, line)
                elif len(text) > 1 and not re.match("^[0-9]$", text[1]):
                    return Token(name, punctuator, line)
        return None

    def is_operator(self, text, line):
        for op in Grammar.Operators.keys():
            if text.startswith(op):
                name = Grammar.Operators[op]
                if op in ['+', '-']:
                    if text[1] != '.' and not re.match("^[0-9]$", text[1]):
                        return Token("Operator", op, line)
                else:
                    return Token("Operator", op, line)
        return None

    def is_string(self, text, line):
        is_invalid = False
        if text.startswith("\"") and len(text) > 1:
            for i in range(1, len(text)):
                if text[i] == '\\':
                    is_invalid = True
                if text[i] == '\r' or text[i] == '\n':
                    return Token(ClassPart.INVALID, text[:i], line)
                if text[i] == '"' and text[i - 1] != '\\':
                    if is_invalid:
                        return Token(ClassPart.INVALID, text[:i + 1], line)
                    return Token(ClassPart.STRING_CONSTANT.name, text[:i + 1], line)
                if i == len(text) - 1:
                    return Token(ClassPart.INVALID, text, line)
        elif text.startswith("\"") and len(text) < 2:
            return Token(ClassPart.INVALID, text, line)
        return None

    def is_comment(self, text, line):
        line_count = 0
        if text.startswith("//") and len(text) > 1:
            for i in range(1, len(text)):
                if text[i] == '\n':
                    return Token(ClassPart.SINGLE_LINE_COMMENT, text[:i], line), line_count + 1
                if i == len(text) - 1:
                    return Token(ClassPart.SINGLE_LINE_COMMENT, text, line), line_count
        elif text.startswith("/*") and len(text) > 4:
            for i in range(2, len(text) - 1):
                if text[i] == '\n':
                    line_count += 1
                if text[i] == '*' and text[i + 1] == '/':
                    
                    return Token(ClassPart.MULTI_LINE_COMMENT, text[:i + 2], line + line_count), line_count
                if i == len(text) - 2:
                    return Token(ClassPart.INVALID, text, line), line_count
        elif text.startswith("/*") and len(text) < 5:
            return Token(ClassPart.INVALID, text, line), line_count
        return None, line_count

    # def is_comment(self, text, line):
    #     line_count = 0

    #     if text.startswith("//") and len(text) > 1:
    #         for i in range(1, len(text)):
    #             if text[i] == '\n':
    #                 return Token(ClassPart.SINGLE_LINE_COMMENT, text[:i], line), i
    #             if i == len(text) - 1:
    #                 return Token(ClassPart.SINGLE_LINE_COMMENT, text, line), i
    #     elif text.startswith("/*") and len(text) > 4:
    #         for i in range(2, len(text) - 1):
    #             if text[i] == '\n':
    #                 line_count += 1
    #             if text[i] == '*' and text[i + 1] == '/':
    #                 return Token(ClassPart.MULTI_LINE_COMMENT, text[:i + 2], line + line_count + 1), i + 2
    #             if i == len(text) - 2:
    #                 return Token(ClassPart.INVALID, text, line), i + 2
    #     elif text.startswith("/*") and len(text) < 5:
    #         return Token(ClassPart.INVALID, text, line), len(text)

    #     return None, 0


    def is_int(self, word, line):
        if re.match("^[+-]?[0-9]+$", word):
            return Token(ClassPart.INT_CONSTANT.name, word, line)
        return None

    def is_double(self, word, line):
        if re.match("^[+-]?[0-9]*[.][0-9]+[d]?$", word):
            return Token(ClassPart.DOUBLE_CONSTANT.name, word, line)
        return None

    def is_bool(self, word, line):
        if word in ['true', 'false']:
            return Token(ClassPart.BOOL_CONSTANT.name, word, line)
        return None

    # def is_identifier(self, word, line):
    #     if re.match("^[_]?[A-Za-z]+([_]*[A-Za-z0-9]*)*[_]*$", word):
    #         return Token(ClassPart.IDENTIFIER.name, word, line)
    #     return None
    def is_identifier(self, word, line):
        if re.match("^[+_]?[A-Za-z]+([_]*[A-Za-z0-9]*)*[_]*$", word):
        # Check if the word is a keyword, and if so, return None
            if word in Grammar.Keywords:
                return None
            return Token(ClassPart.IDENTIFIER.name, word, line)
        return None


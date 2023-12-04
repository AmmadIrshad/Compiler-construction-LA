from classpart import ClassPart
class Grammar:
    WordBreakers = [' ', '\n', '\t', '\r']

    Keywords = {
        "break": ClassPart.BREAK,
        "continue": ClassPart.CONTINUE,
        "class": ClassPart.CLASS,
        "catch": ClassPart.CATCH,
        "else": ClassPart.ELSE,
        "default": ClassPart.DEFAULT,
        "if": ClassPart.IF,
        "for": ClassPart.FOR,
        "using": ClassPart.USING,
        "new": ClassPart.NEW,
        "void": ClassPart.VOID,
        "try": ClassPart.TRY,
        "return": ClassPart.RETURN,
        "static": ClassPart.STATIC,
        "this": ClassPart.THIS,
        "while": ClassPart.WHILE,
        "public": ClassPart.PUBLIC,
        "private": ClassPart.PRIVATE,
        "int": ClassPart.DATA_TYPE,
        "string": ClassPart.DATA_TYPE,
        "double": ClassPart.DATA_TYPE,
        "bool": ClassPart.DATA_TYPE,
        "do": ClassPart.DO,
        "in": ClassPart.IN,
        "True": ClassPart.BOOL_CONSTANT,
        "False": ClassPart.BOOL_CONSTANT
    }

    Punctuators = {
        ";": ClassPart.SEMI_COLON,
        ":": ClassPart.COLON,
        ",": ClassPart.COMMA,
        ".": ClassPart.DOT,
        "(": ClassPart.OPENING_PARANTHESES,
        ")": ClassPart.CLOSING_PARANTHESES,
        "{": ClassPart.OPENING_CURLY_BRACKET,
        "}": ClassPart.CLOSING_CURLY_BRACKET,
        "[": ClassPart.OPENING_SQUARE_BRACKET,
        "]": ClassPart.CLOSING_SQUARE_BRACKET
    }

    Operators = {
        "+=": ClassPart.COMPOUND_EQUAL,
        "-=": ClassPart.COMPOUND_EQUAL,
        "/=": ClassPart.COMPOUND_EQUAL,
        "*=": ClassPart.COMPOUND_EQUAL,
        "%=": ClassPart.COMPOUND_EQUAL,
        "++": ClassPart.INCREMENT_DECREMENT,
        "--": ClassPart.INCREMENT_DECREMENT,
        "+": ClassPart.PLUS_MINUS,
        "-": ClassPart.PLUS_MINUS,
        "*": ClassPart.MULTIPLY_DIVIDE_MODULUS,
        "/": ClassPart.MULTIPLY_DIVIDE_MODULUS,
        "%": ClassPart.MULTIPLY_DIVIDE_MODULUS,
        "&&": ClassPart.AND,
        "||": ClassPart.OR,
        "<=": ClassPart.RELATIONAL_OPERATOR,
        ">=": ClassPart.RELATIONAL_OPERATOR,
        "!=": ClassPart.RELATIONAL_OPERATOR,
        "==": ClassPart.RELATIONAL_OPERATOR,
        "!": ClassPart.NOT,
        ">": ClassPart.RELATIONAL_OPERATOR,
        "<": ClassPart.RELATIONAL_OPERATOR,
        "=": ClassPart.EQUAL
    }

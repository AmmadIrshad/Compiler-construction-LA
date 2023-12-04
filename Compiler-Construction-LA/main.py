from lexical_analyzer import LexicalAnalyzer

# Example usage of LexicalAnalyzer
if __name__ == "__main__":
    lexical_analyzer = LexicalAnalyzer()

    # Example text for analysis
    example_text = """interface::A_B_C
    while (a.b.c<<<<<==78.65 
    b+++=56.75ab7.11/*.56 bcx.55.55.a5c
    char c="abc++=\\"abc\\\*/"abc"a=b=c
    string s='\\\'+'++'\n'+=35'\\
    return a&&==@bc
    int
    _ava = 0"""
    

    # Analyze the example text
    tokens = lexical_analyzer.analyze(example_text)
    output_file = open("output.txt", "w")
    # Display the tokens
    for token in tokens:
        output_file.writelines(f"[LINE NUMBER: {str(token.LineNumber).ljust(5)},\tCLASS PART: {str(token.ClassPart).ljust(20)},\tVALUE: {token.Value}]\n")
        print(f"LINE NUMBER: {str(token.LineNumber).ljust(5)},\tCLASS PART: {str(token.ClassPart).ljust(20)},\tVALUE: {token.Value}")


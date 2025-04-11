import re

def tokenize_sentence(text):

    pattern = r'[ऀ-ॿ]+|[a-zA-Z]+|[.,!?]+|[0-9]+'
    tokens = re.findall(pattern, text)
    return tokens

def build_vocab(tokens) :

    unique_tokens = list(set(tokens))

    unique_tokens.sort()

    token_to_num = {}
    num_to_token = {}

    for i, token in enumerate(unique_tokens):
        token_to_num[token] = i
        num_to_token[i] = token

    return token_to_num, num_to_token

def encode_tokens(tokens, token_to_num):
    return [token_to_num[t] for t in tokens]

def decode_nums(nums, num_to_tokens):
    return [num_to_tokens[i] for i in nums]

if __name__ == "__main__":
    sentence = "Hello नमस्ते, this is a test. क्या हाल हैं?"

    tokens = tokenize_sentence(sentence)
    print("Original Tokens:")
    print(tokens)
    
    token_to_nums, nums_to_token = build_vocab(tokens)
    
    encoded_nums = encode_tokens(tokens, token_to_nums)
    print("\nEncoded Nums:")
    print(encoded_nums)
    
    decoded_tokens = decode_nums(encoded_nums, nums_to_token)
    print("\nDecoded Tokens:")
    print(decoded_tokens)
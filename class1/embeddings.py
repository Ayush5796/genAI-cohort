from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

text = "Andromeda is the closest spiral galaxy to the Milky Way and is expected to merge with our galaxy in about 4 billion years."

response = client.embeddings.create(
    input=text,
    model="text-embedding-3-small"
)

print("Vector Embedding : ", response.data[0].embedding)
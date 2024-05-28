import os
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('distiluse-base-multilingual-cased-v1')
model.save(os.path.join(os.getcwd(), "models", "distiluse-base-multilingual-cased-v1"))

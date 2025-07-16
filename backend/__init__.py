from ._base import BaseEmbedder
from ._utils import NotInstalled
from ._sentencetransformers import SentenceTransformerBackend
from ._utils import NotInstalled, select_backend
from ._mmr import mmr

# Sentence Transformers
try:
    from ._sentencetransformers import SentenceTransformerBackend
except ModuleNotFoundError:
    msg = "`pip install sentence-transformers`"
    SentenceTransformerBackend = NotInstalled("Sentence-Transformers", "sentence-transformers", custom_msg=msg)



__all__ = [
    "BaseEmbedder",
    "SentenceTransformerBackend",
    "NotInstalled",
    "select_backend"]

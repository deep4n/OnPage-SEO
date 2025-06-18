from ._base import BaseEmbedder


def select_backend(embedding_model) -> BaseEmbedder:
    """Select an embedding model based on language or a specific sentence transformer models.
    When selecting a language, we choose `all-MiniLM-L6-v2` for English and
    `paraphrase-multilingual-MiniLM-L12-v2` for all other languages as it support 100+ languages.

    Returns:
        model: Either a Sentence-Transformer or Flair model
    """
    # keybert language backend
    if isinstance(embedding_model, BaseEmbedder):
        return embedding_model

    # Sentence Transformer embeddings
    if "sentence_transformers" in str(type(embedding_model)):
        from ._sentencetransformers import SentenceTransformerBackend

        return SentenceTransformerBackend(embedding_model)

    # Create a Sentence Transformer model based on a string
    if isinstance(embedding_model, str):
        from ._sentencetransformers import SentenceTransformerBackend

        return SentenceTransformerBackend(embedding_model)

class NotInstalled:
    """This object is used to notify the user that additional dependencies need to be
    installed in order to use the string matching model.
    """

    def __init__(self, tool, dep, custom_msg=None):
        self.tool = tool
        self.dep = dep

        msg = f"In order to use {self.tool} you will need to install via;\n\n"
        if custom_msg is not None:
            msg += custom_msg
        else:
            msg += f"pip install keybert[{self.dep}]\n\n"
        self.msg = msg

    def __getattr__(self, *args, **kwargs):
        raise ModuleNotFoundError(self.msg)

    def __call__(self, *args, **kwargs):
        raise ModuleNotFoundError(self.msg)

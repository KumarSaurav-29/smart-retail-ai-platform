import re
import string

import spacy

nlp = spacy.load("en_core_web_sm")


def clean_text(text: str):

    text = text.lower()

    text = re.sub(r"http\S+", "", text)

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    doc = nlp(text)

    tokens = []

    for token in doc:

        if (
            not token.is_stop
            and not token.is_punct
            and not token.like_num
        ):
            tokens.append(token.lemma_)

    return " ".join(tokens)
import nltk
from spacy.en import English


def build_parse_tree():
    print('Starting to build parser')
    parser = English(tagger=False, entity=False)
    print('End to build parser')
    sent = "The ball has been hit by the boy."
    dependency_tree = parser(sent)
    root = find_root(dependency_tree)
    print(root)


def find_root(dependency_tree):
    for token in dependency_tree:
        if token.head == token:
            return token


def find_named_entities(sent):
    tokens = nltk.word_tokenize(sent)
    tokens = nltk.pos_tag(tokens)
    tree = nltk.ne_chunk(tokens)
    named_entities = []
    for child in tree:
        named_entities.append(extract_entity_names(child))
    return named_entities


def extract_entity_names(t):
    entity_names = []
    if hasattr(t, 'label') and t.label:
        print(t.label())
        if t.label() == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))

    return entity_names

if __name__ == "__main__":
    sent = "I am very excited about the next generation of Apple products."
    find_named_entities(sent)

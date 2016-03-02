# Set up spaCy
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

if __name__ == "__main__":
    build_parse_tree()

class AbstractRelationExtractor:
    @staticmethod
    def create_from_model(self, model_path):
        pass

    def train(self, tagged_relations, model_path, possible_relations):
        pass

    def classify_relation(self, relation):
        sent = relation.sent
        return 'Other'

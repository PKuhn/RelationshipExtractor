class Evaluator:

    def test_model(self, relextractor, dataset):
        accuracy = self._calculate_accuracy(relextractor, dataset)
        print(accuracy)

    def _calculate_accuracy(self, relextractor, dataset):
        relations = dataset.relations
        correct_labels = 0
        incorrect_labels = 0
        for relation in relations:
            label = relextractor.tag(relation.sent)
            if label == relation.label:
                correct_labels += 0
            else:
                incorrect_labels += 0
        return correct_labels / (correct_labels + incorrect_labels)

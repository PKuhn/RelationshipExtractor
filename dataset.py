class Dataset:
    def __init__(self, relations):
        self.relations = relations


class Relation:
    def __init__(self, sent, first_pos, second_pos, label):
        self.sent = sent
        self.first_pos = first_pos
        self.second_pos = second_pos
        self.label = label

    def __str__(self):
        words = self.sent.split()
        first_entity = " ".join(
            words[self.first_pos[0]: self.first_pos[1] + 1])
        second_entity = " ".join(
            words[self.second_pos[0]: self.second_pos[1] + 1])
        relation_str = "A relation between {} and {}".format(
            first_entity, second_entity)
        return relation_str

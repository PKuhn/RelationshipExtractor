from dataset import Relation, Dataset


class SemEvalParser:
    def retrieve_from_sem_eval(self, path):
        with open(path) as infile:
            instring = infile.read()
            examples = instring.split('\n\n')
            relations = [self.create_relation(example) for
                         example in examples]

            return Dataset(relations)

    def create_relation(self, example):
        sent, label, comment = example.split('\n')
        first_pos, second_pos = self.find_positions(sent)
        clear_sent = self.clear_line(sent)
        return Relation(clear_sent, first_pos, second_pos, label)

    def find_positions(self, sent):
        for idx, word in enumerate(sent.split()):
            if "<e1>" in word:
                first_start = idx
            if "</e1>" in word:
                first_end = idx
            if "<e2>" in word:
                second_start = idx
            if "</e2>" in word:
                second_end = idx

        first_pos = (first_start, first_end)
        second_pos = (second_start, second_end)
        return (first_pos, second_pos)

    def clear_line(self, line):
        to_delete = ["<e1>", "</e1>", "<e2>", "</e2>"]
        for delete_word in to_delete:
            line = line.replace(delete_word, '')
        return line

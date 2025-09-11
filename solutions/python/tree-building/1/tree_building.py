class Record():
    def __init__(self, record, parent):
        self.record = record
        self.parent = parent


class Node():
    def __init__(self, node):
        self.node_id = node
        self.children = []


def BuildTree(records):
    if not records: return

    records.sort(key=lambda rec: rec.record)

    if not all(
        rec.record == i for i, rec in enumerate(records)
        ): raise ValueError(
            'Tree must be continuous from 0'
            )
    if not all(
        rec.parent == 0 or
        rec.parent < rec.record
        for rec in records
        ): raise ValueError(
            'Parent ID must be 0 or lower than Child ID'
            )

    nodes = [Node(0)]

    for rec in records[1:]:
        nodes.append(Node(rec.record))
        nodes[rec.parent].children.append(nodes[-1])

    return nodes[0]

__all__ = [
    'get_subclasses',
]


def get_subclasses(cls):
    subclasses = set()
    classes = [cls]

    while classes:
        parent = classes.pop()
        for child in parent.__subclasses__():
            if child not in subclasses:
                subclasses.add(child)
                classes.append(child)

    return subclasses

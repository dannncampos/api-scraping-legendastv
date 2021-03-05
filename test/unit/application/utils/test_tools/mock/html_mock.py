class HTMLMock:

    def __init__(self, content):
        self.content = content

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.content == other.content
        return False

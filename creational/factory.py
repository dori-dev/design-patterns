from abc import ABC, abstractmethod


class Creator(ABC):  # creator
    @abstractmethod
    def make(self):
        pass

    def call_edit(self, name: str):
        file: File = self.make(name)
        return file.edit()


class JsonCreator(Creator):
    def make(self, name):
        return Json(name)


class XmlCreator(Creator):
    def make(self, name):
        return Xml(name)


class PdfCreator(Creator):
    def make(self, name):
        return Pdf(name)


class File(ABC):  # product
    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def edit(self):
        pass


class Json(File):
    def edit(self):
        return f'Editing json file {self.name}.json ...'


class Xml(File):
    def edit(self):
        return f'Editing xml file {self.name}.xml ...'


class Pdf(File):
    def edit(self):
        return f'Editing pdf file {self.name}.pdf ...'


def edit(name, format: Creator):
    return format.call_edit(name)


if __name__ == '__main__':
    print(edit('resume', JsonCreator()))
    print(edit('resume', XmlCreator()))
    print(edit('resume', PdfCreator()))

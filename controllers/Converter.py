import sys

from pdf2docx import Converter


class ConverterTo:
    def __init__(self, from_: str, to: str) -> None:
        """
        Classe que converte pdf para word
        Recebe arquivo origem e o tipo de destiono

        :param from_:
        :param to:
        """
        self.__pdf = from_
        self.__docx = to

    def converter_to_docx(self) -> None:
        """
        Converte de pdf para docx
        :return:
        """
        try:
            file = Converter(self.__pdf)
            file.convert(self.__docx)
            file.close()
        except Exception as e:
            print(e)
            pass
        else:
            file.close()
            sys.exit()
        finally:
            ...


if __name__ == '__main__':
        c = ConverterTo("partes_removed.pdf", "word.docx")
        c.converter_to_docx()
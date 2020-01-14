#!/usr/bin/python3
""" Function text_indentation """


def text_indentation(text):
    """ Function that print a text

        Arguments:
                @text:
                    Must be a string, otherwise a TypeError is
                    going to be raised.
                    There should be no space at the beginning or
                    at the end of each printed line

        Return:
                Doesn't return anything
                Print a text in the stdout
    """
    if type(text) != str:
        raise TypeError('text must be a string')
    else:
        i = 0
        m_l = [':', '?', '.']
        while i < len(text) and text[i] != '\0':
            if ord(text[i]) < 65 or ord(text[i]) > 122:
                for l in m_l:
                    if text[i] is l:
                        print("{}".format(text[i]), end="\n\n")
                        if i + 1 == len(text) or text[i + 1] == '\0':
                            return
                        else:
                            while text[i + 1] == ' ':
                                i += 2
                    else:
                        continue
                print("{}".format(text[i]), end="")
            else:
                print("{}".format(text[i]), end="")
            i += 1

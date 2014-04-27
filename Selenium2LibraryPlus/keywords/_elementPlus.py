from Selenium2Library.keywords import *

class _ElementKeyWordsPlus(_ElementKeywords):
    """docstring for _ElementKeyWordsPlus"""
    def __init__(self):
        super(_ElementKeyWordsPlus, self).__init__()
        #self.arg = arg


    def get_matching_count(self, locator):
        """Returns number of elements matching `xpath,Css, id`

        If you wish to assert the number of matching elements, use
        `Xpath Should Match X Times`.
        """
        count = len(self._element_find(locator, False, False))
        return str(count)

if __name__ == '__main__':
    a=_ElementKeyWordsPlus
    print a.__bases__
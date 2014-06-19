import time
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

    def get_matching_elements(self, locator):
        """Returns List of elements matching `xpath,Css, id`
        """
        return self._element_find(locator, False, False)

    #action
    def clear_all_content(self, locator):
        for el in self._element_find(locator, False, False):
            #self.highlight_element(locator)
            el.clear()

    def highlight_element(self, locator):
        """docstring for highlight_element"""
        #self._info("Current page is aaaa '%s'" % self.current._current_url)
        self._info("highlight_element %s" % locator)
        element = self._element_find(locator, True, True)
        parent = element._parent
        # old_style = element.get_attribute('style')
        # new_style = "blackground: yellow; border: 2px solid red;"
        parent.execute_script("""
            element = arguments[0];
            original_style = element.getAttribute('style');
            element.setAttribute('style', original_style + "; background: yellow; border: 2px solid red;");
            setTimeout(function(){
                element.setAttribute('style', original_style);
        }, 1000);
        """, element)
        time.sleep(1.1)
        #parent.execute_script("%s.setAttribute('style',%s);" % (element, old_style))

    def Get_All_Text(self, locator):
        li=[]
        for el in self._element_find(locator, False, False):
            if el is not None:
                li.append(el.text)
        return "\n".join(li)


if __name__ == '__main__':
    a=_ElementKeyWordsPlus
    print a.__bases__
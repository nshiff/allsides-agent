import pprint
class AllSidesItem:
    ITEM_AS_JSON__ORIGINAL = None
    field_article_link = ''
    field_bias_image__alt = ''
    field_bias_image__src = ''
    field_image_of_news__alt = ''
    field_image_of_news__src = ''
    field_news_source = ''
    path = ''
    title = ''

    def _careful_dictionary_get(self, dictionary, key):
        if key in dictionary:
            return dictionary[key]
        return ''

    def __init__(self,item_as_json):
        self.ITEM_AS_JSON__ORIGINAL = item_as_json
        self.field_article_link = self._careful_dictionary_get(item_as_json, 'field_article_link')
        self.field_bias_image__alt = self._careful_dictionary_get(item_as_json, 'field_bias_image__alt')
        self.field_bias_image__src = self._careful_dictionary_get(item_as_json, 'field_bias_image__src')
        self.field_image_of_news__alt = self._careful_dictionary_get(item_as_json, 'field_image_of_news__alt')
        self.field_image_of_news__src = self._careful_dictionary_get(item_as_json, 'field_image_of_news__src')
        self.field_news_source = self._careful_dictionary_get(item_as_json, 'field_news_source')
        self.path = self._careful_dictionary_get(item_as_json, 'path')
        self.title = self._careful_dictionary_get(item_as_json, 'title')

    def __str__(self):
        return pprint.pformat(self.ITEM_AS_JSON__ORIGINAL)

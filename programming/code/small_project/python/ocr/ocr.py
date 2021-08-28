from aip import AipOcr

class Ocr:
    def __init__(self, image_path):
        self.path = image_path

        APP_ID = 'app_id'
        API_KEY = 'api_key'
        SECREY_KEY = 'secrey_key'
        self.client = AipOcr(APP_ID, API_KEY, SECREY_KEY)

    def __get_image_content(self, file_path):
        with open(file_path, 'rb') as fp:
            return fp.read()

    def run(self):
        self.options = {}
        self.options['language_type']    = 'CHN_ENG'
        self.options['detect_direction'] = 'true'
        self.options['detect_language']  = 'true'
        self.options['probability']      = 'true'

        image_content = self.__get_image_content(self.path)
        try:
            response = self.client.basicAccurate(image_content, self.options)
            string = response['words_result']
            self.words_result = ''
            length = len(string)
            for s in string:
                self.words_result = self.words_result + s['words']
                length -= 1
                if length > 0:
                    self.words_result += '\n'
        except:
            self.words_result = 'failure'

    def result(self):
        return self.words_result

class MDWriter:

    def __init__(self, data):

        self.__objectives = data["learn_objectives"]
        self.__title = data["file_name"]
        self.__files = data['files']

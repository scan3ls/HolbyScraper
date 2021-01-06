class Parser:
    """
        Parse through HTML data;
        Store and Return deisred data
    """
    def __init__(self, data):
        """
        --------------
        Method: __init__
        --------------
        Description:
            constructor
        Args:
            @data: List of Strings
                HTML data
        --------------
        """

        self.__data = data
        self.__objectives = []
        self.__proj_dir = None
        self.__files = ""

    def get_objectives(self):
        """
        --------------
        Method: get_objectives
        --------------
        Description:
            Get project objectives from html data
        Args:
            None
        --------------
        """

        if self.__objectives != []:
            return self.__objectives

        import re

        appending = False
        objectives = []
        for line in self.__data:
            if re.match(".+Learning objectives.+", line):
                appending = True

            r1 = re.match(".*<li>(.+)</li>", line)
            if appending and r1:
                self.__objectives.append(r1.groups()[0])
            if re.match(".*</ul>", line) and appending:
                break
        return self.__objectives

    def get_proj_dir(self):
        """
        --------------
        Method: get_proj_dir
        --------------
        Description:
            Get project directory from html data
        Args:
            None
        --------------
        """

        if self.__proj_dir is not None:
            return self.__proj_dir

        import re

        r1, r2 = None, None
        for line in self.__data:

            if r1 is None:
                r1 = re.match(".+GitHub repository: <code>(.+)</code>", line)

            if r2 is None:
                r2 = re.match(".+Directory: <code>(.+)</code>", line)

            if r1 and r2:
                break

        if r1 is None or r2 is None:
            print("No directory found")
            exit(3)

        repo = "{}/{}".format(
            r1.groups()[0],
            r2.groups()[0]
        )

        self.__proj_dir = repo
        return repo

    def get_files(self):
        """
        --------------
        Method: get_files
        --------------
        Description:
            Get project files from html data
        Args:
            None
        --------------
        """

        if self.__files != "":
            return self.__files.split(", ")

        import re
        for line in self.__data:
            r1 = re.match(".*File: <code>(.*)</code>", line)
            if r1:
                self.__files += ", " + r1.groups()[0]
        self.__files = self.__files[2:]

        return self.__files.split(", ")

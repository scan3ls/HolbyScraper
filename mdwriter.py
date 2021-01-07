class MDWriter:
    """
        Create and Write the project's Readme
    """
    def __init__(self, data):
        """
        --------------
        Method: __init__
        --------------
        Description:
            constructor
        Args:
            @data: Dictionary
                @learn_objectives: List of Strings
                    List of learning Objectives
                @file_name: String
                    Path of the readme file
                @files: List of Strings
                    List of file names
        --------------
        """

        self.__objectives = data["learn_objectives"]
        self.__file_name = data["file_name"]
        self.__files = data['files']

    def write(self):
        """
        --------------
        Method: write
        --------------
        Description:
            Writes content to file
        Args:
            None
        --------------
        """

        with open(self.__file_name, "w") as f:

            title = self._get_title()
            f.write(title)

            intro = "{} {}".format(
                "This repository is used for project based",
                "learning in Holberton.\n\n"
            )
            f.write("## Introduction\n")
            f.write(intro)

            f.write("## Learning Objectives\n")
            for item in self.__objectives:
                string = self._md(item)
                f.write("- {}\n".format(string))

    def _get_title(self):
        """
        --------------
        Method: _get_title
        --------------
        Description:
            Format a title for README file
        Args:
            None
        --------------
        """
        title = self.__file_name.split("/")[0]
        title = title.replace("-", ". ")

        return "# {}\n\n".format(title)

    def _md(self, string):
        """
        --------------
        Method: _md
        --------------
        Description:
            Parse a html string into md
        Args:
            @string: String
                A string that may have html code
        --------------
        """
        import re

        string = re.sub(r'(<code>|</code>)', '`', string)
        return string

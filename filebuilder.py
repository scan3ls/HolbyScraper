class FileBuilder:
    """
        Creates project directory and file structure
        from the root repository
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
                @pwd: root project repo
                @proj_dir: project directory
                @files: list of project files
        --------------
        """
        self.__pwd = data["pwd"]
        self.__proj_dir = data["proj_dir"]
        self.__files = data["files"]

        self.__check_pwd()

    def create_files(self):
        """
        --------------
        Method: create_files
        --------------
        Description:
            create project files in project directory
            if the files don't already exist
        Args:
            None
        --------------
        """

        from os import path, mkdir

        proj_dir = self.__proj_dir.split('/')[1]
        if path.exists(proj_dir) is False:
            mkdir(proj_dir)

        for file in self.__files:
            file_path = "{}/{}".format(proj_dir, file)
            if path.exists(file_path):
                continue
            else:
                with open(file_path, 'w') as f:
                    f.write("")

    def __check_pwd(self):
        """
        --------------
        Method: chech_pwd
        --------------
        Description:
            Checks if current project folder structure
            is correct
        Args:
            @pwd: String
                formatted current working directory
            @proj_dir: String
                expected project directory
        --------------
        """

        pwd = self.__root_dir()
        root = self.__proj_dir.split("/")[0]
        if root != pwd:
            print(
                "PWD:{} is the wrong directory.\nExpected: {}".format(
                    pwd, root
                )
            )
            exit(1)

    def __root_dir(self):
        """
        --------------
        Method: __root_dir
        --------------
        Description:
            Format a given directory path
            into a more usable format
        Args:
            @pwd: String
                Current working directory
        --------------
        """

        dirs = self.__pwd.split('/')
        if len(dirs) < 2:
            print("Please check root directory and repo directory.")
            exit(1)

        return dirs[-1]

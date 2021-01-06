class Scraper:
    """
        Navigate and Download a HTML page
    """

    def __init__(self):
        """
        --------------
        Method: __init__
        --------------
        Description:
            constructor
        Args:
            None
        --------------
        """

        print("\n\t->Initalizing scraper")
        self.__data = {
            'uft8': '&#x2713;',
            'authenticity_token': '',
            'user[login]': '',
            'user[password]': '',
            'user[remember_me]': '1',
            'commit': 'Log in'
        }
        self.__login_url = 'https://intranet.hbtn.io/auth/sign_in'

    def _set_token(self, html):
        """
        --------------
        Method: _set_token
        --------------
        Description:
            Gets the authenticity token
            and stores it
        Args:
            @html: list of strings
                Each line of html stored
                in a list
        --------------
        """
        print("\t->Retreiving Authenticity Token")
        for line in html:
            if "csrf-token" not in line:
                continue
            result = line[-92: -4]
            self.__data["authenticity_token"] = result
            return

    def _set_login(self):
        """
        --------------
        Method: _set_login
        --------------
        Description:
            Get and store Holberton login details
        Args:
            None
        --------------
        """

        print("\t->preparring Login Information")
        data = {}
        path = "/opt/HolbyScraper/.env"
        with open(path, 'r') as f:
            reading = True
            while reading:
                line = f.readline().rstrip()
                if line == "":
                    break
                line = line.split('=')
                key = line[0]
                value = line[1]
                data[key] = value

        if data["user_name"] == "" or data["user_pass"] == "":
            print(
                "\n\tCheck login settings in {}".format(path)
            )
            exit(1)

        self.__data["user[login]"] = data["user_name"]
        self.__data["user[password]"] = data["user_pass"]

    def scrape(self, num=None):
        """
        --------------
        Method: scrape
        --------------
        Description:
            Log in to the Holberton intranet and
            download specific project html page
        Args:
            @num: Integer
                Target project number; listed on
                the end of the project url
        --------------
        """

        import requests

        with requests.session() as s:

            res = s.get(self.__login_url)
            html = res.text.split('\n')

            self._set_token(html)
            self._set_login()

            print("\t->Logging In")
            s.post(self.__login_url, data=self.__data)

            print("\t->Traveling to Project Page\n...Done!\n")
            if num is None:
                url = self.__login_url
            else:
                url = "https://intranet.hbtn.io/projects/{}".format(str(num))
            res = s.get(url)

            return res.text.split('\n')

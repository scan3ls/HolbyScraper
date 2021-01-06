class Scraper:

    def __init__(self):
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
        print("\t->Retreiving Authenticity Token")
        for line in html:
            if "csrf-token" not in line:
                continue
            result = line[-92: -4]
            self.__data["authenticity_token"] = result
            return

    def _set_login(self):
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
        self.__data["user[login]"] = data["user_name"]
        self.__data["user[password]"] = data["user_pass"]

    def scrape(self, num=None):
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

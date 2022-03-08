import requests, time, os
from bs4 import BeautifulSoup

class GetModelsID:
    def __init__(self):
        self.model_id = input("Desire model id: ")
        self.counts = 0
        self.new_list = []
        self.found_url = None
        self.bar = [
            " [=     ]",
            " [ =    ]",
            " [  =   ]",
            " [   =  ]",
            " [    = ]",
            " [     =]",
            " [    = ]",
            " [   =  ]",
            " [  =   ]",
            " [ =    ]",]
        self.anim_index = 0
    def listFD(self, url, ext=''):
        return [url + node.get('href') for node in BeautifulSoup(requests.get(url).text, 'html.parser').find_all('a') if node.get('href').endswith(ext)]
    def FindModel(self):
        for i in self.listFD("http://107.173.229.72/3DModels/")[5:]:        ## 3dripper mf ip for models
            self.new_list.append(i)
            for i in self.new_list:
                for x in self.listFD(i):
                    time.sleep(.005)
                    if x.find(self.model_id) > 0:
                        self.counts += 1
                        self.found_url = x  
                        return      ## Don't work with break cause dunno 
                    print("Fetching", self.bar[self.anim_index % len(self.bar)], end="\r")
                    self.anim_index += 1
    def DoWork(self):
        self.FindModel()
        os.system('cls||clear')
        print(f"Found: {self.counts} | URL: {self.found_url}")

if __name__=="__main__":
    GetModelsID().DoWork()
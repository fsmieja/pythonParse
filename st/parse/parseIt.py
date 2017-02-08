import sys
from HTMLParser import HTMLParser


class Parser(HTMLParser):
    # 
    rows = []
    repos=[]
    recording=False
    haveRow=False
    haveSpan=False
    colNum=0
    results=[]
    repoName=""
    repoDate=""
    
    # create a subclass and override the handler methods
    def handle_starttag(self, tag, attrs):
 
        if tag == "tr":
            self.haveRow = True
            return
        if self.haveRow:
            if tag=="th":
                self.haveRow=False 
            if tag=="td":
                self.colNum+=1
                return
            if self.colNum==5 and tag=="span":
                self.haveSpan=True 
        
             

    def handle_endtag(self, tag):
        if tag == "tr":
            if self.haveRow:
                self.repos.append([self.repoName,self.repoDate])
            self.haveRow=False
            self.colNum=0
            self.repo=[]

    def handle_data(self, data):
        data = data.strip()
        if len(data)==0:
            return
        if self.haveSpan:
            self.repoDate=data
            self.haveSpan=False

        if self.haveRow and self.colNum==1:
            self.repoName=data
 
        #print "Encountered some data  :", data
    
    def __init__(self):
        HTMLParser.__init__(self)
        '''
        Constructor
        '''
        
class ProcessParse(object):
    
    DAYSINMONTH = 30
    DAYSINWEEK = 7

    def processHtml(self,htmlStr):
        parser = Parser()
        #print htmlStr
        parser.feed(htmlStr)
        res = ""
        for repo in parser.repos:
            if self.tooLong(repo[1]):
                days = self.getNumberOfDays(repo[1])
                res += "Repo "+repo[0]+": "+str(days)+" days since last change\n"
        print res


    def tooLong(self,dt):
        if "months" in dt or "years" in dt:
            return True
        else:
            firstNum = int(dt.split(" ")[0])
            if "weeks" in dt and firstNum > 4:
                return True
        return False
    

    def getNumberOfDays(self,dateStr):
        days = 0
        num = dateStr.split(" ")[0]
        if "months" in dateStr:
            days = int(num) * self.DAYSINMONTH
        elif "weeks" in dateStr:
            days = int(num) * self.DAYSINWEEK

        return days

def main():
    if len(sys.argv) != 2:
        print "Usage: python parseIt.py <filename>"
        return
    parser = ProcessParse()
    fName = sys.argv[1]
    f = open(fName)
    parser.processHtml(f.read())

    
if __name__ == "__main__":
    main()
    



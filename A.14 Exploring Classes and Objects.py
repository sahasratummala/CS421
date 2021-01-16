Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> class NewsPaper:
    
    def __init__(self, name, year, reporters, founder):
        self.name = name
        self.yearfounded = year
        self.numberofreporters = reporters
        self.founder = founder

    def getDetails(self):
        print("Name : " + self.name)
        print("Year founded : " + self.yearfounded)
        print("Number of reporters : " + self.numberofreporters)
        print("Founder : " + self.founder)
        
        voiceOfFrisco = NewsPaper("Voice of Frisco", "2020", "15", "Sahasra Tummala"
        voiceOfFrisco.getDetails()
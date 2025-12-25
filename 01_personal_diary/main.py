from datetime import datetime
        
class DiaryPage:
        
    def save(self):
        fileName = f"{datetime.now().strftime("%Y-%b-%d %H-%M-%S")}.txt"
        with open(fileName, "w") as fh:
            self.date = datetime.now().strftime("%Y %b %d %A %I:%M %p").split(" ")
            fh.write(f"{self.date[0]}\n{self.date[1]}\n{self.date[2]} {self.date[3]}\n")
            fh.write("\n\n"+self.title+"\n\n")
            fh.write(self.content)
    
    def getData(self):
        self.title = input("Enter Title:- ")
        self.content = input("Write your diary page:- ")
        

if __name__ == "__main__":
    print("My Diary!!!")
    while True:
        action = input("Enter 'n' for new entry or 'q' to quit:- ")
        if (action == 'n'):
            entry = DiaryPage()
            entry.getData()
            entry.save()
        
        else:
            break



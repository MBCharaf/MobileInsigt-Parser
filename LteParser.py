from MiParser import MiParser
import json

class LteParser(MiParser):
    def open_file(self):
        self.output_file = open(self.target_logs+".csv","w")

    def sorter(self,dictionery):
        if dictionery["type_id"] == self.target_logs:
            self.parsed_logs.append(dictionery)
            self.to_csv(self.output_file,dictionery)
            self.find_csv_header(dictionery)
        
    def to_json(self):
        with open(self.target_logs+'.json', 'w', encoding='utf-8') as f:
            json.dump(self.parsed_logs, f, ensure_ascii=False, indent=4)


    def to_csv(self,f,dictionery):
        for i in dictionery:
            f.write(str(dictionery[i])+",")
        f.write("\n")

    def find_csv_header(self,dictionery):
        if len(dictionery) >= self.header_len:
            self.header=[]
            self.header_len =len(dictionery)
            for i in dictionery:
                self.header.append(i)
    
    def add_header(self):
        f= open(self.target_logs+"_Header.txt","w")
        for i in self.header:
            f.write(str(i)+",")
        f.close()


        

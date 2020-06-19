import xml.etree.ElementTree as etree
import json

class MiParser:
    def __init__(self,filename,target_logs):
        self.filename = filename
        self.target_logs = target_logs
        self.keys = []
        self.values = []
        self.count = 0
        self.repeated = False
        self.repetition_idx = 0
        self.header = []
        self.header_len = 0
        self.parsed_logs = []

    def read_file(self):
        self.root = etree.parse(self.filename).getroot()
            
    def get_length(self,data):
        if(len(data)== 0 and data.text):
            self.count+=1
        else:
            for n in data:
                self.get_length(n)

    def collect_data(self,data):
        if(len(data)== 0 and data.text):
            if self.repeated == True:
                self.keys.append(str(data.attrib["key"])+"_"+str(self.repetition_idx))
                self.values.append(data.text)
            else:
                self.keys.append(str(data.attrib["key"]))
                self.values.append(data.text)
        else:
            for n in data:
                if  n.tag == "dict" :
                    self.repeated = True
                    self.repetition_idx +=1
                self.collect_data(n)
    
    def open_file(self):
        self.output_file = open(self.target_logs+".csv","w")
    
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

    def sorter(self,dictionery):
        if dictionery["type_id"] == self.target_logs:
            self.parsed_logs.append(dictionery)
            self.to_csv(self.output_file,dictionery)
            self.find_csv_header(dictionery)
    
    def add_header(self):
        f= open(self.target_logs+"_Header.txt","w")
        for i in self.header:
            f.write(str(i)+",")
        f.close()

    def build_dictionery(self,k,v):
        dictionery = dict(zip(k,v))
        self.sorter(dictionery)
    
    def to_json(self):
        with open(self.target_logs+'.json', 'w', encoding='utf-8') as f:
            json.dump(self.parsed_logs, f, ensure_ascii=False, indent=4)

    def run(self):
        self.read_file()
        self.open_file()
        for i in range(len(self.root)):
            self.get_length(self.root[i])
            self.collect_data(self.root[i])
            if (len(self.keys) == self.count):
                self.build_dictionery(self.keys,self.values)
                del self.values[:],self.keys[:]
                self.count = 0
                self.repetition_idx = 0
                self.repeated = False
        self.add_header()
        self.to_json()

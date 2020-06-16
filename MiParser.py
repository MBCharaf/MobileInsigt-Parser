import xml.etree.ElementTree as etree
import os

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

    def build_dictionery(self,k,v):
        dictionery = dict(zip(k,v))
        self.sorter(dictionery)
    
    def sorter (self,dictionery):
        pass

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

import json
from pprint import pprint

from langchain.text_splitter import RecursiveJsonSplitter

from document_loader import JsonData

class SplitJson:
    def __init__(self, maxChunk=2000):
        self.maxChunk = maxChunk

        # calls JsonData from data loader
        self.json_data = JsonData().retrieve_json_data()

        splitter = RecursiveJsonSplitter(max_chunk_size=self.maxChunk)

        # creates list of str splits from original json data
        self.splits = splitter.split_text(json_data=self.json_data, convert_lists=True)

    # return list of all splits or specific one if index is given
    def returnSplitsSample(self, index="all"):
        if index == "all":
            return self.splits
        else:
            return self.splits[index]
        
    # return number of total splits
    def returnSplitsLength(self):
        return len(self.splits)
    
    # return split lengths of count given or all if no count given
    def returnSplitsSampleLengths(self, count="all"):
        if count == "all":
            return [len(split) for split in self.splits]
        else:
            return [len(split) for split in self.splits[:count]]
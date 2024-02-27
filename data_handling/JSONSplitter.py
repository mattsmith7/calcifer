from langchain.text_splitter import RecursiveJsonSplitter
from langchain.text_splitter import CharacterTextSplitter

from JSONLoader import JSONLoader

from pprint import pprint

class JSONSplitter:
    def __init__(self, maxChunk=2000):
        self.maxChunk = maxChunk

        # calls JsonData from data loader
        self.json_data = JSONLoader().json_data()

        self.splitter = RecursiveJsonSplitter(max_chunk_size=self.maxChunk)

        # creates list of str splits from original json data
        self.splits = self.splitter.split_json(json_data=self.json_data, convert_lists=True)

    # return list of all splits or specific one if index is given
    def get_splits(self, index="all"):
        if index == "all":
            return self.splits
        else:
            return self.splits[index]
        
    # return number of total splits
    def splits_length(self):
        return len(self.splits)
    
    # return split character lengths of count given or all if no count given
    def splits_char_lengths(self, count="all"):
        if count == "all":
            return [len(split) for split in self.splits]
        else:
            return [len(split) for split in self.splits[:count]]
        
class CharSplitter:
    def __init__(self, maxChunk=2000, chunkOverlap=400):
        self.maxChunk = maxChunk
        self.chunkOverlap = chunkOverlap

        # calls JsonData from data loader
        self.json_data = JSONLoader().json_data()

        print(type(self.json_data[0]))

        self.splitter = CharacterTextSplitter(
            separator='"id":',
            chunk_size=self.maxChunk,
            chunk_overlap=self.chunkOverlap,
            length_function=len,
            is_separator_regex=False,
        )

        self.splits = self.splitter.split_text(self.json_data)

    # return list of all splits or specific one if index is given
    def get_splits(self, index="all"):
        if index == "all":
            return self.splits
        else:
            return self.splits[index]
        
    # return number of total splits
    def splits_length(self):
        return len(self.splits)
    
    # return split character lengths of count given or all if no count given
    def splits_char_lengths(self, count="all"):
        if count == "all":
            return [len(split) for split in self.splits]
        else:
            return [len(split) for split in self.splits[:count]]

texts = JSONSplitter(10000).get_splits()

print(JSONSplitter(10000).splits_char_lengths())
print(JSONSplitter().splits_length())

pprint(texts[0])
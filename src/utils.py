import torch
from tqdm import tqdm
from typing import Any , List
from transformers import BertTokenizer, BertModel
import os
import re


from db.client import Client

class Utils():
    def __init__(self) -> None:
        pass

    def compute_similarity(self, U : str, V: str):
        # Check if pre-trained BERT model exists, and if not, load it
        #if not os.path.exists("./weights/bert-base-uncased"):
            #tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
            #model = BertModel.from_pretrained('bert-base-uncased')
            #model.save_pretrained("./weights/bert-base-uncased")
            #tokenizer.save_pretrained("./weights/bert-base-uncased")
        
        #tokenizer = BertTokenizer.from_pretrained('./weights/bert-base-uncased')
        #model = BertModel.from_pretrained('./weights/bert-base-uncased')

        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        model = BertModel.from_pretrained('bert-base-uncased')

        # Tokenize input texts and convert them to tensors
        inputs = tokenizer([U, V], padding=True, truncation=True, return_tensors='pt')
        input_ids = inputs['input_ids']
        attention_mask = inputs['attention_mask']

        # Generate BERT embeddings
        with torch.no_grad():
            outputs = model(input_ids, attention_mask=attention_mask)
            embeddings = torch.mean(outputs.last_hidden_state, dim=1)  # Average pooling of token embeddings

        # Compute cosine similarity between the embeddings
        similarity = torch.cosine_similarity(embeddings[0], embeddings[1], dim=0).item()
        return similarity


    def calculate_score(self, dict: dict, input: str,attribut : str):
        #Use compute_similarity to evaluate the similarity between the new input and the attribute belonging to the dictionary
        score = self.compute_similarity(input, dict[attribut])
        return score


    def processing(self, raw : List[dict] , input : str , attribut : str):
        # Liste de raw
        data_list = raw
        DictScore = {}
        #Loop on the list of dictionary and compute for every dictionary the similarity score
        for item in data_list:
            score = self.calculate_score(item, input,attribut)
            DictScore[score] = item
        #Sort the list of dictionaries according to the hightest smilarity score
        sorted_keys = sorted(DictScore.keys(), reverse=True)
        #we want to return only the first five items
        if len(sorted_keys)>=5:
            Nbr_Max =5
        else:
            Nbr_Max = len(sorted_keys)

        FiveFirst = {key : DictScore[key] for key in sorted_keys[ : Nbr_Max]}
        ListFiveFirst  = []

        #List of 5 first items
        for score , dict in FiveFirst.items():
            dict["SCORE"]= score
            ListFiveFirst.append(dict)
    
        return ListFiveFirst
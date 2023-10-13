from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict
import numpy as np # linear algebra
import pandas as pd 
import nltk
import string
import ast
import re
import unidecode
from final_parser import title_parser

def get_recommendations(N, scores):
    """
    Top-N recomendations order by score
    """
    # load in recipe dataset
    df_recipes = pd.read_csv("/home/anya/major_project/dataset/new_dataset.csv")
    # order the scores with and filter to get the highest N scores
    top = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:N]
    # create dataframe to load in recommendations
    recommendation = pd.DataFrame(columns=["TranslatedRecipeName", "TranslatedIngredients", "URL", "score"])
    count = 0
    for i in top:
        recommendation.at[count, "TranslatedRecipeName"] = title_parser(df_recipes["TranslatedRecipeName"][i])
        recommendation.at[count, "TranslatedIngredients"] = df_recipes["TranslatedIngredients"][i]
        recommendation.at[count, "URL"] = df_recipes["URL"][i]
        recommendation.at[count, "score"] = f"{scores[i]}"
        count += 1
    return recommendation
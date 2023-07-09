import sys,os
from src.exception import CustomException
from src.logger import logging
from src.util.util import load_object

class PredicPipeline:
    def __init__(self):
        pass


class CustomData:
    def __init__(self,
                {age: int,
                sex: str,
                thyroxine: str,
                query_thyroxine: str,
                medication: str,
                sick: str,
                pregnant: str,
                surgery: str,
                I131_treatment: str,
                query_hypothyroid: str,
                query_hyperthyroid: str,
                lithium: str,
                goitre: str,
                tumor: str,
                hypopituitary: str,
                psych: str,
                TSH: float,
                T3: float,
                TT4: float,
                T4U: float,
                FTI: float,
                referral_source: str,
                outcome: int}
                )
                        
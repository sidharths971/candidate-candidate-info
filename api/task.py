from flask_restful import Resource
import pandas as pd
import json
import os


class Task(Resource):
    """
    @desc contains functions will consume candidate information from csv file and format the
    result based on the requirement and create candidate_info json file which holds all the
    result and return the response with same in '/candidate/candidate-details' url
    """

    def get(self):
        #--Read the candidate details from file 
        candidate_details = read_candidate_info(CandidateConstants.PATH)
        pry_key = list(candidate_details.keys())
        #-- create a base strature for out put file
        strture = strature_of_candidate(candidate_details, pry_key)
        #--create the proper out put in dictionary file
        candidate_info_result = format_response(candidate_details, strture, pry_key)
        #--If file not present it will create and store in file
        if CandidateConstants.CANDIDATE_RESULT not in os.listdir():
            with open(CandidateConstants.CANDIDATE_RESULT, 'w') as f:
                json.dump(candidate_info_result, f, indent=4)

        return candidate_info_result, 200


def read_candidate_info(path: str):
    """
    @desc Take absolute path of csv file and fill the missing values and return the dictionary
    format candidate information
    :param path: str
    :return: dict
    """
    candidate_info_df = pd.read_csv(path)
    #--fill the missing values with 0
    candidate_info_df.fillna(0, inplace=True)
    candidate_dic_info = candidate_info_df.to_dict(orient='index')

    return candidate_dic_info


def strature_of_candidate(dic, pry_key):
    """
    @desc Take the dictionary format candidate data and create primary strature of the candidate
    :param dic: dict
    :param pry_key: list
    :return: dict
    """
    strature = {}
    candidate_data = dic[pry_key[0]]
    #-- create basic strature for the every product from the converted dictinary
    strature[list(dic[pry_key[0]].keys())[1].split()[0]] = candidate_data.get(list(dic[pry_key[0]].keys())[1], 0)
    strature[list(dic[pry_key[0]].keys())[2].split()[-1]] = candidate_data.get(list(dic[pry_key[0]].keys())[2], 0)
    strature[list(dic[pry_key[0]].keys())[3].split()[-1]] = candidate_data.get(list(dic[pry_key[0]].keys())[3], 0)
    strature[CandidateConstants.CHILDREN] = []

    return strature


def format_response(dic, strature, pry_key):
    """
    @desc Take dictnary format candidate information and primary strature and format the all candidate
    informatin based on the requirement and return the same
    :param dic: dict
    :param strature: dict
    :param pry_key: list
    :return: dict
    """
    count = 0
    for x in range(1, len(pry_key)):
        #--If the value is 0 skip the line of execution.
        if dic[x][list(dic[x].keys())[1]] == 0:
            continue
        #--Compaire the last element of dictionary and add key value in dictionary
        elif dic[x][list(dic[x].keys())[-1]] == 0:
            strature[CandidateConstants.CHILDREN].append({
            list(dic[x].keys())[1].split()[0]: dic[x][list(dic[x].keys())[4]],
            list(dic[x].keys())[2].split()[-1]: dic[x][list(dic[x].keys())[5]],
            list(dic[x].keys())[3].split()[-1]: dic[x][list(dic[x].keys())[6]],
            CandidateConstants.CHILDREN: []
            })
            count += 1
        #--Otherwise add the element in appropriate data in dictionary
        else:
            strature[CandidateConstants.CHILDREN][count-1][CandidateConstants.CHILDREN].append({
            list(dic[x].keys())[1].split()[0]: dic[x][list(dic[x].keys())[7]],
            list(dic[x].keys())[2].split()[-1]: dic[x][list(dic[x].keys())[8]],
            list(dic[x].keys())[3].split()[-1]: dic[x][list(dic[x].keys())[9]],
            CandidateConstants.CHILDREN: []
            })

    return strature


#--This is the helper class 
class CandidateConstants:
    PATH = 'candidate-informations/data - external candidates.csv'
    CANDIDATE_RESULT = 'candidate_info.json'
    CHILDREN = 'children'
    BASE_FILE = 'candidate-informations'
    MESSAGE = 'File uploaded successfully, the json format data you can check in candidate_info.json ' \
              'file in project directory level or you can check in API in' \
              ' "http://127.0.0.1:8000/candidate/candidate-details"'

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
        candidate_details = read_candidate_info(CandidateConstants.PATH)
        pry_key = list(candidate_details.keys())
        strture = strature_of_candidate(candidate_details, pry_key)
        candidate_info_result = format_response(candidate_details, strture, pry_key)
        if CandidateConstants.CANDIDATE_RESULT not in os.listdir():
            with open(CandidateConstants.CANDIDATE_RESULT, 'w') as f:
                json.dump(candidate_info_result, f, indent=4)

        return candidate_info_result, 200


def read_candidate_info(path: str):
    candidate_info_df = pd.read_csv(path)
    candidate_info_df.fillna(0, inplace=True)
    candidate_dic_info = candidate_info_df.to_dict(orient='index')

    return candidate_dic_info


def strature_of_candidate(dic, pry_key):
 strature = {}
 candidate_data = dic[pry_key[0]]
 strature[list(dic[pry_key[0]].keys())[1].split()[0]] = candidate_data.get(list(dic[pry_key[0]].keys())[1], 0)
 strature[list(dic[pry_key[0]].keys())[2].split()[-1]] = candidate_data.get(list(dic[pry_key[0]].keys())[2], 0)
 strature[list(dic[pry_key[0]].keys())[3].split()[-1]] = candidate_data.get(list(dic[pry_key[0]].keys())[3], 0)
 strature[CandidateConstants.CHILDREN] = []

 return strature


def format_response(dic, strature, pry_key):
 count = 0
 for x in range(1, len(pry_key)):
  if dic[x][list(dic[x].keys())[1]] == 0:
   continue
  elif dic[x][list(dic[x].keys())[-1]] == 0:
   strature[CandidateConstants.CHILDREN].append({
    list(dic[x].keys())[1].split()[0]: dic[x][list(dic[x].keys())[4]],
    list(dic[x].keys())[2].split()[-1]: dic[x][list(dic[x].keys())[5]],
    list(dic[x].keys())[3].split()[-1]: dic[x][list(dic[x].keys())[6]],
    CandidateConstants.CHILDREN: []
   })
   count += 1
  else:
   strature[CandidateConstants.CHILDREN][count-1][CandidateConstants.CHILDREN].append({
    list(dic[x].keys())[1].split()[0]: dic[x][list(dic[x].keys())[7]],
    list(dic[x].keys())[2].split()[-1]: dic[x][list(dic[x].keys())[8]],
    list(dic[x].keys())[3].split()[-1]: dic[x][list(dic[x].keys())[9]],
    CandidateConstants.CHILDREN: []
   })

 return strature


class CandidateConstants:
    PATH = 'candidate-informations/data - external candidates.csv'
    CANDIDATE_RESULT = 'candidate_info.json'
    CHILDREN = 'children'
    BASE_FILE = 'candidate-informations'
    MESSAGE = 'File uploaded successfully, the json format data you can check in candidate_info.json ' \
              'file in project directory level'

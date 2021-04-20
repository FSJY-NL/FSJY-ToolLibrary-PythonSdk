from enum import Enum

import pandas as pd
import requests


# todo: add log
# todo: add exception handling
# todo: add documentation
# todo: CI
# todo: setting in github page

class RunStatus(Enum) :
	NO_FILE = 0
	READY = 10
	STARTED = 20
	END = 30
	ERROR = 100


class ToolLib :
	mainUrl = 'https://ffquant-toollibrary-engine.azurewebsites.net'
	
	def __init__(self, username: str, password: str) :
		url = self.mainUrl + '/token'
		values = {
				'username' : username,
				'password' : password,
				}
		
		r = requests.post(url, data=values)
		if r.status_code != 200 :
			raise Exception(f"Login ERROR, status code: {r.status_code}")
		
		self.headers = {"Authorization" : "Bearer " + r.json()["access_token"]}
	
	# return a list of string
	def GetAvailableToolList(self) -> list :
		url = self.mainUrl + '/tools'
		r = requests.get(url, headers=self.headers)
		if r.status_code != 200 :
			print(f" ERROR, status code: {r.status_code}")
			return {}
		
		return r.json()
	
	# getUser
	def GetMyInfo(self) -> dict :
		url = self.mainUrl + '/users/me'
		r = requests.get(url, headers=self.headers)
		if r.status_code != 200 :
			print(f" ERROR, status code: {r.status_code}")
			return {}
		
		return r.json()
	
	# can input dictionary<string,dataframe> or a dataframe
	# return json as a dict format
	def Run(self, toolname: str, data, runUntil: RunStatus = RunStatus.END.value, runId: str = None) -> dict :
		try :
			# wrap into the format for the communication
			if type(data) is dict :
				input = {}
				for key, value in data.items() :
					if type(value) is pd.DataFrame :
						input[key] = value.to_dict('records')
					elif type(value) is list :
						input[key] = value
			
			elif type(data) is pd.DataFrame :
				input = {"Input" : data.to_dict('records')}
			else :
				raise Exception("invalid input format for data allowed types: dict<string,dataframe> or datafrmae")
			
			
			
			# "RunIdentifier": f"{toolname}_timestamp if runId is None else runId
			requestDict = {"InputJson" : input, "AppName" : toolname, "RunUntil" : runUntil}
			
			url = self.mainUrl + '/api/v1/inputs'
			
			r = requests.post(url, json=requestDict, headers=self.headers)
			
			if r.status_code != 200 :
				print(f" ERROR, status code: {r.status_code} + {r.error}")
				return {}
			
			return r.json()
		
		except Exception as e :
			print(f"error: {e}")
			return {}

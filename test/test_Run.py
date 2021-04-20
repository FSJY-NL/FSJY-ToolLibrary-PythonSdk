import json
import pathlib
import pandas as pd
from src.ToolLib import ToolLib


# user need to pass in dict with keys like "Input" and list <dict>
def test_Run_Dummy_dict() :
	input = {"Input" : [{'1' : 1}]}
	
	info = ToolLib("johndoe", "secret").Run("Dummy", input)
	
	assert info["message"] == 'Get Result Done'
	assert info["data"]["1"] == {'0' : 1}


# user need to pass in dict with keys like "Input" and dataframe, suitable for multiple dataframe input
def test_Run_Dummy_dict_df() :
	d = {'col1' : [1, 2], 'col2' : [3, 4]}
	df = pd.DataFrame(data=d)
	
	input = {"Input" : df}
	
	info = ToolLib("johndoe", "secret").Run("Dummy", input)
	
	assert info["message"] == 'Get Result Done'
	assert info["data"]["1"] == {'0' : 1}


# user just pass in one dataframe, suitable for one dataframe input
def test_Run_Dummy_dataframe() :
	d = {'col1' : [1, 2], 'col2' : [3, 4]}
	df = pd.DataFrame(data=d)
	
	info = ToolLib("johndoe", "secret").Run("Dummy", df)
	
	assert info["message"] == 'Get Result Done'
	assert info["data"]["1"] == {'0' : 1}


# user just pass in one dataframe, suitable for one dataframe input
def test_Run_SME() :
	testInput = {}
	for tag in ["Data", "Definition"] :
		with open(str(pathlib.Path(__file__).parent.joinpath("TestData").joinpath("SMECredit_" + tag + ".json")), "r") as file :
			testInput[tag] = json.load(file)  # json load() return  an array with single object inside
	
	info = ToolLib("johndoe", "secret").Run("SMECredit", testInput)
	
	assert info["message"] == 'Get Result Done'
	assert info["data"]["1"] == {'0' : 1}


# user just pass in one dataframe, suitable for one dataframe input
def test_Run_FRTBSASBM() :
	testInput = {}
	for tag in ["Input"] :
		with open(str(pathlib.Path(__file__).parent.joinpath("TestData").joinpath("FrtbSaSbm_" + tag + ".json")), "r") as file :
			testInput[tag] = json.load(file)  # json load() return  an array with single object inside
	
	info = ToolLib("johndoe", "secret").Run("FrtbSaSbm", testInput)
	
	assert info["message"] == 'Get Result Done'
	assert info["data"]["CSRNonCTP"]["Delta"]["medium"] == 36.1022932897



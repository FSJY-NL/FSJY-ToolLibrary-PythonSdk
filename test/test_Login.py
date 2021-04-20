import pytest
from src.ToolLib import ToolLib


def test_login_only() :
	tool= ToolLib("johndoe",  "secret")
	

def test_login_incorrect():
	with pytest.raises(Exception) :
		tool = ToolLib("wrong", "wrong")
	
	
def test_GetUser() :
	tool =ToolLib("johndoe",  "secret")
	info=tool.GetMyInfo()

	assert info["company"]=="J.D.Limited"
	
def test_GetAllowedTools() :
	tool =ToolLib("johndoe",  "secret")
	info=tool.GetAvailableToolList()

	assert 'Dummy' in info["validTools"]



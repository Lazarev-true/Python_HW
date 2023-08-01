import pytest
from Task_5 import Project
from exceptions import NotAllowedError

@pytest.fixture
def project():
    project = Project()
    project.fill_project_users()
    return Project()

def test_add_user(project):
    project.add_user('Поля', 193, 3)
    assert 123 in project.user_dict
    assert project.user_dict[123].name == 'Поля'
    assert project.user_dict[123].level == 3

def test_del_user(project):
    project.del_user('Антон', 567, 3)
    assert 123 not in project.user_dict

def test_enter_not_allowed(project):
    with pytest.raises(NotAllowedError):
        project.enter('Константин', 709)

        
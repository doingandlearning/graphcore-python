from company import Programmer


def test_programmer_can_add_skill_with_level():
    emp = Programmer("Person", 12000)
    emp.addSkill("Python", 1)

    assert emp.getSkillLevel("Python") == 1


def test_programmer_can_improve_skill():
    emp = Programmer("Person", 12000)
    emp.addSkill("Python", 1)
    emp.improveSkill("Python", 4)

    assert emp.getSkillLevel("Python") == 4


def test_programmer_cannot_improve_non_existent_skill():
    emp = Programmer("Person", 12000)
    emp.improveSkill("Python", 4)

    assert not emp.getSkillLevel("Python")

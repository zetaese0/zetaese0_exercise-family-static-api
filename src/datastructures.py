
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [{"id": self._generateId(),
                          "first_name": "John",
                          "last_name": self.last_name,
                          "age": 33,
                          "lucky_numbers": [7, 1, 12]},
                          {"id": self._generateId(),
                          "first_name": "Jane",
                          "last_name": self.last_name,
                          "age": 35,
                          "lucky_numbers": [10, 14, 3]},
                          {"id": self._generateId(),
                          "first_name": "Jimmy",
                          "last_name": self.last_name,
                          "age": 5,
                          "lucky_numbers": [1]}]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        member["id"] = self._generateId()
        member["last_name"] = self.last_name
        self._members.append(member)

    def delete_member(self, id):
        for index, member in enumerate(self._members):
            if id == member["id"]:
                del self._members[index]
                return True
        return False

    def get_member(self, id):
        if {"first_name", "age", "lucky_numbers", "id", "last_name"}.issubset(update.keys()):
            for index, member in enumerate(self._members):
                if member["id"] == id:
                    self._members[index] = update
                    return self._members[index] 
            return "Error2"
        return "Error1"


    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

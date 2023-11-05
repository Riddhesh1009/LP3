// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract StudentData {
    // Define a Student structure
    struct Student {
        string name;
        uint age;
        string course;
    }

    // Array to store Student structs
    Student[] public students;

    // Fallback function to handle unknown function calls
    fallback() external {}

    // Receive function to accept Ether
    receive() external payable {}

    // Function to add a new student
    function addStudent(string memory _name, uint _age, string memory _course) public {
        Student memory newStudent = Student(_name, _age, _course);
        students.push(newStudent);
    }

    // Function to get the total number of students
    function getTotalStudents() public view returns (uint) {
        return students.length;
    }
}
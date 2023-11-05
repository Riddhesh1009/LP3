// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

contract BankAccount {
    // The address of the account owner
    address public owner;
    
    // Constructor to set the owner of the account
    constructor() {
        owner = msg.sender;
    }

    // Modifier to check if the caller is the owner of the account
    modifier isOwner() {
        require(msg.sender == owner, "You are not the owner");
        _;
    }

    // Function to deposit money into the account
    function depositMoney() public payable isOwner {
        require(msg.value > 0, "Deposit amount should be greater than zero");
    }

    // Function to withdraw money from the account
    function withdrawMoney(uint amount) public isOwner {
        require(address(this).balance >= amount, "Insufficient balance");
        payable(owner).transfer(amount);
    }

    // Function to get the account balance
    function showBalance() public view isOwner returns (uint) {
        return address(this).balance;
    }
}
pragma solidity ^0.8.0;

contract FitonAiInvestmentFund {
    address public manager;
    mapping(address => uint) public investors;
    
    constructor() {
        manager = msg.sender;
    }
    
    function invest() public payable {
        require(msg.value > 0.01 ether);
        investors[msg.sender] += msg.value;
    }
    
    function getBalance() public view returns(uint) {
        return address(this).balance;
    }
    
    function withdraw(uint amount) public {
        require(msg.sender == manager);
        payable(manager).transfer(amount);
    }
}


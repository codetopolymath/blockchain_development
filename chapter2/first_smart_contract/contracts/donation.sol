
pragma solidity ^0.5.0; 

contract Donation {
    address public donatur;
    address public donatee;
    uint public money;
    string public useless_variable;

    constructor() public {
        donatee = msg.sender;
        useless_variable = "Donation String";
    }

    function change_useless_variable(string memory param) public {
        useless_variable = params; 
    }

    function donate() public payable {
        donatur = msg.sender;
        money = msg.value;
    }

    function receive_donation() public {
        donatee.transfer.(address(this).balance);
    }
}




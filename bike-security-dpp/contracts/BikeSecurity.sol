// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BikeSecurity {

    // EVENTS

    event UserRegistered(string phone);
    event UserLoggedIn(string phone);
    event SensorTriggered(string phone);


    // USER STRUCTURE

    struct User {
        string phone;
        bool registered;
    }


    // USER STORAGE

    mapping(string => User) public users;


    // REGISTER USER

    function registerUser(string memory phone) public {

        require(!users[phone].registered, "User already registered");

        users[phone] = User(phone, true);

        emit UserRegistered(phone);
    }


    // LOGIN USER

    function loginUser(string memory phone) public {

        require(users[phone].registered, "User not registered");

        emit UserLoggedIn(phone);
    }


    // SENSOR TRIGGER FUNCTION (PAYABLE)

    function triggerSensor(string memory phone) public payable {

        require(users[phone].registered, "User not registered");

        emit SensorTriggered(phone);
    }

}
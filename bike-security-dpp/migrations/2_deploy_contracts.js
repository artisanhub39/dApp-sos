const BikeSecurity = artifacts.require("BikeSecurity");

module.exports = function (deployer) {
  deployer.deploy(BikeSecurity);
};
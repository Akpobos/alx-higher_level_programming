#!/usr/bin/node
exports.addMeMaybe = function (num, cb) {
    const nNum = num + 1;
    cb(nNum);
};

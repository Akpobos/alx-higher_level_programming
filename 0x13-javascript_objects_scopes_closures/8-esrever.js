#!/usr/bin/node
exports.esrever = function (list) {
    return (
      list.reduceRight(
        function (accumulator, currentValue) {
          return accumulator.concat(currentValue);
        }, [])
    );
};

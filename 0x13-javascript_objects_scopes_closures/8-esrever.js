#!/usr/bin/node
exports.esrever = function (list) {
  const rev = [];
  for (let i = 0; i < list.length; i++) {
    rev.push(list[i]);
  }
  return rev;
};

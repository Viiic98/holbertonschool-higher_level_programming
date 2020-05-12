#!/usr/bin/node
exports.esrever = function (list) {
  let i = list.length - 1;
  const revList = [];
  while (i >= 0) {
    revList.push(list[i]);
    i--;
  }
  return (revList);
};

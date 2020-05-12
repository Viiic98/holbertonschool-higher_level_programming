#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
for (const key in dict) {
  const userId = String(dict[key]);
  if (!newDict[userId]) {
    newDict[userId] = [key];
  } else {
    newDict[userId].push(key);
  }
}
console.log(newDict);

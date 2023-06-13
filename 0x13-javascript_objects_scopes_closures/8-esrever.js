#!/usr/bin/node

exports.esrever = function (list) {
  const idx = list.length();
  let revList = [];
  for (let i = idx; i > 0; i--) {
    revList.push(list[i]);
  }
  console.log(revList);
};

#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let res = 0;

  for (const el of list) {
    if (el === searchElement) {
      res++;
    }
  }

  return res;
};

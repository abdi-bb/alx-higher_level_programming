#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, res, bod) => {
  if (!err) {
    const completedTasks = {};
    bod = JSON.parse(bod);

    for (let i = 0; i < bod.length; ++i) {
      const userId = bod[i].userId;
      const completed = bod[i].completed;

      if (completed && !completedTasks[userId]) {
        completedTasks[userId] = 0;
      }

      if (completed) ++completedTasks[userId];
    }

    console.log(completedTasks);
  }
});

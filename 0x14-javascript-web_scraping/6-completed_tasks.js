#!/usr/bin/node

const request = require('request');

const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error('Error:', err.message);
    return;
  }

  try {
    const completedTasks = {};
    const data = JSON.parse(body);

    for (let i = 0; i < data.length; ++i) {
      const userId = data[i].userId;
      const completed = data[i].completed;

      if (completed && !completedTasks[userId]) {
        completedTasks[userId] = 0;
      }

      if (completed) ++completedTasks[userId];
    }

    console.log(completedTasks);
  } catch (error) {
    console.error('Error parsing JSON response:', error.message);
  }
});

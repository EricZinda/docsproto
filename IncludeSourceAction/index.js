const core = require('@actions/core');
const github = require('@actions/github');
const fs = require('fs');

try {
    console.log(`Test`);
    // Parse the input file and loop through all of the repositories
    const pathToFile = core.getInput('definition-file');


    // Read users.json file
    fs.readFile(pathToFile, function(err, data) {
        // Check for errors
        if (err) throw err;

        // Converting to JSON
        const data = JSON.parse(data);

        console.log(data); // Print users
    });
//
//  // `who-to-greet` input defined in action metadata file
//  console.log(`Hello ${nameToGreet}!`);
//  const time = (new Date()).toTimeString();
//  core.setOutput("time", time);
//  // Get the JSON webhook payload for the event that triggered the workflow
//  const payload = JSON.stringify(github.context.payload, undefined, 2)
//  console.log(`The event payload: ${payload}`);
} catch (error) {
  core.setFailed(error.message);
}
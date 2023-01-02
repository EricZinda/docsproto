const core = require('@actions/core');
const github = require('@actions/github');
const fs = require("fs");
const lunr = require('lunr')

const pathToFile = core.getInput('json-data-file-path');
const indexFile = core.getInput('index-file-path');

fs.readFile(pathToFile, "utf8", (err, jsonString) => {
    if (err) {
        console.log("Error reading file from disk:", err);
        return;
    }

    try {
        const documents = JSON.parse(jsonString);

        var idx = lunr(function () {
            this.ref('link')
            this.field('body')

            documents.forEach(function (doc) {
                console.log(`Link processed: ${doc.link}`)
                this.add(doc)
            }, this);
        });

        console.log(`Serializing index...`)
        const content = JSON.stringify(idx);
        fs.writeFile(indexFile, content, err => {
            if (err) {
                console.error(err);
            }
            else {
                console.log(`Done.`)
            }
        });
    } catch (err) {
        console.log("Error parsing JSON string:", err);
    }
});

//
//try {
//  // `who-to-greet` input defined in action metadata file
//  console.log(`Hello ${nameToGreet}!`);
//  const time = (new Date()).toTimeString();
//  core.setOutput("time", time);
//  // Get the JSON webhook payload for the event that triggered the workflow
//  const payload = JSON.stringify(github.context.payload, undefined, 2)
//  console.log(`The event payload: ${payload}`);
//} catch (error) {
//  core.setFailed(error.message);
//}
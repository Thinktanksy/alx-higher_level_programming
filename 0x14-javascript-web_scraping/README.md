0x14-javascript-web_scraping

This repository contains JavaScript scripts for web scraping, which allows you to extract data from web pages using Node.js and various libraries.
Getting Started

To use these scripts, you need to have Node.js and npm (Node Package Manager) installed on your system.
Prerequisites

    Node.js
    npm (usually comes with Node.js installation)

Setup

    Clone this repository to your local machine:

bash

git clone https://github.com/your_username/0x14-javascript-web_scraping.git

    Navigate to the project directory:

bash

cd 0x14-javascript-web_scraping

    Install the required dependencies:

bash

npm install

Available Scripts

The following JavaScript scripts are available in this repository:

    0-readme.js: A script to read and print the content of a file.

    1-writeme.js: A script to write a specified string to a file.

    2-statuscode.js: A script to display the status code of a GET request to a specified URL.

    3-starwars_title.js: A script to fetch the title of a Star Wars movie by its episode number from the Star Wars API (SWAPI).

    4-starwars_count.js: A script to count the number of films where a specific character appeared using the Star Wars API (SWAPI).

    5-request_store.js: A script to get the contents of a webpage and save it to a file.

    6-completed_tasks.js: A script to compute the number of tasks completed by each user from a given API and display the result.

How to Run

To execute any of the JavaScript scripts, use the node command followed by the script filename.

Example:

bash

node 0-readme.js

This will run the 0-readme.js script, which reads and prints the content of a file.
Dependencies

The following Node.js libraries are used in the scripts:

    axios: Used for making HTTP requests to APIs and web pages.
    fs: The built-in Node.js File System module, used for file operations.

These dependencies are installed when you run npm install as mentioned in the setup section.

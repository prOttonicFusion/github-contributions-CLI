# GitHub Contributions CLI
A command line tool for keeping track of your daily contributions count on GitHub

<p align="left">
  <img src="assets/sample-output.png" width="210px" alt="Sample output"/>
</p>

## Setup (Optional)
To be able to call the script without specifying your GitHub username every time, add it to the `config.ini`.

## Usage
If the configuration file has been set up as described above, the script works by simply running
```
python3 githubContributions.py
```
By default, contributions are shown for the last week. This can be modified by using either 
```
python3 githubContributions.py -N 15
```
to print out the last 15 days or
```
python3 githubContributions.py -t 
```
to check today's stats.

To get more info about usage, run the script with the `-h` flag. If the output looks odd, try changing the progress bar symbol in `config.ini` or using the command line flag `-m`. 

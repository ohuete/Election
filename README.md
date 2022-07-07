# Election Analysis
## Overview of Election Audit
### Purpose and Background
Tom and his manager Seth are employees at the Colorado Board of Elections. They have asked me to complete the election audit of a recent local congressional election using Python. The tasks are as follows: 
1. Calculate the total number of votes cast.
2. Get a complete list of counties that received votes.
3. Calculate the total number of votes for each candidate.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote. 
6. Calculate voter turnout for each county.
7. Based on total number of votes, calculate total votes from each county.
8. Determine the county with largest voter turnout.
### Resources
- Data Source: election_results.csv
- Software: Python 3.10.5, Visual Studio Code, 1.68.1
## Election Audit Results
The election analysis shows:
* **Total votes**: 369,711
* **Counties and their results**:
  * Jefferson received 10.5% of votes with a total number of 38,855 votes.
  * Denver received 82.8% of votes with a total number of 306,055 votes.
  * Arapahoe received 6.7% of votes with a total number of 24,801 votes.
* **County with largest voter turnout**:
  * Denver who received 82.8% of votes with a total number of 306,055 votes.
* **Candidate results**:
  * Charles Casper Stockham received 23% of votes with a total number of 85,213 votes.
  * Diana Degette received 73.8% of votes with a total number of 272,892 votes.
  * Raymon Anthony Doane received 3.1% of votes with a total number of 11,606 votes. 
* **Winner of the election was**:
  *  Diana Degette who received 73.8% of votes with a total number of 272,892 votes.

This data can be found in the output file of the election analysis (shown below):

![Election_Analysis_Output](https://user-images.githubusercontent.com/107595127/177875351-8f6b7d01-8d16-4234-938a-b84d0c0c4d70.png)

## Election Audit Summary
To the Election Commission,

I was assigned this task by members of the Colorado Board of Elections to generate election results for their local election. The script provided worked perfectly for their needs. With a few modifications, the present script can be applied to other local elections or even large scale national elections. To operate, the present script reads and analyzes a given * *csv* * file that contains election and voting data. It is programmed to generate lists for candidates and counties then dictionaries to store values (such as voting results). The decision statements in the script help determine the exact values you may be looking for, such as: number of votes, percentages, winner, etc. 

To modify for larger scale elections, you would include state data and perhaps even the data for counties within the states. If so, a "nested" loop with decision statements would be used to include this data. To do this, you loop through all counties in one state before it moves on and does the same for the next state. Then we have to account for electoral college, in which you could use if statements to determine values that would grant an electoral college vote. 

Similarly, to add more specific details like demographic, party affiliation, or perosnal demographic data, this would have to be included in the original * *csv* * file. A "for" loop that counts votes for these specific catagories can be included in the script that would then generate the outcom onto the output text file. "If" statements could then determine and generate final results for each category. 

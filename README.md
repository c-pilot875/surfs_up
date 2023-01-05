# Surfs_up Temperature Analysis

## Overview of Project
Performing a comparison analysis on Oahu temperatures during months of June and December. asqlalchemy was used with pandas to extract June and December temperatures from the hawaii.sqlite file. A session.query was created to first extract the table, columns, and filter the date column to only June or December. The values pulled were then put into a list to display in a pandas data frame. Summaries for both months were pulled using df.describe() to display average, min, and max temperatures.

### Languages and Programs
SQL Lite, sqlachemy, pandas

## Key differences between June and December Temperatures
* Temperatures in June averaged almost 75 degrees
<img width="156" alt="Screen Shot 2023-01-05 at 3 58 04 PM" src="https://user-images.githubusercontent.com/115188500/210878765-16529a4f-1d73-44e4-9e41-ecede6f6d643.png">

* Temperatures in December averaged around 71 degrees
<img width="152" alt="Screen Shot 2023-01-05 at 3 58 15 PM" src="https://user-images.githubusercontent.com/115188500/210878800-b6fd3449-587e-42bb-97de-bd9474029f9e.png">

* The minimum temperature for December was aroun 54 degrees while June's minimum was 64 degrees. 
---
## Suggestions

For business purposes June would be the ideal month to operate the business since the temperatures remained in the upper 70's for most of the month of June.

---

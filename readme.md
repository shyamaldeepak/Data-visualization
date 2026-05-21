# Video Game Sales Project Documentation

This document contains the project documentation that fulfills the rubric requirements, as well as the PowerPoint Presentation outline structured for a 5-member team.

---

## Part 1: Project Report Content

### 1. Introduction
* **What is the subject and context of the project?**
  This project analyzes the historical global sales of video games. The context is to understand market dynamics, consumer preferences, and industry evolution by examining how factors like genre, platform, and region influence commercial success.
* **What is the source of the data?**
  The data is sourced from Kaggle's "Video Game Sales" dataset.
* **Who collected the data?**
  The dataset was originally scraped and compiled by Kaggle user GregorySmith, using data from VGChartz.com.
* **When was the data collected?**
  The dataset was collected and published in October 2016.
* **How was the data collected?**
  It was collected via web scraping using Python (specifically BeautifulSoup) to extract the data from the VGChartz website.
* **In what context/for what purpose was the data collected?**
  The data was collected to provide a comprehensive, publicly accessible dataset for data scientists and analysts to practice data visualization and uncover trends in the global gaming industry.
* **What does the dataset contain?**
  The dataset contains 11 columns tracking game attributes and sales. 
  * *Categorical Data:* `Name`, `Platform`, `Genre`, `Publisher`
  * *Continuous/Numerical Data:* `Rank`, `Year`, `NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`, `Global_Sales` (Sales are in millions of units).
* **What is the size of the dataset?**
  The dataset contains 16,598 rows (video games) and 11 columns.
* **What is the dataset's license?**
  It is released under the CC0: Public Domain license, meaning it is free for anyone to use without restriction.

### 2. Project Question & Hypotheses
* **Main Research Question:** How do genre, platform, and publisher influence the global and regional sales performance of video games over time?
  * *Context:* This main question encompasses the geographical distribution of sales, the performance of different platforms and publishers, the evolution of sales over time, and the market share of various genres, providing a holistic view of the global video game industry.
* **Sub-questions:**
  1. **Trend Analysis:** How have total global video game sales trended year over year from the start of the dataset to the most recent year?
  2. **Genre Popularity by Region:** Which video game genres have generated the highest total global sales, and how do these genre preferences differ between North America (NA_Sales), Europe (EU_Sales), and Japan (JP_Sales)?
  3. **Platform Dominance:** What are the top 10 most successful gaming platforms of all time based on total global sales? 
  4. **Publisher Market Share:** Which publishers dominate the top 100 best-selling games of all time, and what percentage of total global sales do they account for?
  5. **Regional Market Sizes:** How do the total market sizes (total sales) of North America, Europe, Japan, and "Other" regions compare to one another across the entire dataset?
  6. **Platform Lifespan & Success:** For the top 3 most successful platforms (e.g., PS2, X360, Wii), how are their sales distributed across their active years? 
  7. **Average Sales per Game:** While some genres or platforms have high total sales because of a massive number of releases, which genres and platforms have the highest *average* global sales per game?
  8. **Decade Comparison:** How has the market share of the top 5 genres evolved from the 1990s to the 2000s, and then to the 2010s?
  9. **The "Other" Market:** Which specific publishers and game genres perform the strongest in the "Other_Sales" category?
  10. **Concentration of Sales:** What percentage of all global video game sales is captured by the top 1% of games (based on Rank) compared to the bottom 50%?
* **Do your sub-questions allow you to answer your main research question?**
  Yes. By breaking down "commercial success" into categories (genres/platforms) and environments (time/region), we can build a comprehensive understanding of what drives sales.
* **Do you have the data to answer your sub-questions?**
  Yes, the dataset contains specific columns for Genre, Platform, Year, and regional sales (NA, EU, JP, Other) to support this analysis.
* **What are your hypotheses?**
  * *Hypothesis 1:* Action and Sports games will have the highest total sales due to their broad demographic appeal.
  * *Hypothesis 2:* North America will be the largest contributing region to global sales.
  * *Hypothesis 3:* Sales will show a massive peak between 2006-2010 due to the success of the Nintendo Wii and PlayStation 3.

### 3. Analysis of Sub-Questions

#### Sub-Question 1 Analysis: Categorical Factors (Genre & Platform)
* **Relevance:** Understanding which genres and platforms sell the most is crucial for developers deciding what kind of game to make and where to release it.
* **Methodology:** We use data aggregation (grouping by Genre and Platform) to sum up global sales. 
* **Analysis & Results:** 
  * The bar charts reveal that **Action** and **Sports** are the dominant genres, confirming our first hypothesis. 
  * For platforms, the **PS2** and **X360** lead in historical sales. This represents an era where gaming went mainstream. 
* **Limitations:** The data only goes up to 2016, so it entirely misses modern platforms like the PS5, Xbox Series X, and Nintendo Switch, creating a recency bias.

#### Sub-Question 2 Analysis: Temporal and Regional Factors
* **Relevance:** Identifying the "golden age" of gaming and understanding regional market shares helps publishers target marketing campaigns.
* **Methodology:** We aggregate sales across the `Year` column to create a time-series line chart, and we sum regional sales columns to create a comparative composition chart.
* **Analysis & Results:**
  * **Temporal:** Video game sales peaked steeply around 2008-2009. This perfectly aligns with the height of the PS3, Xbox 360, and Wii console generation, confirming our hypothesis. Sales taper off near 2016 because the dataset is incomplete for recent years.
  * **Regional:** North America (NA_Sales) accounts for nearly 50% of total global sales, proving the second hypothesis. Europe is the second largest market.
* **Limitations:** Regional data combines many distinct countries into broad categories ("EU" or "Other"), hiding local nuances. Also, digital sales became dominant after 2010, but VGChartz mostly tracks physical box sales, meaning the "drop" in later years is artificially exaggerated.

### 4. Conclusions
* **Main Findings:** Action and Sports games are the most reliable genres for high sales. North America is the dominant consumer market, and the PS2/Wii era (2008-2010) represents the historical peak of physical game sales. Furthermore, a game's sales rank holds a strong negative correlation with global sales (a lower rank number = exponentially higher sales).
* **Does your analysis answer the research question?** Yes. We successfully identified that genre selection, platform choice, and regional targeting are massive drivers of a game's commercial success.
* **Limitations and Biases:** The methodology suffers from survivor bias (only games that sold enough to be tracked are included) and physical media bias (digital sales are heavily underreported). 
* **Sources:** Our findings align with general industry consensus published by groups like NPD and Newzoo regarding the PS2's dominance and the NA market size.
* **Next Steps:** If we had more time, we would merge this dataset with a modern API (like IGDB or SteamSpy) to include data from 2017-2026 and track digital-only sales.
* **Other Methods:** We could use a Machine Learning regression model (e.g., Random Forest) to predict the exact `Global_Sales` of a new game based on its Genre, Platform, and Publisher.

---

## Part 2: PowerPoint Presentation Structure (10-15 mins)

Here is a proposed structure for your 5 team members. Each member takes one graph from the Jupyter notebook to explain. 

### **Member 1: Introduction & Genre Analysis**
* **Slide 1: Title Slide** (Project Name, Team Members)
* **Slide 2: Project Context & Data** (Briefly explain where the data is from, what it contains, and the main research question).
* **Slide 3: Graph 1 - Top Selling Genres**
  * *Visual:* Bar chart of Global Sales by Genre.
  * *Talking Points:* Explain methodology. Point out that Action and Sports dominate. Briefly discuss why (broad demographic appeal).

### **Member 2: Platform Dominance**
* **Slide 4: Graph 2 - Top Performing Platforms**
  * *Visual:* Bar chart of Global Sales by Platform.
  * *Talking Points:* Explain how platform availability drives success. Highlight the PS2, X360, and Wii. Mention that this reflects the 2000s console boom.

### **Member 3: Temporal Trends**
* **Slide 5: Graph 3 - Sales Over Time**
  * *Visual:* Line chart showing sales by Year.
  * *Talking Points:* Show the massive peak around 2008-2009. Explain that the drop after 2010 is largely due to the dataset missing *digital* sales (a key limitation of the data).

### **Member 4: Regional Market Share**
* **Slide 6: Graph 4 - Regional Contributions**
  * *Visual:* Pie chart or comparative bar chart of NA, EU, JP, and Other sales.
  * *Talking Points:* Confirm the hypothesis that North America is the dominant market (~50%). Explain the relevance for publishers planning marketing budgets.

### **Member 5: Correlation & Final Conclusions**
* **Slide 7: Graph 5 - Rank vs. Sales Relationship**
  * *Visual:* Scatter plot with trendline showing Rank vs. Global Sales.
  * *Talking Points:* Explain the correlation calculation (-0.42). Show that the absolute top 10 games sell exponentially more than the rest of the market.
* **Slide 8: Conclusion & Critical Thinking**
  * *Talking Points:* Summarize the 3 main takeaways. Discuss limitations (data ends in 2016, lacks digital sales). Suggest future machine learning steps.
* **Slide 9: Q&A**
  * *Talking Points:* Ask the audience questions to secure the "Asking questions to others" grade (e.g., "Do you think Action games still dominate today, or have mobile games changed the landscape?"). Open the floor to audience questions.

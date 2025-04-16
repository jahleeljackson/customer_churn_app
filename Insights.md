# Insights, Findings, and Data-Driven Recommendations - Customer Churn


### Overview
In this project, we explored a dataset of customers to see if there were any valuable insights to be derived with respect to a customer's likelihood to 'churn' (to leave our business). 

### Insights & Findings
**Average Monthly Cost:**
I began the analysis by comparing the average monthly costs of customers, grouped by whether they churned or not. Through this process, I found that churning customers paid, on average,`$13.42` more per month. This would come to be `$161.04` that customers pay *more* every year. See figure 1.1 below: \
![Average Monthly Cost - Bar](avg_monthly.png 'Average Monthly Cost, Does Churn & Doesn\'t Churn') \
*Figure 1.1* 

However, this statistic can be misleading of the **true cause of the churn** in our dataset. After further analysis, I found that the **type of contract** a particular customer was under to be the single biggest predictor of them leaving. More specifically, having a Month-to-Month contract as opposed to a One-Year or Two-Year contract. Month-to-Month contracts by nature have higher monthly charges, explaining the preceding figure of average monthly cost. View figures 1.2 and 1.3 below: \
![Churn Pie](churning_pie.png 'Contract Type % For Churning Customers') \
*Figure 1.2* \
![Non-Churn pie](nonchurning_pie.png 'Contract Type % For Churning Customers') \
*Figure 1.3*

This valuable insight gives me the confidence to make the following recommendation.

## Recommendation

As we saw in figures 1.2 & 1.3 above, most of our churning customers **(57.9%)** had a Month-to-Month contract. Perhaps more insightful is the negative, none of our non-churning customers had Month-to-Month contracts. Put differently, all customers with Month-to-Month contracts end up churning. \
I recommend that we either drastically decrease the monthly pricing of our Month-to-Month contracts or cease offering these contracts altogether. 

### Assumptions

Giving this recommendation, I am assuming Month-to-Month contracts themselvese to be offensive to customers in some way. This is the limit to how nuanced our findings may get given this dataset. For instance, it could be that the channel through which customers sign their respective Month-to-Month contracts is vastly more inconvenient than One-Year or Two-Year, explaining higher churn rates. 
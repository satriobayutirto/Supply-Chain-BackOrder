# Supply-Chain-BackOrder
In this project, we will look for target items that need to be backordered

Description:

• sku – Random ID for the product

• national_inv – Current inventory level for the part

• lead_time – Transit time for product (if available)

• in_transit_qty – Amount of product in transit from source

• forecast_3_month – Forecast sales for the next 3 months

• forecast_6_month – Forecast sales for the next 6 months

• forecast_9_month – Forecast sales for the next 9 months

• sales_3_month – Sales quantity for the prior 3 month time period

• sales_6_month – Sales quantity for the prior 6 month time period

• sales_9_month – Sales quantity for the prior 9 month time period

• min_bank – Minimum recommend amount to stock

• potential_issue – Source issue for part identified

• pieces_past_due – Parts overdue from source

• perf_6_month_avg – Source performance for prior 6 month period

• perf_12_month_avg – Source performance for prior 12 month period

• local_bo_qty – Amount of stock orders overdue

• deck_risk – Part risk flag

• oe_constraint – Part risk flag

• ppap_risk – Part risk flag

• stop_auto_buy – Part risk flag

• rev_stop – Part risk flag

• went_on_backorder – Product actually went on backorder.

## 1. EDA
• There is 1 empty row and the lead time column is 5.9 % empty. That row will be dropped and lead time missing value wll be imputed with knn

• There missing value in average performance as -99 %, that value will be replaced with mean performance with out that value

• The forcasting and sku column will be droped

• There multicol column and we will combine ti make feature engineering

• There high imbalance in data, 99% od data is no backorder

## 2. Machine Learning 
• Because its huge imbalance in data, make minimum target precission is 1% and recall(detection) 50%

• After split dataset, we will use SMOTHE(imbalance handle), Standarization, and Gridsearch(Automate tunning) with weight for recall value

• In this project we use RandomForestClassification and XGBoost for model learning

• After that we will find important column and testing the model using streamlit to see how users will use this model





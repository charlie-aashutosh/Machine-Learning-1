{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Dataset is downloaded from Kaggle. Link: https://www.kaggle.com/giripujar/hr-analytics"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from matplotlib import pyplot as plt\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>satisfaction_level</th>\n",
       "      <th>last_evaluation</th>\n",
       "      <th>number_project</th>\n",
       "      <th>average_montly_hours</th>\n",
       "      <th>time_spend_company</th>\n",
       "      <th>Work_accident</th>\n",
       "      <th>left</th>\n",
       "      <th>promotion_last_5years</th>\n",
       "      <th>Department</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.38</td>\n",
       "      <td>0.53</td>\n",
       "      <td>2</td>\n",
       "      <td>157</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.80</td>\n",
       "      <td>0.86</td>\n",
       "      <td>5</td>\n",
       "      <td>262</td>\n",
       "      <td>6</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>medium</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.11</td>\n",
       "      <td>0.88</td>\n",
       "      <td>7</td>\n",
       "      <td>272</td>\n",
       "      <td>4</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>medium</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.72</td>\n",
       "      <td>0.87</td>\n",
       "      <td>5</td>\n",
       "      <td>223</td>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.37</td>\n",
       "      <td>0.52</td>\n",
       "      <td>2</td>\n",
       "      <td>159</td>\n",
       "      <td>3</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>sales</td>\n",
       "      <td>low</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   satisfaction_level  last_evaluation  number_project  average_montly_hours  \\\n",
       "0                0.38             0.53               2                   157   \n",
       "1                0.80             0.86               5                   262   \n",
       "2                0.11             0.88               7                   272   \n",
       "3                0.72             0.87               5                   223   \n",
       "4                0.37             0.52               2                   159   \n",
       "\n",
       "   time_spend_company  Work_accident  left  promotion_last_5years Department  \\\n",
       "0                   3              0     1                      0      sales   \n",
       "1                   6              0     1                      0      sales   \n",
       "2                   4              0     1                      0      sales   \n",
       "3                   5              0     1                      0      sales   \n",
       "4                   3              0     1                      0      sales   \n",
       "\n",
       "   salary  \n",
       "0     low  \n",
       "1  medium  \n",
       "2  medium  \n",
       "3     low  \n",
       "4     low  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(\"HR_comma_sep.csv\")\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 style=\"color:purple\">Data exploration and visualization</h2>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(3571, 10)"
      ]
     },
     "execution_count": 73,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "left = df[df.left==1]\n",
    "left.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(11428, 10)"
      ]
     },
     "execution_count": 74,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "retained = df[df.left==0]\n",
    "retained.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Average numbers for all columns** "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>satisfaction_level</th>\n",
       "      <th>last_evaluation</th>\n",
       "      <th>number_project</th>\n",
       "      <th>average_montly_hours</th>\n",
       "      <th>time_spend_company</th>\n",
       "      <th>Work_accident</th>\n",
       "      <th>promotion_last_5years</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>left</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.666810</td>\n",
       "      <td>0.715473</td>\n",
       "      <td>3.786664</td>\n",
       "      <td>199.060203</td>\n",
       "      <td>3.380032</td>\n",
       "      <td>0.175009</td>\n",
       "      <td>0.026251</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.440098</td>\n",
       "      <td>0.718113</td>\n",
       "      <td>3.855503</td>\n",
       "      <td>207.419210</td>\n",
       "      <td>3.876505</td>\n",
       "      <td>0.047326</td>\n",
       "      <td>0.005321</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      satisfaction_level  last_evaluation  number_project  \\\n",
       "left                                                        \n",
       "0               0.666810         0.715473        3.786664   \n",
       "1               0.440098         0.718113        3.855503   \n",
       "\n",
       "      average_montly_hours  time_spend_company  Work_accident  \\\n",
       "left                                                            \n",
       "0               199.060203            3.380032       0.175009   \n",
       "1               207.419210            3.876505       0.047326   \n",
       "\n",
       "      promotion_last_5years  \n",
       "left                         \n",
       "0                  0.026251  \n",
       "1                  0.005321  "
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('left').mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From above table we can draw following conclusions,\n",
    "<ol>\n",
    "    <li>**Satisfaction Level**: Satisfaction level seems to be relatively low (0.44) in employees leaving the firm vs the retained ones (0.66)</li>\n",
    "    <li>**Average Monthly Hours**: Average monthly hours are higher in employees leaving the firm (199 vs 207)</li>\n",
    "    <li>**Promotion Last 5 Years**: Employees who are given promotion are likely to be retained at firm </li>\n",
    "</ol>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Impact of salary on employee retention**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1442bf3eda0>"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\nSUVORK5CYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x14429998240>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "pd.crosstab(df.salary,df.left).plot(kind='bar')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above bar chart shows employees with high salaries are likely to not leave the company"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Department wise employee retention rate**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x1442bf75128>"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\ngg==\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x1442bf7cba8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "pd.crosstab(df.Department,df.left).plot(kind='bar')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "From above chart there seem to be some impact of department on employee retention but it is not major hence we will ignore department in our analysis"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h3 style=\"color:purple\">From the data analysis so far we can conclude that we will use following variables as dependant variables in our model</h3>\n",
    "<ol>\n",
    "    <li>**Satisfaction Level**</li>\n",
    "    <li>**Average Monthly Hours**</li>\n",
    "    <li>**Promotion Last 5 Years**</li>\n",
    "    <li>**Salary**</li>\n",
    "</ol>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>satisfaction_level</th>\n",
       "      <th>average_montly_hours</th>\n",
       "      <th>promotion_last_5years</th>\n",
       "      <th>salary</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.38</td>\n",
       "      <td>157</td>\n",
       "      <td>0</td>\n",
       "      <td>low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.80</td>\n",
       "      <td>262</td>\n",
       "      <td>0</td>\n",
       "      <td>medium</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.11</td>\n",
       "      <td>272</td>\n",
       "      <td>0</td>\n",
       "      <td>medium</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.72</td>\n",
       "      <td>223</td>\n",
       "      <td>0</td>\n",
       "      <td>low</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.37</td>\n",
       "      <td>159</td>\n",
       "      <td>0</td>\n",
       "      <td>low</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   satisfaction_level  average_montly_hours  promotion_last_5years  salary\n",
       "0                0.38                   157                      0     low\n",
       "1                0.80                   262                      0  medium\n",
       "2                0.11                   272                      0  medium\n",
       "3                0.72                   223                      0     low\n",
       "4                0.37                   159                      0     low"
      ]
     },
     "execution_count": 76,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "subdf = df[['satisfaction_level','average_montly_hours','promotion_last_5years','salary']]\n",
    "subdf.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Tackle salary dummy variable**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Salary has all text data. It needs to be converted to numbers and we will use dummy variable for that. Check my one hot encoding tutorial to understand purpose behind dummy variables."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "metadata": {},
   "outputs": [],
   "source": [
    "salary_dummies = pd.get_dummies(subdf.salary, prefix=\"salary\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "metadata": {},
   "outputs": [],
   "source": [
    "df_with_dummies = pd.concat([subdf,salary_dummies],axis='columns')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>satisfaction_level</th>\n",
       "      <th>average_montly_hours</th>\n",
       "      <th>promotion_last_5years</th>\n",
       "      <th>salary</th>\n",
       "      <th>salary_high</th>\n",
       "      <th>salary_low</th>\n",
       "      <th>salary_medium</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.38</td>\n",
       "      <td>157</td>\n",
       "      <td>0</td>\n",
       "      <td>low</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.80</td>\n",
       "      <td>262</td>\n",
       "      <td>0</td>\n",
       "      <td>medium</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.11</td>\n",
       "      <td>272</td>\n",
       "      <td>0</td>\n",
       "      <td>medium</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.72</td>\n",
       "      <td>223</td>\n",
       "      <td>0</td>\n",
       "      <td>low</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.37</td>\n",
       "      <td>159</td>\n",
       "      <td>0</td>\n",
       "      <td>low</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   satisfaction_level  average_montly_hours  promotion_last_5years  salary  \\\n",
       "0                0.38                   157                      0     low   \n",
       "1                0.80                   262                      0  medium   \n",
       "2                0.11                   272                      0  medium   \n",
       "3                0.72                   223                      0     low   \n",
       "4                0.37                   159                      0     low   \n",
       "\n",
       "   salary_high  salary_low  salary_medium  \n",
       "0            0           1              0  \n",
       "1            0           0              1  \n",
       "2            0           0              1  \n",
       "3            0           1              0  \n",
       "4            0           1              0  "
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_with_dummies.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Now we need to remove salary column which is text data. It is already replaced by dummy variables so we can safely remove it"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 81,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>satisfaction_level</th>\n",
       "      <th>average_montly_hours</th>\n",
       "      <th>promotion_last_5years</th>\n",
       "      <th>salary_high</th>\n",
       "      <th>salary_low</th>\n",
       "      <th>salary_medium</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.38</td>\n",
       "      <td>157</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.80</td>\n",
       "      <td>262</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.11</td>\n",
       "      <td>272</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.72</td>\n",
       "      <td>223</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.37</td>\n",
       "      <td>159</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   satisfaction_level  average_montly_hours  promotion_last_5years  \\\n",
       "0                0.38                   157                      0   \n",
       "1                0.80                   262                      0   \n",
       "2                0.11                   272                      0   \n",
       "3                0.72                   223                      0   \n",
       "4                0.37                   159                      0   \n",
       "\n",
       "   salary_high  salary_low  salary_medium  \n",
       "0            0           1              0  \n",
       "1            0           0              1  \n",
       "2            0           0              1  \n",
       "3            0           1              0  \n",
       "4            0           1              0  "
      ]
     },
     "execution_count": 81,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df_with_dummies.drop('salary',axis='columns',inplace=True)\n",
    "df_with_dummies.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 82,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>satisfaction_level</th>\n",
       "      <th>average_montly_hours</th>\n",
       "      <th>promotion_last_5years</th>\n",
       "      <th>salary_high</th>\n",
       "      <th>salary_low</th>\n",
       "      <th>salary_medium</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.38</td>\n",
       "      <td>157</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.80</td>\n",
       "      <td>262</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0.11</td>\n",
       "      <td>272</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.72</td>\n",
       "      <td>223</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.37</td>\n",
       "      <td>159</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   satisfaction_level  average_montly_hours  promotion_last_5years  \\\n",
       "0                0.38                   157                      0   \n",
       "1                0.80                   262                      0   \n",
       "2                0.11                   272                      0   \n",
       "3                0.72                   223                      0   \n",
       "4                0.37                   159                      0   \n",
       "\n",
       "   salary_high  salary_low  salary_medium  \n",
       "0            0           1              0  \n",
       "1            0           0              1  \n",
       "2            0           0              1  \n",
       "3            0           1              0  \n",
       "4            0           1              0  "
      ]
     },
     "execution_count": 82,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X = df_with_dummies\n",
    "X.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {},
   "outputs": [],
   "source": [
    "y = df.left"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 91,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split\n",
    "X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=0.3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 87,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "model = LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 88,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1.0, class_weight=None, dual=False, fit_intercept=True,\n",
       "          intercept_scaling=1, max_iter=100, multi_class='ovr', n_jobs=1,\n",
       "          penalty='l2', random_state=None, solver='liblinear', tol=0.0001,\n",
       "          verbose=0, warm_start=False)"
      ]
     },
     "execution_count": 88,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 89,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([0, 0, 0, ..., 0, 0, 1], dtype=int64)"
      ]
     },
     "execution_count": 89,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.predict(X_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**Accuracy of the model**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 90,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.78428571428571425"
      ]
     },
     "execution_count": 90,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(X_test,y_test)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
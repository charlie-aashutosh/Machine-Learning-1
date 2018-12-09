{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 style=\"color:green\" align=\"center\">Predicting if a person would buy life insurnace based on his age using logistic regression</h2>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Above is a binary logistic regression problem as there are only two possible outcomes (i.e. if person buys insurance or he/she doesn't). "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 106,
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
   "execution_count": 108,
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
       "      <th>age</th>\n",
       "      <th>bought_insurance</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>22</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>25</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>47</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>52</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>46</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age  bought_insurance\n",
       "0   22                 0\n",
       "1   25                 0\n",
       "2   47                 1\n",
       "3   52                 0\n",
       "4   46                 1"
      ]
     },
     "execution_count": 108,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(\"insurance_data.csv\")\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 109,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x2922f6bf390>"
      ]
     },
     "execution_count": 109,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXcAAAD8CAYAAACMwORRAAAABHNCSVQICAgIfAhkiAAAAAlwSFlz\nAAALEgAACxIB0t1+/AAADlZJREFUeJzt3X+s3fVdx/Hny3bE/XKd65XU/rCY1M1mDobHgpFoB9ls\n52JjshhAt0k0DQk1mGik+odGFxP9QzMJjNog4qKuWTZ0SHB14mCaiXKrDCiseFMYbcfGRWQmWyKp\nvP3jfLsdbtt7zr09t/fyOc9HctP7/X4/93w//fTwvF++5542VYUkqS3fsdwTkCSNn3GXpAYZd0lq\nkHGXpAYZd0lqkHGXpAYZd0lqkHGXpAYZd0lq0OrlOvHatWtr8+bNy3V6SXpVOnTo0PNVNTVs3LLF\nffPmzUxPTy/X6SXpVSnJl0cZ520ZSWqQcZekBhl3SWqQcZekBhl3SWqQcZekBhl3SWrQ0LgnuSPJ\nc0keO8vxJLk5yUySR5JcOv5pSpIWYpQr9zuBHfMc3wls6T52A7ed+7Qat317/0Mr00r585lvHos9\nthTnG7eV9Pte7NetgLUcGveq+jzwwjxDdgEfq74HgTVJ1o1rgpKkhRvHXz+wHjg2sH282/fsGB67\nLae+Wz/wwCu3779/GSaj06yUP5/55rHYY0txvnFbSb/vlTTPRTqvL6gm2Z1kOsn07Ozs+Ty1JE2U\nVNXwQclm4J6qevsZjv0JcH9VfbzbPgJsr6p5r9x7vV5N7F8c5hX7yrZS/nzmm8dijy3F+cZtJf2+\nF/t1S7iWSQ5VVW/YuHFcud8NfLD7qZnLga8PC7skaWkNvXJP8nFgO7AW+Brw28BrAKpqX5IAt9D/\niZpvAtdV1dBL8om+cpekRRr1yn3oC6pVdc2Q4wXcsIC5SZKWmO9QlaQGGXdJapBxl6QGGXdJapBx\nl6QGGXdJapBxl6QGGXdJapBxl6QGGXdJapBxl6QGGXdJapBxl6QGGXdJapBxl6QGGXdJapBxl6QG\nGXdJapBxl6QGGXdJapBxl6QGGXdJapBxl6QGGXdJapBxl6QGGXdJapBxl6QGGXdJapBxl6QGGXdJ\natBIcU+yI8mRJDNJ9p7h+JuS/G2SLyY5nOS68U9VkjSqoXFPsgq4FdgJbAWuSbJ1zrAbgMer6mJg\nO/CHSS4Y81wlSSMa5cp9GzBTVUer6iXgALBrzpgC3pgkwBuAF4CTY52pJGlko8R9PXBsYPt4t2/Q\nLcAPAl8BHgVurKqX5z5Qkt1JppNMz87OLnLKkqRhxvWC6k8CDwPfC1wC3JLku+YOqqr9VdWrqt7U\n1NSYTi1JmmuUuJ8ANg5sb+j2DboOuKv6ZoCngLeNZ4qSpIUaJe4PAVuSXNS9SHo1cPecMc8AVwEk\nuRB4K3B0nBOVJI1u9bABVXUyyR7gILAKuKOqDie5vju+D/gwcGeSR4EAN1XV80s4b0nSPIbGHaCq\n7gXunbNv38DnXwHeM96pSZIWy3eoSlKDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4\nS1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KD\njLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDRop7kh1JjiSZSbL3LGO2J3k4yeEk\nD4x3mpKkhVg9bECSVcCtwLuB48BDSe6uqscHxqwBPgrsqKpnknzPUk1YkjTcKFfu24CZqjpaVS8B\nB4Bdc8ZcC9xVVc8AVNVz452mJGkhRon7euDYwPbxbt+gHwDenOT+JIeSfHBcE5QkLdzQ2zILeJwf\nBq4CXgv8S5IHq+rJwUFJdgO7ATZt2jSmU0uS5hrlyv0EsHFge0O3b9Bx4GBVfaOqngc+D1w894Gq\nan9V9aqqNzU1tdg5S5KGGCXuDwFbklyU5ALgauDuOWM+DVyRZHWS1wGXAU+Md6qSpFENvS1TVSeT\n7AEOAquAO6rqcJLru+P7quqJJJ8BHgFeBm6vqseWcuKSpLNLVS3LiXu9Xk1PTy/LuSXp1SrJoarq\nDRvnO1QlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIa\nZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaZNwl\nqUHGXZIaZNwlqUHGXZIaZNwlqUHGXZIaNFLck+xIciTJTJK984z7kSQnk7x/fFOUJC3U0LgnWQXc\nCuwEtgLXJNl6lnF/APz9uCcpSVqYUa7ctwEzVXW0ql4CDgC7zjDul4FPAc+NcX6SpEUYJe7rgWMD\n28e7fd+SZD3wM8Bt8z1Qkt1JppNMz87OLnSukqQRjesF1Y8AN1XVy/MNqqr9VdWrqt7U1NSYTi1J\nmmv1CGNOABsHtjd0+wb1gANJANYC701ysqr+ZiyzlCQtyChxfwjYkuQi+lG/Grh2cEBVXXTq8yR3\nAvcYdklaPkPjXlUnk+wBDgKrgDuq6nCS67vj+5Z4jpKkBRrlyp2quhe4d86+M0a9qn7h3KclSToX\nvkNVkhpk3CWpQcZdkhpk3CWpQcZdkhpk3CWpQcZdkhpk3CWpQcZdkhpk3CWpQcZdkhpk3CWpQcZd\nkhpk3CWpQcZdkhpk3CWpQcZdkhpk3CWpQcZdkhpk3CWpQcZdkhpk3CWpQcZdkhpk3CWpQcZdkhpk\n3CWpQcZdkhpk3CWpQcZdkho0UtyT7EhyJMlMkr1nOP5zSR5J8miSLyS5ePxTlSSNamjck6wCbgV2\nAluBa5JsnTPsKeAnquqHgA8D+8c9UUnS6Ea5ct8GzFTV0ap6CTgA7BocUFVfqKr/7jYfBDaMd5qS\npIUYJe7rgWMD28e7fWfzi8DfncukJEnnZvU4HyzJu+jH/YqzHN8N7AbYtGnTOE8tSRowypX7CWDj\nwPaGbt8rJHkHcDuwq6r+60wPVFX7q6pXVb2pqanFzFeSNIJR4v4QsCXJRUkuAK4G7h4ckGQTcBfw\ngap6cvzTlCQtxNDbMlV1Mske4CCwCrijqg4nub47vg/4LeAtwEeTAJysqt7STVuSNJ9U1bKcuNfr\n1fT09LKcW5JerZIcGuXi2XeoSlKDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KD\njLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLsk\nNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNci4S1KDjLskNWikuCfZkeRIkpkke89wPElu7o4/\nkuTS8U+1s2ZN/+NMtm/vfyzUfF+32GPn+3xLMU/pXI37uedzeWRD455kFXArsBPYClyTZOucYTuB\nLd3HbuC2Mc9TkrQAq0cYsw2YqaqjAEkOALuAxwfG7AI+VlUFPJhkTZJ1VfXs2GZ66mr9619/5faL\nL377O/kDD/R/PbV9//3zP+Z8X7fYY+f7fEsxT+lcjfu553N5wUa5LbMeODawfbzbt9AxJNmdZDrJ\n9Ozs7ELnKkkaUfoX2/MMSN4P7KiqX+q2PwBcVlV7BsbcA/x+Vf1zt30fcFNVTZ/tcXu9Xk1Pn/Xw\n2Q1esc+12O/m833dYo+d7/MtxTylczXu557PZZIcqqresHGjXLmfADYObG/o9i10jCTpPBnlyn01\n8CRwFf1gPwRcW1WHB8b8FLAHeC9wGXBzVW2b73EXfeUuSRNs1Cv3oS+oVtXJJHuAg8Aq4I6qOpzk\n+u74PuBe+mGfAb4JXHcuk5cknZtRflqGqrqXfsAH9+0b+LyAG8Y7NUnSYvkOVUlqkHGXpAYZd0lq\nkHGXpAYZd0lqkHGXpAYZd0lq0NB3qC7ZiZNZ4Mvn+bRrgefP8zlXOtfkzFyX07kmp1uONfm+qpoa\nNmjZ4r4ckkyP8rbdSeKanJnrcjrX5HQreU28LSNJDTLuktSgSYv7/uWewArkmpyZ63I61+R0K3ZN\nJuqeuyRNikm7cpekidBs3JNsTPK5JI8nOZzkxm7/dyf5bJL/7H5983LP9XxJ8p1J/i3JF7s1+Z1u\n/8SuySlJViX5j+6fjJz4NUnydJJHkzycZLrbN+lrsibJJ5N8KckTSX50Ja9Js3EHTgK/WlVbgcuB\nG5JsBfYC91XVFuC+bntS/C9wZVVdDFwC7EhyOZO9JqfcCDwxsO2awLuq6pKBH/Wb9DX5Y+AzVfU2\n4GL6z5eVuyZVNREfwKeBdwNHgHXdvnXAkeWe2zKtx+uAf6f/zyJO9JrQ/zd/7wOuBO7p9k36mjwN\nrJ2zb2LXBHgT8BTd65SvhjVp+cr9W5JsBt4J/CtwYVU92x36KnDhMk1rWXS3Hx4GngM+W1UTvybA\nR4BfB14e2Dfpa1LAPyQ5lGR3t2+S1+QiYBb4s+723e1JXs8KXpPm457kDcCngF+pqv8ZPFb9b7cT\n9eNCVfV/VXUJ/avVbUnePuf4RK1JkvcBz1XVobONmbQ16VzRPU920r+l+eODBydwTVYDlwK3VdU7\ngW8w5xbMSluTpuOe5DX0w/6XVXVXt/trSdZ1x9fRv4KdOFX1IvA5YAeTvSY/Bvx0kqeBA8CVSf6C\nyV4TqupE9+tzwF8D25jsNTkOHO/+Txfgk/Rjv2LXpNm4Jwnwp8ATVfVHA4fuBj7Uff4h+vfiJ0KS\nqSRrus9fS/81iC8xwWtSVb9RVRuqajNwNfCPVfXzTPCaJHl9kjee+hx4D/AYE7wmVfVV4FiSt3a7\nrgIeZwWvSbNvYkpyBfBPwKN8+17qb9K/7/4JYBP9v5XyZ6vqhWWZ5HmW5B3AnwOr6H9j/0RV/W6S\ntzChazIoyXbg16rqfZO8Jkm+n/7VOvRvR/xVVf3eJK8JQJJLgNuBC4CjwHV0/x2xAtek2bhL0iRr\n9raMJE0y4y5JDTLuktQg4y5JDTLuktQg4y5JDTLuktQg4y5JDfp/lGl7q+CJlocAAAAASUVORK5C\nYII=\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x2922f59a0b8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(df.age,df.bought_insurance,marker='+',color='red')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 83,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 99,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train, X_test, y_train, y_test = train_test_split(df[['age']],df.bought_insurance,train_size=0.9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
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
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    age\n",
       "25   54\n",
       "24   50\n",
       "21   26"
      ]
     },
     "execution_count": 100,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "model = LogisticRegression()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 102,
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
     "execution_count": 102,
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
   "execution_count": 104,
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
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    age\n",
       "25   54\n",
       "24   50\n",
       "21   26"
      ]
     },
     "execution_count": 104,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 111,
   "metadata": {},
   "outputs": [],
   "source": [
    "y_predicted = model.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 105,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 0.25566869,  0.74433131],\n",
       "       [ 0.29592482,  0.70407518],\n",
       "       [ 0.58520192,  0.41479808]])"
      ]
     },
     "execution_count": 105,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.predict_proba(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 110,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 110,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model.score(X_test,y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "metadata": {
    "scrolled": true
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
       "      <th>age</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>54</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>50</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "    age\n",
       "25   54\n",
       "24   50\n",
       "21   26"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X_test"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "<h2 style=\"color:purple\">Exercise</h2>\n",
    "\n",
    "Download employee retention dataset from here: https://www.kaggle.com/giripujar/hr-analytics. \n",
    "1. Now do some exploratory data analysis to figure out which variables have direct and clear impact on employee retention (i.e. whether they leave the company or continue to work)\n",
    "2. Plot bar charts showing impact of employee salaries on retention\n",
    "3. Plot bar charts showing corelation between department and employee retention\n",
    "4. Now build logistic regression model using variables that were narrowed down in step 1\n",
    "5. Measure the accuracy of the model"
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
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-09-23T16:49:45.619532Z",
     "start_time": "2020-09-23T16:49:45.477803Z"
    }
   },
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-09-23T17:02:04.962292Z",
     "start_time": "2020-09-23T17:01:43.667231Z"
    },
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
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "      <th>5</th>\n",
       "      <th>6</th>\n",
       "      <th>7</th>\n",
       "      <th>8</th>\n",
       "      <th>9</th>\n",
       "      <th>...</th>\n",
       "      <th>16</th>\n",
       "      <th>17</th>\n",
       "      <th>18</th>\n",
       "      <th>19</th>\n",
       "      <th>20</th>\n",
       "      <th>21</th>\n",
       "      <th>22</th>\n",
       "      <th>23</th>\n",
       "      <th>24</th>\n",
       "      <th>25</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>DOT_NUMBER</td>\n",
       "      <td>LEGAL_NAME</td>\n",
       "      <td>DBA_NAME</td>\n",
       "      <td>CARRIER_OPERATION</td>\n",
       "      <td>HM_FLAG</td>\n",
       "      <td>PC_FLAG</td>\n",
       "      <td>PHY_STREET</td>\n",
       "      <td>PHY_CITY</td>\n",
       "      <td>PHY_STATE</td>\n",
       "      <td>PHY_ZIP</td>\n",
       "      <td>...</td>\n",
       "      <td>TELEPHONE</td>\n",
       "      <td>FAX</td>\n",
       "      <td>EMAIL_ADDRESS</td>\n",
       "      <td>MCS150_DATE</td>\n",
       "      <td>MCS150_MILEAGE</td>\n",
       "      <td>MCS150_MILEAGE_YEAR</td>\n",
       "      <td>ADD_DATE</td>\n",
       "      <td>OIC_STATE</td>\n",
       "      <td>NBR_POWER_UNIT</td>\n",
       "      <td>DRIVER_TOTAL</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>FEDERAL MOTOR CARRIER SAFETY ADMINISTRATION</td>\n",
       "      <td>FMCSA TECHNOLOGY DIVISION</td>\n",
       "      <td>A</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "      <td>1200 NEW JERSEY AVENUE SE</td>\n",
       "      <td>WASHINGTON</td>\n",
       "      <td>DC</td>\n",
       "      <td>20590</td>\n",
       "      <td>...</td>\n",
       "      <td>(202) 385-2363</td>\n",
       "      <td>NaN</td>\n",
       "      <td>JEFF.LOFTUS@DOT.GOV</td>\n",
       "      <td>16-DEC-19</td>\n",
       "      <td>3000</td>\n",
       "      <td>2019</td>\n",
       "      <td>01-JUN-74</td>\n",
       "      <td>DC</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10000</td>\n",
       "      <td>POWELL DISTRIBUTING CO INC</td>\n",
       "      <td>NaN</td>\n",
       "      <td>A</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "      <td>9125 N BURRAGE</td>\n",
       "      <td>PORTLAND</td>\n",
       "      <td>OR</td>\n",
       "      <td>97217</td>\n",
       "      <td>...</td>\n",
       "      <td>(503) 289-5558</td>\n",
       "      <td>(503) 735-0100</td>\n",
       "      <td>JASON@POWELLOIL.COM</td>\n",
       "      <td>25-JUN-20</td>\n",
       "      <td>10000</td>\n",
       "      <td>2019</td>\n",
       "      <td>01-JUN-74</td>\n",
       "      <td>OR</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1000000</td>\n",
       "      <td>JAMES EARL KILLINGSWORTH JR</td>\n",
       "      <td>JAMES KILLINGSWORTH TRUCKING</td>\n",
       "      <td>A</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "      <td>15 GASLINE ROAD</td>\n",
       "      <td>PHENIX CITY</td>\n",
       "      <td>AL</td>\n",
       "      <td>36870</td>\n",
       "      <td>...</td>\n",
       "      <td>(706) 325-1816</td>\n",
       "      <td>NaN</td>\n",
       "      <td>JIMBOSPLICE2469@YAHOO.COM</td>\n",
       "      <td>18-MAY-20</td>\n",
       "      <td>1</td>\n",
       "      <td>2019</td>\n",
       "      <td>23-JAN-02</td>\n",
       "      <td>AL</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1000002</td>\n",
       "      <td>NEW JERSEY BOOM &amp; ERECTORS INC</td>\n",
       "      <td>NaN</td>\n",
       "      <td>A</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "      <td>405 INDUSTRIAL PARK DRIVE</td>\n",
       "      <td>MOUNT POCONO</td>\n",
       "      <td>PA</td>\n",
       "      <td>18344</td>\n",
       "      <td>...</td>\n",
       "      <td>(570) 620-1546</td>\n",
       "      <td>(570) 620-1517</td>\n",
       "      <td>GAIL@NJBOOM.COM</td>\n",
       "      <td>03-FEB-20</td>\n",
       "      <td>40000</td>\n",
       "      <td>2019</td>\n",
       "      <td>22-JAN-02</td>\n",
       "      <td>PA</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "           0                                            1   \\\n",
       "0  DOT_NUMBER                                   LEGAL_NAME   \n",
       "1           1  FEDERAL MOTOR CARRIER SAFETY ADMINISTRATION   \n",
       "2       10000                   POWELL DISTRIBUTING CO INC   \n",
       "3     1000000                  JAMES EARL KILLINGSWORTH JR   \n",
       "4     1000002               NEW JERSEY BOOM & ERECTORS INC   \n",
       "\n",
       "                             2                  3        4        5   \\\n",
       "0                      DBA_NAME  CARRIER_OPERATION  HM_FLAG  PC_FLAG   \n",
       "1     FMCSA TECHNOLOGY DIVISION                  A        N        N   \n",
       "2                           NaN                  A        N        N   \n",
       "3  JAMES KILLINGSWORTH TRUCKING                  A        N        N   \n",
       "4                           NaN                  A        N        N   \n",
       "\n",
       "                          6             7          8        9   ...  \\\n",
       "0                 PHY_STREET      PHY_CITY  PHY_STATE  PHY_ZIP  ...   \n",
       "1  1200 NEW JERSEY AVENUE SE    WASHINGTON         DC    20590  ...   \n",
       "2             9125 N BURRAGE      PORTLAND         OR    97217  ...   \n",
       "3            15 GASLINE ROAD   PHENIX CITY         AL    36870  ...   \n",
       "4  405 INDUSTRIAL PARK DRIVE  MOUNT POCONO         PA    18344  ...   \n",
       "\n",
       "               16              17                         18           19  \\\n",
       "0       TELEPHONE             FAX              EMAIL_ADDRESS  MCS150_DATE   \n",
       "1  (202) 385-2363             NaN        JEFF.LOFTUS@DOT.GOV    16-DEC-19   \n",
       "2  (503) 289-5558  (503) 735-0100        JASON@POWELLOIL.COM    25-JUN-20   \n",
       "3  (706) 325-1816             NaN  JIMBOSPLICE2469@YAHOO.COM    18-MAY-20   \n",
       "4  (570) 620-1546  (570) 620-1517            GAIL@NJBOOM.COM    03-FEB-20   \n",
       "\n",
       "               20                   21         22         23              24  \\\n",
       "0  MCS150_MILEAGE  MCS150_MILEAGE_YEAR   ADD_DATE  OIC_STATE  NBR_POWER_UNIT   \n",
       "1            3000                 2019  01-JUN-74         DC               4   \n",
       "2           10000                 2019  01-JUN-74         OR               1   \n",
       "3               1                 2019  23-JAN-02         AL               1   \n",
       "4           40000                 2019  22-JAN-02         PA               2   \n",
       "\n",
       "             25  \n",
       "0  DRIVER_TOTAL  \n",
       "1             4  \n",
       "2             1  \n",
       "3             1  \n",
       "4             1  \n",
       "\n",
       "[5 rows x 26 columns]"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('./assets/data/FMCSA_CENSUS1_2020Aug.txt', \n",
    "                 sep=\"\\s{4}\", \n",
    "                 delimiter=',',\n",
    "                 header=None, \n",
    "                 engine='python')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-09-23T17:01:22.981507Z",
     "start_time": "2020-09-23T17:01:22.978958Z"
    }
   },
   "outputs": [],
   "source": [
    "# Reset column names (read with col names in row 0)\n",
    "columns = df.iloc[0]\n",
    "df = df[1:]\n",
    "df.columns= df.loc[0:]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-09-23T17:01:26.726809Z",
     "start_time": "2020-09-23T17:01:26.709797Z"
    }
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
       "      <th>0</th>\n",
       "      <th>1</th>\n",
       "      <th>2</th>\n",
       "      <th>3</th>\n",
       "      <th>4</th>\n",
       "      <th>5</th>\n",
       "      <th>6</th>\n",
       "      <th>7</th>\n",
       "      <th>8</th>\n",
       "      <th>9</th>\n",
       "      <th>...</th>\n",
       "      <th>16</th>\n",
       "      <th>17</th>\n",
       "      <th>18</th>\n",
       "      <th>19</th>\n",
       "      <th>20</th>\n",
       "      <th>21</th>\n",
       "      <th>22</th>\n",
       "      <th>23</th>\n",
       "      <th>24</th>\n",
       "      <th>25</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>FEDERAL MOTOR CARRIER SAFETY ADMINISTRATION</td>\n",
       "      <td>FMCSA TECHNOLOGY DIVISION</td>\n",
       "      <td>A</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "      <td>1200 NEW JERSEY AVENUE SE</td>\n",
       "      <td>WASHINGTON</td>\n",
       "      <td>DC</td>\n",
       "      <td>20590</td>\n",
       "      <td>...</td>\n",
       "      <td>(202) 385-2363</td>\n",
       "      <td>NaN</td>\n",
       "      <td>JEFF.LOFTUS@DOT.GOV</td>\n",
       "      <td>16-DEC-19</td>\n",
       "      <td>3000</td>\n",
       "      <td>2019</td>\n",
       "      <td>01-JUN-74</td>\n",
       "      <td>DC</td>\n",
       "      <td>4</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>10000</td>\n",
       "      <td>POWELL DISTRIBUTING CO INC</td>\n",
       "      <td>NaN</td>\n",
       "      <td>A</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "      <td>9125 N BURRAGE</td>\n",
       "      <td>PORTLAND</td>\n",
       "      <td>OR</td>\n",
       "      <td>97217</td>\n",
       "      <td>...</td>\n",
       "      <td>(503) 289-5558</td>\n",
       "      <td>(503) 735-0100</td>\n",
       "      <td>JASON@POWELLOIL.COM</td>\n",
       "      <td>25-JUN-20</td>\n",
       "      <td>10000</td>\n",
       "      <td>2019</td>\n",
       "      <td>01-JUN-74</td>\n",
       "      <td>OR</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1000000</td>\n",
       "      <td>JAMES EARL KILLINGSWORTH JR</td>\n",
       "      <td>JAMES KILLINGSWORTH TRUCKING</td>\n",
       "      <td>A</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "      <td>15 GASLINE ROAD</td>\n",
       "      <td>PHENIX CITY</td>\n",
       "      <td>AL</td>\n",
       "      <td>36870</td>\n",
       "      <td>...</td>\n",
       "      <td>(706) 325-1816</td>\n",
       "      <td>NaN</td>\n",
       "      <td>JIMBOSPLICE2469@YAHOO.COM</td>\n",
       "      <td>18-MAY-20</td>\n",
       "      <td>1</td>\n",
       "      <td>2019</td>\n",
       "      <td>23-JAN-02</td>\n",
       "      <td>AL</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1000002</td>\n",
       "      <td>NEW JERSEY BOOM &amp; ERECTORS INC</td>\n",
       "      <td>NaN</td>\n",
       "      <td>A</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "      <td>405 INDUSTRIAL PARK DRIVE</td>\n",
       "      <td>MOUNT POCONO</td>\n",
       "      <td>PA</td>\n",
       "      <td>18344</td>\n",
       "      <td>...</td>\n",
       "      <td>(570) 620-1546</td>\n",
       "      <td>(570) 620-1517</td>\n",
       "      <td>GAIL@NJBOOM.COM</td>\n",
       "      <td>03-FEB-20</td>\n",
       "      <td>40000</td>\n",
       "      <td>2019</td>\n",
       "      <td>22-JAN-02</td>\n",
       "      <td>PA</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1000004</td>\n",
       "      <td>RAY TRUCKING LLC</td>\n",
       "      <td>NaN</td>\n",
       "      <td>C</td>\n",
       "      <td>N</td>\n",
       "      <td>N</td>\n",
       "      <td>218 PEACHTREE ST</td>\n",
       "      <td>WARWICK</td>\n",
       "      <td>GA</td>\n",
       "      <td>31796</td>\n",
       "      <td>...</td>\n",
       "      <td>(229) 535-4140</td>\n",
       "      <td>NaN</td>\n",
       "      <td>MONTOYARAY@YMAIL.COM</td>\n",
       "      <td>01-JUN-20</td>\n",
       "      <td>25000</td>\n",
       "      <td>2019</td>\n",
       "      <td>22-JAN-02</td>\n",
       "      <td>GA</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 26 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "        0                                            1   \\\n",
       "1        1  FEDERAL MOTOR CARRIER SAFETY ADMINISTRATION   \n",
       "2    10000                   POWELL DISTRIBUTING CO INC   \n",
       "3  1000000                  JAMES EARL KILLINGSWORTH JR   \n",
       "4  1000002               NEW JERSEY BOOM & ERECTORS INC   \n",
       "5  1000004                             RAY TRUCKING LLC   \n",
       "\n",
       "                             2  3  4  5                          6   \\\n",
       "1     FMCSA TECHNOLOGY DIVISION  A  N  N  1200 NEW JERSEY AVENUE SE   \n",
       "2                           NaN  A  N  N             9125 N BURRAGE   \n",
       "3  JAMES KILLINGSWORTH TRUCKING  A  N  N            15 GASLINE ROAD   \n",
       "4                           NaN  A  N  N  405 INDUSTRIAL PARK DRIVE   \n",
       "5                           NaN  C  N  N           218 PEACHTREE ST   \n",
       "\n",
       "             7   8      9   ...              16              17  \\\n",
       "1    WASHINGTON  DC  20590  ...  (202) 385-2363             NaN   \n",
       "2      PORTLAND  OR  97217  ...  (503) 289-5558  (503) 735-0100   \n",
       "3   PHENIX CITY  AL  36870  ...  (706) 325-1816             NaN   \n",
       "4  MOUNT POCONO  PA  18344  ...  (570) 620-1546  (570) 620-1517   \n",
       "5       WARWICK  GA  31796  ...  (229) 535-4140             NaN   \n",
       "\n",
       "                          18         19     20    21         22  23 24 25  \n",
       "1        JEFF.LOFTUS@DOT.GOV  16-DEC-19   3000  2019  01-JUN-74  DC  4  4  \n",
       "2        JASON@POWELLOIL.COM  25-JUN-20  10000  2019  01-JUN-74  OR  1  1  \n",
       "3  JIMBOSPLICE2469@YAHOO.COM  18-MAY-20      1  2019  23-JAN-02  AL  1  1  \n",
       "4            GAIL@NJBOOM.COM  03-FEB-20  40000  2019  22-JAN-02  PA  2  1  \n",
       "5       MONTOYARAY@YMAIL.COM  01-JUN-20  25000  2019  22-JAN-02  GA  2  1  \n",
       "\n",
       "[5 rows x 26 columns]"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.7.6"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}

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
   "execution_count": 2,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-09-23T16:50:14.367958Z",
     "start_time": "2020-09-23T16:50:14.062793Z"
    }
   },
   "outputs": [
    {
     "ename": "UnicodeDecodeError",
     "evalue": "'utf-8' codec can't decode byte 0xa0 in position 26: invalid start byte",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mUnicodeDecodeError\u001b[0m                        Traceback (most recent call last)",
      "\u001b[0;32mpandas/_libs/parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader._convert_tokens\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader._convert_with_dtype\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader._string_convert\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers._string_box_utf8\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;31mUnicodeDecodeError\u001b[0m: 'utf-8' codec can't decode byte 0xa0 in position 26: invalid start byte",
      "\nDuring handling of the above exception, another exception occurred:\n",
      "\u001b[0;31mUnicodeDecodeError\u001b[0m                        Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-2-3c8dbe60b30d>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mdf\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mpd\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread_csv\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"./assets/data/FMCSA_CENSUS1_2020Aug.txt\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mdf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mhead\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/pandas/io/parsers.py\u001b[0m in \u001b[0;36mparser_f\u001b[0;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, dialect, error_bad_lines, warn_bad_lines, delim_whitespace, low_memory, memory_map, float_precision)\u001b[0m\n\u001b[1;32m    674\u001b[0m         )\n\u001b[1;32m    675\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 676\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0m_read\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilepath_or_buffer\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mkwds\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    677\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    678\u001b[0m     \u001b[0mparser_f\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m__name__\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mname\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/pandas/io/parsers.py\u001b[0m in \u001b[0;36m_read\u001b[0;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[1;32m    452\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    453\u001b[0m     \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 454\u001b[0;31m         \u001b[0mdata\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mparser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnrows\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    455\u001b[0m     \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    456\u001b[0m         \u001b[0mparser\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclose\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/pandas/io/parsers.py\u001b[0m in \u001b[0;36mread\u001b[0;34m(self, nrows)\u001b[0m\n\u001b[1;32m   1131\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnrows\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1132\u001b[0m         \u001b[0mnrows\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_validate_integer\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"nrows\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnrows\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1133\u001b[0;31m         \u001b[0mret\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_engine\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnrows\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1134\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1135\u001b[0m         \u001b[0;31m# May alter columns / col_dict\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/anaconda3/lib/python3.7/site-packages/pandas/io/parsers.py\u001b[0m in \u001b[0;36mread\u001b[0;34m(self, nrows)\u001b[0m\n\u001b[1;32m   2035\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnrows\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mNone\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2036\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2037\u001b[0;31m             \u001b[0mdata\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_reader\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mnrows\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2038\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mStopIteration\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2039\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_first_chunk\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader.read\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader._read_low_memory\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader._read_rows\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader._convert_column_data\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader._convert_tokens\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader._convert_with_dtype\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers.TextReader._string_convert\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;32mpandas/_libs/parsers.pyx\u001b[0m in \u001b[0;36mpandas._libs.parsers._string_box_utf8\u001b[0;34m()\u001b[0m\n",
      "\u001b[0;31mUnicodeDecodeError\u001b[0m: 'utf-8' codec can't decode byte 0xa0 in position 26: invalid start byte"
     ]
    }
   ],
   "source": [
    "df = pd.read_csv(\"./assets/data/FMCSA_CENSUS1_2020Aug.txt\")\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "ExecuteTime": {
     "end_time": "2020-09-23T16:51:49.392613Z",
     "start_time": "2020-09-23T16:51:49.386102Z"
    }
   },
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'path' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-3-eb025fc11c03>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpath\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'rb'\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m   \u001b[0mcontents\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mNameError\u001b[0m: name 'path' is not defined"
     ]
    }
   ],
   "source": [
    "with open(path, 'rb') as f:\n",
    "  contents = f.read()"
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

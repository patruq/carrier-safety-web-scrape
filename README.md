# carrier-safety-web-scrape

## Instructions:
1) Scrape the "Carrier Registration Details" page for each operator in
the "Motor Carrier Census Information" file.
    - Pull the lists of cargo carried.
    - Pull the vehicle type breakout table.
2) Output a `csv`.

### Bonus:
1) Find variations, `Nan` and missing values.
2) Develop a light scrape tool.

--- 
# Methodology
- ***Raw Data***
    - Downloaded raw `.txt` from site.
    - Extracted `DOT_NUMBER` col
- ***Webscraper***
    - Organized the `DOT_NUMBER` in a list of dictionaries of the dot_number and updated `url` with dot_number inserted.
    - The `robots.txt` file specified the following conditions for the webscrape:
            
            User-agent: Speedy
            Crawl-Delay: 60
            User-agent: msnbot 
            Crawl-delay: 60
            User-agent: Slurp
            Crawl-delay: 6
            User-agent: *
            Crawl-delay: 60
    
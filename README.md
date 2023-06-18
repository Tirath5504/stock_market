# Stock Market

#### Video Demo: "link"

#### Description: 

A basic stock market data science app that displays stock price of GOOGLE and MICROSOFT.

It uses the *streamlit* library to deploy the web application and tabulate and graphically represent the data.

It uses the *yfinance* library to take in the information and stock price data of the aforementioned companies.

I run the app using the streamlit hosting service, although I could have used heroku.
The application can also be run via the command line interface with the following command: 

` streamlit run project.py `

I have devised three custom functions:
+ history(comp, time)
    + This function takes in a *comp* and a *time* input as parameters.
    + *comp* is a ticker object containing data about which company (abbreviated) I want the stock market prices.
    + The *time* variable denotes the time duration for which I want the data. 
    + The function returns data of stock market prices of the mentioned company for the mentioned time period which we
      can use to tabulate in the form of a graph.
  

+ download(tag, start, end)
  + This function takes in a *tag*, *start* and an *end* input as parameters.
  + *tag* is a string which provides the stock market code of the company which we want the data of.
  + The *start* and *end* variables denotes the time duration in the day for which I want the stock market price. 
  + The function returns data of stock market information of the mentioned company for the mentioned time period in the
  day which we can use to tabulate in the form of a table.


+ get_ticker(tag)
  + This function takes in only one variable, *tag* as a parameter.
  + *tag* is a string which provides the stock market code of the company which we want the data of.
  + The function returns a ticket object (from *yfinance* API) which we can use to get all sorts of information of the 
  above-mentioned company.
  

I have also made a test_project() python file which tests all the above-mentioned functions. It finds the stock market
of the company ****Tesla.inc**** (*TSLA*).

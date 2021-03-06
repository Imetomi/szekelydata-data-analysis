# SzékelyData Data Visualisation Contest Entry by Tamás Imets

This repository contains the tools and programs I made to analyze the `data.json` dataset. I used Jupyter and Python for data processing and decoding then switched to JS, HTML, and Django for making a website that you can check out [here](http://imetomi.pythonanywhere.com). The site basically shows where the Székelys live, where were they born, where did they move, and etc. 

### The Story
I have never tried to visualize such a big ammount of data before, but I had some experience with big data handling in Python. I knew from start that I want make a Google Earth like geographical plot. Browsing the web I found the WebGL Globe (three.js) framework and I built up the cralified data in Jupyter. This is how it looks now: 

<img src="https://github.com/Imetomi/szekelydata-data-analysis/blob/master/earth.PNG">

After creating the globe I used D3.js to create a beaufiful chord diagram. You can check out both of them on my website. I also have some static plots on the site, but those are not so interesting since my data analysis algorithm wasn't the best at the time of plotting.  

<img src="https://github.com/Imetomi/szekelydata-data-analysis/blob/master/chord.PNG">

### Guidance

If you want to run the Python program or you will need to install the libraries listed in `dependencies.txt` and of course you will need Jupyter Notebook. If you are looking for the Django code that one is in another repository.

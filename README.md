# NOAA-Refined-Stations
This repository contains some refined NOAA measurement stations data to provide a unified dataset for future work on applications of ocean wave energy. It has been gathered by the authors of the paper ...
and its purpose is solely for accademic research.   

As mentioned by https://www.ndbc.noaa.gov/download_data.php, use of NOAA/NWS Data and Products is as follows:
The information on National Weather Service (NWS) Web pages are in the public domain, unless specifically noted otherwise, and may be used without charge for any lawful purpose so long as you do not: 1) claim it is your own (e.g., by claiming copyright for NWS information -- see below), 2) use it in a manner that implies an endorsement or affiliation with NOAA/NWS, or 3) modify its content and then present it as official government material. You also cannot present information of your own in a way that makes it appear to be official government information. 

Furthermore, as mentioned by https://www7.ncdc.noaa.gov/CDO/cdoselect.cmd?datasetabbv=GSOD&countryabbv=IR&georegionabbv=&resolution=40: 
The following data and products may have conditions placed on their international commercial use. They can be used within the U.S. or for non-commercial international activities without restriction. The non-U.S. data cannot be redistributed for commercial purposes. Re-distribution of these data by others must provide this same notification. A log of IP addresses accessing these data and products will be maintained and may be made available to data providers 
One must agrees to above-mentioned terms to use any data from this repository.  

We define Refined-Stations as those stations where 
i) The station was active up to 2017 
ii) It has a year with at least 1000 clean data points.

"refinedStations" file contains such stations. The format is [Station ID, list[year]]. For instance:
['46084', [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]]. You may notice the year 2009 is missing. It means that in the year 2009, less than 1000 accurate data points where measured. 

Forecasting and reconstruction folders contain some of the refined stations data which are used in the paper. Missing points have only been omitted without anymore changes. 


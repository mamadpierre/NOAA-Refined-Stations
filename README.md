# NOAA-Refined-Stations
This repository contains some refined NOAA measurement stations data to provide a unified dataset for future work on applications of ocean wave energy. It has been gathered by the authors of the papers "Multivariate Multistep Forecasting, Reconstruction and Feature Selection of Ocean Wave Features via Recurrent and Sequence-to-Sequence Networks" and "Feature Engineering and Forecasting via Derivative-free Optimization and Ensemble of Sequence-to-sequence Networks with Applications in Renewable Energy" and its purpose is solely for accademic research.   

As mentioned by https://www.ndbc.noaa.gov/download_data.php, the guideline for proper usage of NOAA/NWS Data and Products is as follows:
The information on National Weather Service (NWS) Web pages are in the public domain, unless specifically noted otherwise, and may be used without charge for any lawful purpose so long as you do not: 1) claim it is your own (e.g., by claiming copyright for NWS information -- see below), 2) use it in a manner that implies an endorsement or affiliation with NOAA/NWS, or 3) modify its content and then present it as official government material. You also cannot present information of your own in a way that makes it appear to be official government information. 

Furthermore, as mentioned by https://www7.ncdc.noaa.gov/CDO/cdoselect.cmd?datasetabbv=GSOD&countryabbv=IR&georegionabbv=&resolution=40: 
The following data and products may have conditions placed on their international commercial use. They can be used within the U.S. or for non-commercial international activities without restriction. The non-U.S. data cannot be redistributed for commercial purposes. Re-distribution of these data by others must provide this same notification. A log of IP addresses accessing these data and products will be maintained and may be made available to data providers 
One must agrees to above-mentioned terms to use any data from this repository.  

We define Refined-Stations as those stations where 
i) The station was active up to 2017 
ii) It has a year with at least 1000 clean data points.

"refinedStations" file contains such stations. The format is [Station ID, list[year]]. For instance:
['46084', [2002, 2003, 2004, 2005, 2006, 2007, 2008, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]]. You may notice the year 2009 is missing. It means that in the year 2009, less than 1000 accurate data points where measured. 

Forecasting, reconstruction and feature selection folders contain some of the refined stations data which are used in the paper. Missing points have only been omitted without anymore changes. 

Citaiton:

@article{pirhooshyaran2019multivariate,

  title={Multivariate, multistep forecasting, reconstruction and feature selection of ocean waves via recurrent and sequence-to-sequence networks},
  
  author={Pirhooshyaran, Mohammad and Snyder, Lawrence V},
  
  journal={arXiv preprint arXiv:1906.00195},
  
  year={2019}
  
}


@article{pirhooshyaran2019feature,

  title={Feature Engineering and Forecasting via Derivative-free Optimization and Ensemble of Sequence-to-sequence Networks with Applications in Renewable Energy},
  
  author={Pirhooshyaran, Mohammad and Scheinberg, Katya and Snyder, Lawrence V},
  
  journal={arXiv preprint arXiv:1909.05447},
  
  year={2019}
  
}

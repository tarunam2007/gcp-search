# Search on Google Cloud Platform

Open Cloud Shell and set your region and zone
1)	Copy the Code file from Git 
 git clone https://github.com/tarunam2007/gcp-search.git

2)	Extract Data from Best buy data set : I used only 15000 skus(1.5GB) as data was really big
•	Upload data to Bucket : Buckets/tarunam-autocomplete/products--> 71 Product Xmls
•	Use gsutil to copy Data from bucket to cloud shell current directory:
	gsutil cp -r gs://tarunam-autocomplete/products . 
•	Change the Data Location to Dataset:extract data/extract_product_data.py
•	Converts XML to CSV with header : 'sku', 'name', 'regularPrice', 'salePrice', 'type', 'url', 'image', 'inStoreAvailability'
•	Also before running the python file please import XMLtoDICT module by running below command:
   o	sudo pip install xmltodict
   o	inside folder extract_product_data python extract_product_data.py 
•	After successful transformation you will get an “best_buy_products.csv” under extract data folder 15K skus

3)	Creating Index from CSV file : Connecting to GAE search API for indexing the fields 
-	I am not using “Setting” file at parent level as somehow I was having issue so directly used variables into index file
-	 Before loading indexes run below commands
cd gae_search_api/webapp/
   o	sudo pip install -r requirements.txt -t lib
   o	cd gae_search_api/load_data
   o	python upload.py
-	This will create Indexes in GAE dashboard
4)	Deploy Web App to GAE 
cd gae_search_api/webapp/
o	sudo pip install -r requirements.txt -t lib
-	Above command will create folder under Webapp
-	Deploy the App: cd gae_search_api/webapp/
o	gcloud app deploy . –promote
o	gcloud app deploy -v search –promote
-	Access application: GAE Dashboard
-------------------------------------------------------Thanks from previous dev-----------------------------------------------------
this repository contains examples of applications which have "search" functionality using different GCP products and services.
every example is described in detail with blog article.

Examples:
1. [Search API and Google App Engine](https://www.the-swamp.info/blog/search-google-cloud-platform-app-engine-and-search-api/)
2. [Cloud Datastore](https://www.the-swamp.info/blog/search-google-cloud-platform-cloud-datastore/)
3. [Cloud SQL](https://www.the-swamp.info/blog/search-google-cloud-platform-cloud-sql/) 

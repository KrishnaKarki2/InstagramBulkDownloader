# InstagramBulkDownloader
Bulk-download photos from public Instagram profiles. No Instagram login required. 

### DISCLAIMER: 
**By using this software, you agree to the following terms**
* **No Liability**: The author is not responsible for any misuse of this tool, nor any account suspensions, IP bans, or legal actions taken against you by third-party platforms
* **Respect Platform Terms**: You are solely responsible for complying with Instagram's Terms of Service and robots.txt limitations 
* **Ethical Use Only**: Do not use this tool to scrape private data, harass individuals, or redistribute content without the explicit consent of the original creator(s)
* **User Responsibility**: You assume all risks associated with the use of this software

**Instagram Terms of Service:** https://help.instagram.com/581066165581870/ 

**This tool is not affiliated with Instagram, Meta, or Apify** 

<br>

## Introduction 

This tool was created because many similar bulk downloader tools get blocked from datacenter IPs (such as Google Colab), request account logins (putting your account at risk), or offer a limited bulk download on a free plan. This repository offers a risk-free way of handing bulk downloads using Apify's hosted scraper over the cloud rather than with your IP. Photos can be later downloaded onto your computer. 

## Usage 
### Set-up (Google Colab)
1. Make a free Apify account, copy your API token: https://console.apify.com/account/integrations

2. Open json-extractor.ipynb in Google Colab, and paste your API token
https://github.com/KrishnaKarki2/InstagramBulkDownloader/blob/0e7d8817fa3a60080d00f331a5758b254e886f9e/json-extractor.ipynb#L29

3. Add your desired profiles in the usernames list 
https://github.com/KrishnaKarki2/InstagramBulkDownloader/blob/65b66bc4e3153f6bafb1eddf636eff7e6b645102/json-extractor.ipynb#L31-L33

4. Run the cell

5. Once the cell has completed running, go to https://console.apify.com/storage/datasets and download the dataset as a JSON file

6. Make a folder with the newly created JSON file and photodownloaders.py 

7. In your terminal / VS Code, add the name of your json file to this line 
https://github.com/KrishnaKarki2/InstagramBulkDownloader/blob/9aa4ab363e0ad1c32e0614573d8ad11d22948f76/photodownloader.py#L5

8. Run 
```
python photodownloader.py
# this will not work in Colab as Instagram frequently blocks datacenter IPs
```

#### After you have completed these steps, photos should go into photos/ subfolders by username 

### Have fun 


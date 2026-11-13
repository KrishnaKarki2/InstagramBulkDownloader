# InstagramBulkDownloader
Bulk-download photos from public Instagram profiles. No Instagram login required. 

### DISCLAIMER: 
By using this software, you agree to the following terms
* **No Liability**: The author is not responsible for any misuse of this tool, nor any account suspensions, IP bans, or legal actions taken against you by third-party platforms
* **Respect Platform Terms**: You are solely responsible for complying with Instagram's Terms of Service and robots.txt limitations; 
* **Ethical Use Only**: Do not use this tool to scrape private data, harass individuals, or redistribute content without the explicit consent of the original creator(s)
* **User Responsibility**: You assume all risks associated with the use of this software

Instagram Terms of Service: https://help.instagram.com/581066165581870/ 

**This tool is not affiliated with Instagram, Meta, or Apify** 

<br>

## Introduction 

This tool was created because many similar bulk downloader tools get blocked from datacenter IPs (such as Google Colab), request account logins (putting your account at risk), or offer a limited bulk download on a free plan. This repository offers a risk-free way of handing bulk downloads using Apify's hosted scraper over the cloud rather than with your IP. Photos can be later downloaded onto your computer. 

## Usage 

1. Make a free Apify account, copy your API token: https://console.apify.com/account/integrations
2. Open json-extractor.ipynb (preferably in Google Colab), and paste your API token
3. Add your desired profiles in line 8 
4. Run the cell


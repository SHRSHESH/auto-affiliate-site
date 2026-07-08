import os
import requests
from datetime import datetime

SITE_DIR = r"D:\hermes-portable\workspace\affiliate-site"
SITE_URL = "https://shrshesh.github.io/auto-affiliate-site"
URLS = [
    "/",
    "/productivity.html",
    "/software.html",
    "/about.html",
    "/privacy.html",
    "/disclosure.html",
]

def generate_sitemap():
    sitemap_path = os.path.join(SITE_DIR, "sitemap.xml")
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')
    for path in URLS:
        lines.append(f"  <url><loc>{SITE_URL}{path}</loc><lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod><changefreq>daily</changefreq><priority>0.8</priority></url>")
    lines.append('</urlset>')
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"SITEMAP_CREATED: {sitemap_path}")
    return sitemap_path

def submit_to_bing():
    try:
        url = f"https://www.bing.com/powershell/webmasters/SubmitUrlToSearchEngine.ashx"
        params = {"siteUrl": SITE_URL}
        resp = requests.get(url, params=params, timeout=15)
        print(f"BING_SUBMIT: status={resp.status_code}, response={resp.text[:200]}")
    except Exception as e:
        print(f"BING_SUBMIT_ERROR: {e}")

def submit_to_baidu():
    # Baidu requires site verification; provide manual links as fallback
    print("BAIDU_MANUAL: https://ziyuan.baidu.com/linksubmit/url")
    print(f"BAIDU_URL: {SITE_URL}/")

def submit_to_sogou():
    # Sogou requires site verification; provide manual links as fallback
    print("SOGOU_MANUAL: https://fankui.sogou.com/")
    print(f"SOGOU_URL: {SITE_URL}/")

def main():
    print("SEARCH_ENGINE_SUBMISSION")
    generate_sitemap()
    submit_to_bing()
    submit_to_baidu()
    submit_to_sogou()
    print("SUBMISSION_COMPLETE")

if __name__ == "__main__":
    main()

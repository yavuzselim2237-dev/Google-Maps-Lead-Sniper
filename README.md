# 🛡️ Google Maps Lead Sniper (B2B Intelligence Engine)

A professional-grade automation tool designed for **Global Lead Generation** and **Market Intelligence**. This engine automates the discovery of local businesses across any geographic location and extracts verified lead data using Deep DOM Crawling.

## 🚀 Strategic Features

- **Automated Reconnaissance:** Handles infinite scrolling and dynamic content loading on complex UI structures.
- **Deep Email Crawling:** Does not stop at the homepage. The engine dynamically hunts for "Contact" or "About" sub-pages and extracts encrypted or hidden emails using strict Regex validation.
- **Stealth Architecture:** Utilizes persistent sessions and automation-masking to avoid detection and maintain a high 'Human-Score'.
- **B2B Targeting:** Perfect for digital marketing agencies, SaaS companies, and recruiters.

## ⚠️ Commercial Notice & Limitations

This repository contains the **Lite Version** of the engine for portfolio demonstration purposes only. To protect proprietary logic, the following features are disabled:
1. Limited to single-thread sequential scanning (Throttled execution).
2. Social Media Radar (LinkedIn, Instagram extraction) is locked.
3. Advanced phone number parsing is disabled.

## 🎯 Proof of Concept (Terminal Execution)
*Example output showing the Deep Crawl routing in action:*

```text
[*] Intelligence Node Active. Target: Dentists in London
[*] Engaging search interface...
[+] Target grid locked. Initiating scroll sequence...
[*] Discovered 6 nodes. Penetrating top 5...
    [>] Analyzing: Da Vinci Clinic...
    [OK] Captured | Email: info@davinciclinic.co.uk
    [>] Analyzing: Harley Street Dental Clinic (HSDC London)...
        [~] Shallow scan negative. Initiating Deep Crawl routing...
    [OK] Captured | Email: info@hsdc.net
    [>] Analyzing: Dental Smiles London | Euston Practice...
        [~] Shallow scan negative. Initiating Deep Crawl routing...
    [OK] Captured | Email: Not Found (Encrypted/Hidden)

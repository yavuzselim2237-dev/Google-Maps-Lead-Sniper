import asyncio
import random
import re
import pandas as pd
from playwright.async_api import async_playwright

class MapsLeadSniper:
    """
    Enterprise B2B Lead Generation Engine.
    Features: Automated G-Maps reconnaissance, Dynamic routing, and Deep Email Crawling.
    """
    def __init__(self, category, location):
        self.query = f"{category} in {location}"
        self.leads = []
        self.session_dir = "gmaps_auth_session"
        # Professional Regex pattern for strict Email validation
        self.email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")

    async def _apply_stealth(self, page):
        """Masks automation fingerprints."""
        await page.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    async def _hunt_email(self, browser, website_url):
        """
        Dual-Phase Email Extraction:
        1. Shallow Scan (Homepage)
        2. Deep Crawl (Contact/About pages routing)
        """
        if not website_url or "google.com" in website_url:
            return "N/A"
            
        page = await browser.new_page()
        try:
            # PHASE 1: Shallow Scan
            await page.goto(website_url, timeout=15000, wait_until="domcontentloaded")
            body_text = await page.inner_text("body")
            emails_found = self.email_pattern.findall(body_text)
            
            if emails_found:
                return emails_found[0].lower()

            # PHASE 2: Deep Crawl Routing
            print("        [~] Shallow scan negative. Initiating Deep Crawl routing...")
            
            # Find the 'Contact' or 'About' link dynamically
            contact_url = await page.evaluate("""
                () => {
                    const links = Array.from(document.querySelectorAll('a'));
                    const target = links.find(a => {
                        if (!a.href) return false;
                        const text = a.innerText.toLowerCase();
                        const href = a.href.toLowerCase();
                        return (text.includes('contact') || text.includes('about') || text.includes('iletişim') || href.includes('contact'));
                    });
                    return target ? target.href : null;
                }
            """)

            if contact_url and contact_url.startswith('http'):
                # Infiltrate the sub-page
                await page.goto(contact_url, timeout=15000, wait_until="domcontentloaded")
                deep_body_text = await page.inner_text("body")
                deep_emails = self.email_pattern.findall(deep_body_text)
                
                if deep_emails:
                    return deep_emails[0].lower()
                    
            return "Not Found (Encrypted/Hidden)"
            
        except Exception:
            return "Connection Timeout/Protected"
        finally:
            await page.close()

    async def execute_recon(self, scan_limit: int = 10):
        async with async_playwright() as p:
            context = await p.chromium.launch_persistent_context(
                self.session_dir,
                headless=False,
                args=['--disable-blink-features=AutomationControlled'],
                ignore_default_args=['--enable-automation'],
                viewport={'width': 1366, 'height': 768}
            )
            
            page = context.pages[0] if context.pages else await context.new_page()
            await self._apply_stealth(page)

            print(f"[*] Intelligence Node Active. Target: {self.query}")
            await page.goto("https://www.google.com/maps?hl=en", wait_until="domcontentloaded")

            try:
                consent_btn = page.get_by_role("button", name=re.compile("Accept all|Agree|Tümünü kabul et", re.IGNORECASE))
                await consent_btn.first.click(timeout=5000)
            except: pass

            print("[*] Engaging search interface...")
            search_box = await page.wait_for_selector("input[name='q']")
            await search_box.fill(self.query)
            await page.keyboard.press("Enter")
            
            try:
                await page.wait_for_selector('div[role="feed"]', timeout=20000)
                print("[+] Target grid locked. Initiating scroll sequence...")
            except:
                print("[!] Timeout waiting for results. Check network or manual CAPTCHA.")

            # Scroll to load businesses
            for i in range(4):
                await page.mouse.wheel(0, 3000)
                await asyncio.sleep(2)

            listings = await page.locator('div[role="article"]').all()
            print(f"[*] Discovered {len(listings)} nodes. Penetrating top {scan_limit}...")

            for index, listing in enumerate(listings[:scan_limit]):
                try:
                    name_el = listing.locator('div.qBF1Pd')
                    if await name_el.count() == 0: continue
                    name = await name_el.inner_text()

                    await listing.click()
                    await asyncio.sleep(2.5)

                    website_url = None
                    website_el = page.locator('a[data-item-id="authority"]')
                    if await website_el.count() > 0:
                        website_url = await website_el.get_attribute("href")

                    print(f"    [>] Analyzing: {name}...")
                    email = await self._hunt_email(context, website_url)

                    self.leads.append({
                        'Business Name': name,
                        'Website': website_url if website_url else "N/A",
                        'Contact Email': email,
                        'Lead Status': 'Verified' if '@' in email else 'Unreachable'
                    })
                    print(f"    [OK] Captured | Email: {email}")
                    
                except Exception as e:
                    print(f"    [!] Node Error: {str(e)[:30]}")
                    continue

            if self.leads:
                df = pd.DataFrame(self.leads)
                df.to_excel("gmaps_lead_intelligence.xlsx", index=False)
                print(f"\n[FINISH] Operation complete. Lead data secured in gmaps_lead_intelligence.xlsx")
            else:
                print("\n[!] Zero leads extracted. Mission failed.")
            
            await context.close()

if __name__ == "__main__":
    recon = MapsLeadSniper("Dentists", "London")
    asyncio.run(recon.execute_recon(scan_limit=5))

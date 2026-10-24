# Shared, factual analytics wording for every site's privacy page (EN, formal ZH, Cantonese ZH).
# Source for the Cloudflare claims: https://www.cloudflare.com/web-analytics/ ("does not use any client-side
# state, such as cookies or localStorage ... We also don't 'fingerprint' individuals via their IP address,
# User Agent string, or any other data for the purpose of displaying analytics").
def en(links="WhatsApp, phone or email link", extra=""):
    return [
     ("Website analytics (no cookies)", [
      "We use Cloudflare Web Analytics to count visits to this website and see which pages are read. It does not use cookies or local storage, and Cloudflare says it does not fingerprint visitors by IP address, browser or any other data. It records things like the page viewed, the page you came from, browser and device type, country and how fast the page loaded.",
      f"When you tap a {links} or send a form, the page also loads a tiny blank counter page on this website (for example /go/whatsapp/), so we can count how many people get in touch. It does not record who you are or anything you type or send.",
      "We don't use Google Analytics, advertising pixels or tracking cookies on this website. To opt out of the count, block static.cloudflareinsights.com in your browser or content blocker." + (" " + extra if extra else "")])]
def zh(links="WhatsApp、電話或電郵連結", extra=""):
    return [
     ("網站分析（不使用 Cookie）", [
      "我們使用 Cloudflare Web Analytics 統計本網站的瀏覽次數及被瀏覽的頁面。它不使用 Cookie 或本機儲存（localStorage）；Cloudflare 表示不會透過 IP 位址、瀏覽器或其他資料識別個別訪客。系統會記錄瀏覽的頁面、來源頁面、瀏覽器及裝置類型、國家／地區及頁面載入速度等資料。",
      f"當你按下{links}或提交表格時，頁面會同時載入本網站一個空白的計數頁（例如 /go/whatsapp/），讓我們統計有多少人聯絡我們。它不會記錄你的身份，亦不會記錄你輸入或傳送的內容。",
      "本網站不使用 Google Analytics、廣告像素或追蹤 Cookie。如不希望被計算，可在瀏覽器或內容封鎖工具中封鎖 static.cloudflareinsights.com。" + (extra or "")])]
def yue(links="WhatsApp、電話或者電郵連結", extra=""):
    return [
     ("網站統計（唔用 Cookie）", [
      "我哋用 Cloudflare Web Analytics 統計本網站有幾多人睇、睇咗邊啲頁。佢唔會用 Cookie 或者本機儲存（localStorage）；Cloudflare 表示唔會用 IP 地址、瀏覽器或者其他資料去辨認個別訪客。佢會記錄你睇嘅頁面、由邊個頁面過嚟、瀏覽器同裝置類型、國家／地區，同埋頁面載入速度。",
      f"當你撳{links}或者交表格嗰陣，頁面會同時載入本網站一個空白嘅計數頁（例如 /go/whatsapp/），等我哋知道有幾多人搵我哋。佢唔會記錄你係邊個，亦唔會記錄你打咗或者傳咗乜嘢。",
      "本網站冇用 Google Analytics、廣告像素或者追蹤 Cookie。如果唔想被計算，可以喺瀏覽器或者內容封鎖工具封鎖 static.cloudflareinsights.com。" + (extra or "")])]

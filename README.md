# Xyno

OSINT Scrapers mostly scrapy

Rough format is `[org_][munic_]state_country` IE `cary_nc_us`

## nc\_us

For North Carolina General Assembly

### reps

* [ ] Scrape the member lists and provide page `{flavor: 'page', date: $date, url: $url, title: $title, hashed: $hashed}`
  * [House](https://ncleg.gov/Members/MemberList/H)
  * [Senate](https://ncleg.gov/Members/MemberList/S)
* [ ] Scrape each biography from those pages providing 'page' dictionary defined above
* [ ] Scrape each district for map (May be simpler to just grab from dl.ncsbe.gov)

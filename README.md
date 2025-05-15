# Xyno

OSINT Scrapers mostly scrapy

Rough format is `[org_][munic_]state_country` IE `cary_nc_us`

## nc\_us

For North Carolina General Assembly

### reps

* [x] Scrape the member lists and provide page `{flavor: 'page', date: $date, url: $url, title: $title, hashed: $hashed}`
  * [House](https://ncleg.gov/Members/MemberList/H)
  * [Senate](https://ncleg.gov/Members/MemberList/S)
* [x] Scrape each biography from those pages providing 'page' dictionary defined above
  * [x] Scrape Introduced bills
  * [x] Scrape Votes
  * [x] Scrape Committees
  * [ ] Extract bio details
    * [Eric Ager](https://ncleg.gov/Members/Biography/H/819)
      * [ ] Name
      * [ ] Party
      * [ ] Elected Office
      * [ ] District
      * [ ] Legislative Office
      * [ ] Mailing Address
      * [ ] Terms
      * [ ] Occupation
      * [ ] Main Phone
      * [ ] Military
      * [ ] Experience (presumed military)
      * [ ] Member's Email
      * [ ] Legislative Assistant
* [ ] Scrape each district for map (May be simpler to just grab from dl.ncsbe.gov)

import scrapy


class RepSpider(scrapy.Spider):
    name = "rep"
    allowed_domains = ["ncleg.gov"]
    start_urls = ["https://ncleg.gov/Members/Biography/H/819"]
    usable_key = {
            'Legislative Office:': 'legislative_office',
            }

    def parse(self, response):
        url = response.url
        # name
        title = response.css('title::text').get()
        honorific_name = title.split(' - ')[0]
        name = honorific_name.split(' ', 1)[1]
        # party
        # This needs cleanup to DEM/REP from ncvoter.  Currently (Par)
        party = response.css('h1.section-title::text').get().split(' ')[-1]
        # elected_office
        # This needs cleanup to nc_house/nc_senate current Senator/Representative
        elected_office = honorific_name.split(' ')[0]
        box = response.css('div.row.ncga-row-no-gutters')[0]
        # district
        district = box.css('h6.text-nowrap::text').get().split(' ')[-1]
        # Legislative Office
        # Mailing Address
        # Terms
        # Occupation
        # Main Phone
        # Military
        # Experience (presumed military)
        # Member's Email
        # Legislative Assistant
        fields = self.get_fields(box)
        yield dict(
                url=url,
                title=title,
                name=name,
                party=party,
                district=district,
                **fields
                )

    def get_fields(self, box):
        fields = {}
        key = None
        for x in box.css('*'):
            potential_key = ''
            if x.root.tag in ('h6', 'p'):
                potential_key = x.css('*::text').get() or ''
            if potential_key.endswith(':'):
                key = ''.join(potential_key[:-1].split(' '))
                continue
            if key and x.root.tag in ('h6', 'p'):
                fields.setdefault(key, [])
                fields[key].append(potential_key)
            if key and x.root.tag in ('a'):
                fields.setdefault(key + 'Href', [])
                fields[key + 'Href'].append(x.attrib.get('href'))
        return fields



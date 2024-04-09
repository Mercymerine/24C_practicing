'''
import re

pattern = re.compile('^Hello') #takes a string as its argument, which represents the regular expression pattern

result = pattern.search('Hello, world!') # searches for the first occurrence of the pattern in the string, and returns a match object if the pattern is found, or None otherwise


print(result)

result2 = pattern.findall('Hello, world! Hello')

print(result2)

result3 = pattern.finditer('Hello, world! Hello')
for match in result3:
    print(match.start(), match.end(), match.group())
    '''
'''
import re

text = 'Elon musk`s phone number is 9991116666, call him if you have any question on dodgecoin. Tesla`s revenue is 40 billion. Tesla`s CFO number (999)-333-7777'

pattern = '\(\d{3}\)-\d{3}-\d{4}|\d{10}'

matches = re.findall(pattern, text)
print(matches)
'''

import re

text = '''Note 1 – Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 – Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods'''

pattern = 'Note \d ([^\n]*)'

matches = re.findall(pattern, text)

print(matches)

texts = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion
In previous quarter i e fY2020 Q4 it was $3 billion
FY2030 Q5'''

patterns = 'FY(\d{4} Q[1-4])'

matchezz = re.findall(patterns, texts, flags = re.IGNORECASE)
print(matchezz)

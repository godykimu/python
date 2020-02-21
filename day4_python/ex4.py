swahili = dict()
swahili['hello'] = 'Jambo'
swahili['blue'] = 'Samawati'

print("{} shati langu ni la {}".format(swahili['hello'],swahili['blue']))
output = "{hello} shati langu ni la {blue}".format(**swahili)
print(output)
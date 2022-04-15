from bs4 import BeautifulSoup

text = '''
<html>
<head>
    <title>The Dormouse's Story</title>
</head>

<body>
    <p class="title"><b>The Dormouse's Story</b></p>

    <p class="story">Once upon a time there were
        three little sisters; their names:
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.
    </p>

    <p class="story">...</p>

    <b class="boldest">Extremely bold</b>
    <blockquote class="boldest">Extremely bold</blockquote>
    <b id="1">Test 1</b>
    <b another.attribute="1" id="verybold">Test 2</b>
    <p id="my id"></p>
<body>
</html>
'''
with open('index.html', 'w') as f:
    f.write(text)

soup = BeautifulSoup(text)

# >>> Contemplate:
# print(soup.prettify())

print("1. Print 1st bold tag: ")
print(soup.b)
print()

print("2. Again print first bold tag: ")
print(soup.find('b'))
print()

print("3. Print all bold tags: ")
print(soup.find_all('b'))
print()

print("4. Print name of tag:")
print(soup.b.name)
print()

print("5. Alter tag: ")
tag = soup.b
print(tag)
tag.name = "blockqoute"
print(tag)
print

print("6. Print specific tag number: ")
tagx = soup.find_all('b')[2]
print(tagx)
print()

print("7. Print tag id: ")
print(tagx['id'])
print()

print("8. Print all attributes: ")
print(tag.attrs)
print(tagx.attrs)
print()

print("9. Alter Attribute, since all are muteable: ")
print(tagx)
tagx['another.attribute'] = 2
print(tagx)
print()

print("10. Delete Attribute: ")
print(tagx)
del tagx['id']
print(tagx)

print("11. Print Content of Tag: ")
print(tag.string)
print(tagx.string)
print()

print("12. Muteable Content of tags: ")
print(tag)
tag.string.replace_with("These are just variables in Py-Env!!")
print(tag)
print()
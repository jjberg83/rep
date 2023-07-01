def potatoes(theStr):
    print(theStr.count("potato"))

potatoes("potato")
potatoes("potatopotatocherry")
potatoes("potatopotatopotatoorange")
potatoes("potatopotatobananapotatopotato")
potatoes("potatopotatomangopotatopotatopotato")
potatoes("potatocucumberpotatopotatopotatopotatopotato")

"""
Test.assert_equals(potatoes("potato"), 1)
Test.assert_equals(potatoes("potatopotatocherry"),2 )
Test.assert_equals(potatoes("potatopotatopotatoorange"), 3)
Test.assert_equals(potatoes("potatopotatobananapotatopotato"), 4)
Test.assert_equals(potatoes("potatopotatomangopotatopotatopotato"), 5)
Test.assert_equals(potatoes("potatocucumberpotatopotatopotatopotatopotato"), 6)
"""
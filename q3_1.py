import json 
x = {
"""1) What do we call a newly hatched butterfly??
a. A moth
b.A chrysalis
""":"b",
"""2)  Which did Viking people use as money? ?
a.Seal skins
b.Jewellery
""":"a",
"""3) Which of these mobile brands have you heard of?
a.apple
b.sony
""":"a",
"""4) What was the first country to use tanks in combat during World War I?
a.Germany
b.Japan
""":"a",
"""5) What is the capital of German?
a.Berlin
b.Paris
""":"a",
"""6) Which of the following disorders is the fear of being alone? ?
a.Agoraphobia
b.Arachnophobia
""":"a",
"""7) What is the speed of sound? ?
a. 1,200 km/h
b.700 km/h
""":"a",
"""8) Which of the following is a song by the German heavy metal band “Scorpions”?
a.Wind of Change
b.Hey Jude
""":"a",
"""9)Which is the easiest way to tell the age of many trees??
a.To measure the width of the tree
b.To count the number of leaves
""":"a",
"""10) What is the capital of Egypt ?
a.Cairo
b.Paris
""":"a",
"""11) Goulash is a type of beef soup in which country ?
a.Slovakia
b.Hungary
""":"b",
"""12) What is the main component of the sun ?
a. Gas
b.Molten iron
""":"b",
    """13)  Which two months are named after Emperors of the Roman Empire ?
a.May and June
b.March and April
""":"a",

"""14)Which of the following animals can run the fastest?
a.dog
b.Cheetah
""":"b",}
bb = json.dumps(x)
with open("bb.json","w")as f:
    f.write(bb)